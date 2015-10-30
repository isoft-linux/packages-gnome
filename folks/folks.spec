Name:	    folks	
Version:    0.11.1
Release:	2
Summary:	Folks is a library that aggregates people from multiple sources

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: telepathy-glib-devel
BuildRequires: evolution-data-server-devel

%description
Folks is a library that aggregates people from multiple sources

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q

%build
%configure --disable-fatal-warnings
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} 

%find_lang folks


%post
/sbin/ldconfig ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:
%postun
/sbin/ldconfig ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f folks.lang
%{_bindir}/folks-import
%{_bindir}/folks-inspect
%{_libdir}/libfolks.so.*
%{_libdir}/libfolks-eds.so.*
%{_libdir}/libfolks-telepathy.so.*
%{_libdir}/libfolks-dummy.so.*
%dir %{_libdir}/folks
%{_libdir}/folks/*
%{_libdir}/girepository-1.0/Folks-0.6.typelib
%{_libdir}/girepository-1.0/FolksEds-0.6.typelib
%{_libdir}/girepository-1.0/FolksTelepathy-0.6.typelib
%{_datadir}/GConf/gsettings/folks.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.folks.gschema.xml

%{_libdir}/girepository-1.0/FolksDummy-0.6.typelib

%files devel
%{_libdir}/libfolks-eds.so
%{_libdir}/libfolks-telepathy.so
%{_libdir}/libfolks-dummy.so
%{_libdir}/libfolks.so
%{_libdir}/pkgconfig/folks-eds.pc
%{_libdir}/pkgconfig/folks-telepathy.pc
%{_libdir}/pkgconfig/folks.pc
%{_libdir}/pkgconfig/folks-dummy.pc
%dir %{_includedir}/folks
%{_includedir}/folks/*
%{_datadir}/gir-1.0/Folks-0.6.gir
%{_datadir}/gir-1.0/FolksEds-0.6.gir
%{_datadir}/gir-1.0/FolksTelepathy-0.6.gir
%{_datadir}/vala/vapi/folks-eds.deps
%{_datadir}/vala/vapi/folks-eds.vapi
%{_datadir}/vala/vapi/folks-telepathy.deps
%{_datadir}/vala/vapi/folks-telepathy.vapi
%{_datadir}/vala/vapi/folks.deps
%{_datadir}/vala/vapi/folks.vapi
%{_datadir}/gir-1.0/FolksDummy-0.6.gir
%{_datadir}/vala/vapi/folks-dummy.deps
%{_datadir}/vala/vapi/folks-dummy.vapi

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.11.1-2
- Rebuild for 4.0 release

