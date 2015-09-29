Name:		gnome-bluetooth
Version:	3.18.0
Release:	1
Summary:	Gnome bluetooth Utilities and Libraries

Group:	    Desktop/Gnome/Runtime/Libraries	
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

%description
The gnome-bluetooth package contains graphical utilities to setup,
monitor and use Bluetooth devices.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%build
%configure --disable-desktop-update --disable-icon-update
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} DATADIRNAME=share

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
* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

