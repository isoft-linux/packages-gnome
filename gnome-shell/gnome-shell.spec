Name:		gnome-shell
Version:	3.20.0
Release:	2
Summary:	Window management and application launching for GNOME

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
Patch0:     gnome-shell-default-tweak.patch
Patch1:     gnome-shell-hide-calendar-events.patch
Patch2:     gnome-shell-default-favorite.patch
Patch3:     gnome-shell-disable-hot-corner.patch

## Needed when we re-autogen
BuildRequires:  autoconf >= 2.53
BuildRequires:  automake >= 1.10
BuildRequires:  gnome-common >= 2.2.0
BuildRequires:  libtool >= 1.4.3
BuildRequires:  caribou-devel
BuildRequires:  chrpath
BuildRequires:  clutter-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  evolution-data-server-devel
BuildRequires:  gcr-devel
BuildRequires:  gjs-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection
BuildRequires:  json-glib-devel
BuildRequires:  upower-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libnm-gtk-devel
BuildRequires:  NetworkManager-glib-devel
BuildRequires:  polkit-devel
BuildRequires:  startup-notification-devel
BuildRequires:  telepathy-glib-devel
BuildRequires:  telepathy-logger-devel
# for screencast recorder functionality
BuildRequires:  gstreamer-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libcanberra-devel
BuildRequires:  libcanberra-gtk3-devel
BuildRequires:  libcroco-devel
BuildRequires:  python3

# for barriers
BuildRequires:  libXfixes-devel
# used in unused BigThemeImage
BuildRequires:  librsvg2-devel
BuildRequires:  mutter-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  gnome-bluetooth-devel >= %{gnome_bluetooth_version}

#We should seperate gnome-control-centor to bin/devel package.
BuildRequires:  gnome-control-center

# Bootstrap requirements
BuildRequires: gtk-doc gnome-common
Requires:       gnome-bluetooth
Requires:       gnome-desktop3
Requires:       gnome-session
Requires:       gobject-introspection
Requires:       gjs
Requires:       gtk3
# needed for loading SVG's via gdk-pixbuf
Requires:       librsvg2
# needed as it is now split from Clutter
Requires:       json-glib
Requires:       libgsystem
# For $libdir/mozilla/plugins
Requires:       mutter
Requires:       upower
Requires:       polkit
Requires:       gsettings-desktop-schemas
Requires:       libcroco
Requires:       telepathy-logger
# needed for schemas
Requires:       at-spi2-atk
# needed for on-screen keyboard
Requires:       caribou
# needed for the user menu
Requires:       accountsservice-libs
Requires:       gdm
Requires:       clutter
Requires:  gnome-control-center
# needed by some utilities
Requires:       python3

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
* Mon Apr 11 2016 sulit <sulitsrc@gmail.com> - 3.20.0-2
- update to release 3.20.0

* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Fri Nov 06 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-3
- Add more requires

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

