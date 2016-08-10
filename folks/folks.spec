Name:	    folks	
Version:    0.11.2
Release:	3
Summary:	Folks is a library that aggregates people from multiple sources

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: telepathy-glib-devel
BuildRequires: evolution-data-server-devel
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: vala-tools
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: intltool

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
%configure --disable-fatal-warnings --enable-vapigen
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
* Wed Aug 10 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.11.2-3
- Update

* Fri Jul 08 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.11.2-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.11.1-2
- Rebuild for 4.0 release

