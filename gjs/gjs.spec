Name: gjs	
Version: 1.43.3
Release: 2
Summary: JavaScript bindings based on gobject-introspection	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

BuildRequires:	mozjs24-devel
Requires:	mozjs24

%description
JavaScript bindings based on gobject-introspection

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/gjs
%{_bindir}/gjs-console
%{_libdir}/libgjs.so.*
%{_libexecdir}/gjs/installed-tests/js
%{_libdir}/gjs/girepository-1.0/GjsPrivate-1.0.typelib

%files devel
%{_includedir}/gjs-1.0
%{_libdir}/libgjs.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 1.43.3-2
- Rebuild for 4.0 release


