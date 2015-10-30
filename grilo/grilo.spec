Name:		grilo
Version:	0.2.14
Release:	2
Summary:    Grilo is a framework for browsing and searching media content from various sources using a single API.	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

BuildRequires: totem-pl-parser-devel

%description
Grilo is a framework for browsing and searching media content from various sources using a single API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
export CC=cc
export CXX=c++
%configure \
    --enable-grl-net \
    --enable-vala \
    --enable-introspection \
    --enable-compile-warnings=no
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%find_lang grilo

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f grilo.lang
%{_bindir}/grl-launch-0.2
#%{_bindir}/grilo-simple-playlist
%{_bindir}/grilo-test-ui-0.2
%{_bindir}/grl-inspect-0.2
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libg*.so.*
%{_mandir}/man1/grilo-test-ui-0.2.1.gz
%{_mandir}/man1/grl-inspect-0.2.1.gz
%{_mandir}/man1/grl-launch-0.2.1.gz

%files devel
%dir %{_includedir}/grilo-0.2
%{_includedir}/grilo-0.2/*
%{_libdir}/libg*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/grilo-0.2.deps
%{_datadir}/vala/vapi/grilo-0.2.vapi
%{_datadir}/vala/vapi/grilo-net-0.2.deps
%{_datadir}/vala/vapi/grilo-net-0.2.vapi

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.2.14-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

