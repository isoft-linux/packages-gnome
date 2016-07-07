Name:		caribou
Version:	0.4.20
Release:	1
Summary:    A simplified in-place on-screen keyboard

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
Patch0:     caribou_ignore_intltool_check.patch

BuildRequires:	pygobject3-devel libgee-devel, libxklavier-devel, 
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(clutter-1.0)
Requires:	pygobject3

%description
On-screen Keyboard for GNOME 

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang caribou

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f caribou.lang
%{_sysconfdir}/xdg/autostart/caribou-autostart.desktop
#%{_bindir}/caribou
%{_bindir}/caribou-preferences
%{_libdir}/girepository-1.0/Caribou-1.0.typelib
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/caribou-gtk-module.desktop
%{_libdir}/gtk-2.0/modules/libcaribou-gtk-module.so
%{_libdir}/gtk-3.0/modules/libcaribou-gtk-module.so
%{_libdir}/libcaribou.so.*
%{_libdir}/python2.7/site-packages/caribou
%{_libexecdir}/antler-keyboard
%dir %{_datadir}/antler
%{_datadir}/antler/dark-key-border.svg
%{_datadir}/antler/style.css
%dir %{_datadir}/caribou
%{_datadir}/caribou/*
%{_datadir}/dbus-1/services/org.gnome.Caribou.Antler.service
%{_datadir}/glib-2.0/schemas/org.gnome.antler.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.caribou.gschema.xml
%{_libexecdir}/caribou
%{_datadir}/dbus-1/services/org.gnome.Caribou.Daemon.service

%files devel
%{_includedir}/libcaribou
%{_libdir}/libcaribou.so
%{_libdir}/pkgconfig/caribou-1.0.pc
%{_datadir}/gir-1.0/Caribou-1.0.gir
%{_datadir}/vala/vapi/caribou-1.0.deps
%{_datadir}/vala/vapi/caribou-1.0.vapi

%changelog
* Wed Jul 06 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.4.20-2
- Updated

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.4.19-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 0.4.19 

