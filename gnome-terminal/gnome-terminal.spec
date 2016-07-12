Name: gnome-terminal	
Version: 3.20.2
Release: 1
Summary: Terminal emulator for GNOME	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

BuildRequires: dbus-x11
BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: vte3-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: autoconf automake libtool
BuildRequires: itstool
BuildRequires: dconf-devel
BuildRequires: libuuid-devel
BuildRequires: nautilus-devel
BuildRequires: appstream-glib
BuildRequires: vala-devel
BuildRequires: evolution-data-server
BuildRequires: gnome-shell

%description
gnome-terminal is a terminal emulator for GNOME. It features the ability to use
multiple terminals in a single window (tabs) and profiles support.

%prep
%setup -q

%build
%configure \
  --disable-static \
  --disable-migration \
  --disable-schemas-compile \
  --disable-gterminal \
  --with-gtk=3.0 \
  --with-nautilus-extension

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang gnome-terminal

%post
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-terminal.lang
%{_bindir}/gnome-terminal
%{_libdir}/nautilus/extensions-3.0/libterminal-nautilus.so
#%{_libexecdir}/gnome-terminal-migration
%{_libexecdir}/gnome-terminal-server
%{_datadir}/appdata/gnome-terminal.appdata.xml
%{_datadir}/applications/gnome-terminal.desktop
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_datadir}/gnome-shell/search-providers/gnome-terminal-search-provider.ini
%{_datadir}/help/*/gnome-terminal



%changelog
* Mon Jul 11 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.2-1
- Update

* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

