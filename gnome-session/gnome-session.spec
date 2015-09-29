%global _changelog_trimtime %(date +%s -d "1 year ago")

%define po_package gnome-session-3.0
%define _default_patch_fuzz 2

Summary: GNOME session manager
Name: gnome-session
Version: 3.18.0
Release: 2 
URL: http://www.gnome.org
Source0: http://download.gnome.org/sources/gnome-session/3.12/%{name}-%{version}.tar.xz
 
Patch1: gnome-session-3.3.92-nv30.patch
Patch2: 0001-main-Set-XDG_MENU_PREFIX.patch
Patch3: gnome-session-3.6.2-swrast.patch

Patch4: gnome-session-remove-use-rpmatch.patch

License: GPLv2+
Group:  Desktop/Gnome/Runtime/Base 

Requires: gsettings-desktop-schemas >= 0.1.7

# pull in dbus-x11, see bug 209924
Requires: dbus-x11

BuildRequires: gtk3-devel >= 2.99.0
BuildRequires: dbus-glib-devel
BuildRequires: gnome-desktop3-devel
BuildRequires: libnotify-devel >= 0.7.0
BuildRequires: pango-devel
BuildRequires: gnome-settings-daemon-devel
BuildRequires: desktop-file-utils
BuildRequires: libXau-devel
BuildRequires: libXrandr-devel
BuildRequires: xorg-x11-xtrans-devel
BuildRequires: mesa-libGL-devel
BuildRequires: librsvg2-devel
BuildRequires: json-glib-devel

BuildRequires: intltool, autoconf, automake
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libX11-devel libXt-devel
BuildRequires: libXtst-devel
BuildRequires: xmlto
BuildRequires: upower-devel
BuildRequires: gnome-common
BuildRequires: systemd-devel
BuildRequires: polkit-devel

# an artificial requires to make sure we get dconf, for now
Requires: dconf

%description
gnome-session manages a GNOME desktop or GDM login session. It starts up
the other core GNOME components and handles logout and saving the session.

%prep
%setup -q
%patch1 -p1 -b .nv30
%patch2 -p1 -b .set-xdg-menu-prefix
%patch3 -p1 -b .swrast
%patch4 -p1

echo "ACLOCAL_AMFLAGS = -I m4" >> Makefile.am

autoreconf -i -f

%build
export CC=cc
export CXX=c++
%configure --enable-docbook-docs                                \
           --enable-session-selector                            \
           --enable-systemd
make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{po_package}


rpmclean
%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
  gtk3-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
gtk3-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

#%files xsession

#%files wayland-session

%files -f %{po_package}.lang
%doc AUTHORS COPYING NEWS README
%doc %{_mandir}/man*/*
%{_bindir}/*
%{_libexecdir}/gnome-session-check-accelerated
%{_libexecdir}/gnome-session-check-accelerated-helper
%{_libexecdir}/gnome-session-failed
%{_datadir}/gnome-session/
%{_datadir}/icons/hicolor/*/apps/session-properties.png
%{_datadir}/icons/hicolor/scalable/apps/session-properties.svg
%{_datadir}/icons/hicolor/symbolic/apps/session-properties-symbolic.svg
%{_datadir}/GConf/gsettings/gnome-session.convert
%{_datadir}/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
%{_datadir}/xsessions/*
%{_datadir}/wayland-sessions/*
%{_docdir}/gnome-session/dbus/gnome-session.html

%changelog
* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

