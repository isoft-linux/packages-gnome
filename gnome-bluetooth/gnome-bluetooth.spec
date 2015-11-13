Name: gnome-bluetooth
Version: 3.18.1
Release: 2
Summary: Gnome bluetooth Utilities and Libraries

License: GPL
URL: http://www.gnome.org
Source0: http://download.gnome.org/sources/gnome-bluetooth/3.18/gnome-bluetooth-%{version}.tar.xz
Source1: 61-gnome-bluetooth-rfkill.rules

BuildRequires:	gtk3-devel >= 3.0
BuildRequires:	dbus-glib-devel

BuildRequires:	intltool desktop-file-utils gettext gtk-doc
BuildRequires:	itstool
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	systemd-devel

BuildRequires:	gobject-introspection-devel

%description
The gnome-bluetooth package contains graphical utilities to setup,
monitor and use Bluetooth devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:	gobject-introspection-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%build
%configure --disable-desktop-update --disable-icon-update --disable-schemas-compile --disable-compile-warnings
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 

install -m0644 -D %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/udev/rules.d/61-gnome-bluetooth-rfkill.rules

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%find_lang gnome-bluetooth2
%post
/sbin/ldconfig
gtk3-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database -q ||: 
%postun 
/sbin/ldconfig
gtk3-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database -q ||: 

%files -f gnome-bluetooth2.lang
%{_bindir}/bluetooth-sendto
%{_libdir}/girepository-1.0/GnomeBluetooth-1.0.typelib
%{_libdir}/libgnome-bluetooth.so.*
%{_datadir}/applications/bluetooth-sendto.desktop
%dir %{_datadir}/gnome-bluetooth
%{_datadir}/gnome-bluetooth/pin-code-database.xml
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/udev/rules.d/61-gnome-bluetooth-rfkill.rules
%{_mandir}/man1/bluetooth-sendto.1.gz


%files devel
%dir %{_includedir}/gnome-bluetooth
%{_includedir}/gnome-bluetooth/*
%{_libdir}/libgnome-bluetooth.so
%{_libdir}/pkgconfig/gnome-bluetooth*.pc
%{_datadir}/gir-1.0/GnomeBluetooth-1.0.gir
%dir %{_datadir}/gtk-doc/html/gnome-bluetooth
%{_datadir}/gtk-doc/html/gnome-bluetooth/*

%changelog
* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

