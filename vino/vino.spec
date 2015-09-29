Name: vino	
Version: 3.18.0
Release: 1
Summary: A remote desktop system for GNOME	

Group: Desktop/Gnome/Runtime
License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz
BuildRequires: telepathy-glib-devel
BuildRequires: avahi-glib-devel
BuildRequires: libsecret-devel 
%description
Vino is a VNC server for GNOME. It allows remote users to
connect to a running GNOME session using VNC.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} DATADIRNAME=share

%find_lang vino
rpmclean

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f vino.lang
%{_datadir}/applications/vino-server.desktop
%{_libexecdir}/vino-server
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vino.service
%{_datadir}/glib-2.0/schemas/org.gnome.Vino.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Vino.gschema.xml
%{_datadir}/telepathy/clients/Vino.client


%changelog
* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18


