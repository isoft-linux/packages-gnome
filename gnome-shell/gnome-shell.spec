Name:		gnome-shell
Version:	3.18.1
Release:	2
Summary:	Window management and application launching for GNOME

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
Patch0:     gnome-shell-default-tweak.patch
Patch1:     gnome-shell-hide-calendar-events.patch
Patch2:     gnome-shell-default-favorite.patch
Patch3:     gnome-shell-disable-hot-corner.patch

BuildRequires:	caribou
BuildRequires:  evolution-data-server-devel
BuildRequires:  libcanberra-gtk3-devel
BuildRequires:  clutter-devel
BuildRequires:  cogl-devel
BuildRequires:  libcroco-devel
BuildRequires:  gcr-devel 
BuildRequires:  gstreamer-devel
BuildRequires:  libical-devel
BuildRequires:  json-glib-devel
BuildRequires:  mutter-devel >= 3.14
BuildRequires:  mozjs24-devel
BuildRequires:  libnm-gtk-devel
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  polkit-devel
BuildRequires:  pulseaudio-libs-devel 
BuildRequires:  libsecret-devel
BuildRequires:  sqlite-devel
BuildRequires:  startup-notification-devel
BuildRequires:  systemd-devel
BuildRequires:  telepathy-glib-devel
BuildRequires:  gnome-control-center
BuildRequires:  gjs-devel

Requires: caribou
Requires: gjs
%description
GNOME Shell provides core user interface functions for the GNOME 3 desktop,
like switching to windows and launching applications. GNOME Shell takes
advantage of the capabilities of modern graphics hardware and introduces
innovative user interface concepts to provide a visually attractive and
easy to use experience.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.



%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CC=cc
export CXX=c++
%configure --enable-systemd --enable-compile-warnings=no 
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

sed -i 's@#!/bin/python@#!/usr/bin/python@g' $RPM_BUILD_ROOT%{_bindir}/gnome-shell-extension-tool
sed -i 's@#!/bin/python@#!/usr/bin/python@g' $RPM_BUILD_ROOT%{_bindir}/gnome-shell-perf-tool

%find_lang gnome-shell


%post
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-shell.lang
%{_bindir}/gnome-shell
%{_bindir}/gnome-shell-extension-prefs
%{_bindir}/gnome-shell-extension-tool
%{_bindir}/gnome-shell-perf-tool
%dir %{_libdir}/gnome-shell
%{_libdir}/gnome-shell/*
%{_libdir}/mozilla/plugins/libgnome-shell-browser-plugin.so
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell-perf-helper
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/applications/evolution-calendar.desktop
%{_datadir}/applications/gnome-shell-extension-prefs.desktop
%{_datadir}/applications/gnome-shell.desktop
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-gnome-shell-system.xml
%dir %{_datadir}/gnome-shell
%{_datadir}/gnome-shell/*
%{_mandir}/man1/gnome-shell.1.gz
%{_libexecdir}/gnome-shell-portal-helper
%{_datadir}/applications/gnome-shell-wayland.desktop
%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service

#only docs
%files devel 
%{_datadir}/gtk-doc/html/shell
%{_datadir}/gtk-doc/html/st

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

