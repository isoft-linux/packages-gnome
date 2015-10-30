Name: libchamplain	
Version: 0.12.11
Release: 2
Summary: Map view for Clutter

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz
BuildRequires: clutter-gtk-devel

%description
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q

%build
%configure --disable-static --enable-compile-warnings=no 
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/girepository-1.0/Champlain-0.12.typelib
%{_libdir}/girepository-1.0/GtkChamplain-0.12.typelib
%{_libdir}/libchamplain-0.12.so.*
%{_libdir}/libchamplain-gtk-0.12.so.*

%files devel
%{_includedir}/libchamplain-0.12
%{_includedir}/libchamplain-gtk-0.12
%{_libdir}/libchamplain-0.12.so
%{_libdir}/libchamplain-gtk-0.12.so
%{_libdir}/pkgconfig/champlain-0.12.pc
%{_libdir}/pkgconfig/champlain-gtk-0.12.pc
%{_datadir}/gir-1.0/Champlain-0.12.gir
%{_datadir}/gir-1.0/GtkChamplain-0.12.gir
%{_datadir}/gtk-doc/html/libchamplain-0.12
%{_datadir}/gtk-doc/html/libchamplain-gtk-0.12
%{_datadir}/vala/vapi/champlain-0.12.vapi
%{_datadir}/vala/vapi/champlain-gtk-0.12.vapi


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.12.11-2
- Rebuild for 4.0 release

* Thu Sep 24 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

