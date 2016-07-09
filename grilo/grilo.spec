Name:		grilo
Version:	0.3.1
Release:	1
Summary:    Grilo is a framework for browsing and searching media content from various sources using a single API.	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

BuildRequires: totem-pl-parser-devel
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: vala-devel
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: intltool

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
#make %{?_smp_mflags}
make

%install
make install DESTDIR=%{buildroot} 
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%find_lang grilo

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f grilo.lang
%{_bindir}/grl-inspect-0.3
%{_bindir}/grl-launch-0.3
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libg*.so.*
%{_mandir}/man1/grl-inspect-0.3.1.gz
%{_mandir}/man1/grl-launch-0.3.1.gz

%files devel
%{_libdir}/libg*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_includedir}/grilo-0.3/grilo.h
%{_includedir}/grilo-0.3/grl-caps.h
%{_includedir}/grilo-0.3/grl-config.h
%{_includedir}/grilo-0.3/grl-data.h
%{_includedir}/grilo-0.3/grl-definitions.h
%{_includedir}/grilo-0.3/grl-error.h
%{_includedir}/grilo-0.3/grl-log.h
%{_includedir}/grilo-0.3/grl-media.h
%{_includedir}/grilo-0.3/grl-metadata-key.h
%{_includedir}/grilo-0.3/grl-multiple.h
%{_includedir}/grilo-0.3/grl-operation-options.h
%{_includedir}/grilo-0.3/grl-operation.h
%{_includedir}/grilo-0.3/grl-plugin.h
%{_includedir}/grilo-0.3/grl-range-value.h
%{_includedir}/grilo-0.3/grl-registry.h
%{_includedir}/grilo-0.3/grl-related-keys.h
%{_includedir}/grilo-0.3/grl-source.h
%{_includedir}/grilo-0.3/grl-util.h
%{_includedir}/grilo-0.3/grl-value-helper.h
%{_includedir}/grilo-0.3/net/grl-net-wc.h
%{_includedir}/grilo-0.3/net/grl-net.h
%{_includedir}/grilo-0.3/pls/grl-pls.h
%{_datadir}/vala/vapi/grilo-0.3.deps
%{_datadir}/vala/vapi/grilo-0.3.vapi
%{_datadir}/vala/vapi/grilo-net-0.3.deps
%{_datadir}/vala/vapi/grilo-net-0.3.vapi

%changelog
* Sat Jul 09 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.3.1-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.2.14-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

