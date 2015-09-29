Name: gnome-screenshot	
Version: 3.18.0
Release: 1
Summary: A screenshot utility for GNOME	

Group: Desktop/Gnome/Application	
License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

%description
The GNOME Screenshot is an utility used for taking screenshots of the entire screen, a window or an user- defined area of the screen, with optional beautifying border effects.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} DATADIRNAME=share

%find_lang gnome-screenshot
rpmclean

%post
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f gnome-screenshot.lang
%{_bindir}/gnome-screenshot
%{_datadir}/GConf/gsettings/gnome-screenshot.convert
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-screenshot.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Screenshot.service
%{_datadir}/appdata/org.gnome.Screenshot.appdata.xml
%{_mandir}/man1/gnome-screenshot.1.gz


%changelog
* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

