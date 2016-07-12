Name:	    libgdata	
Version:	0.17.5
Release:	1
Summary:	libgdata is a GLib-based library for accessing online service APIs

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: libxml2-devel
BuildRequires: libsoup-devel 
BuildRequires: liboauth-devel
BuildRequires: json-glib-devel
BuildRequires: gcr-devel
BuildRequires: uhttpmock-devel
BuildRequires: gnome-online-accounts-devel 
%description
libgdata is a GLib-based library for accessing online service APIs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%prep
%setup -q

%build
%configure --enable-gnome --enable-compile-warnings=no
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}  

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%find_lang gdata

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gdata.lang
%{_libdir}/girepository-1.0/GData-0.0.typelib
%{_libdir}/libgdata.so.*


%files devel
%dir %{_includedir}/libgdata
%{_includedir}/libgdata/*
%{_libdir}/libgdata.so
%{_libdir}/pkgconfig/libgdata.pc
%{_datadir}/gir-1.0/GData-0.0.gir
%dir %{_datadir}/gtk-doc/html/gdata
%{_datadir}/gtk-doc/html/gdata/*
%{_datadir}/vala/vapi/libgdata.deps
%{_datadir}/vala/vapi/libgdata.vapi

%changelog
* Tue Jul 12 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.17.5-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.17.3-2
- Rebuild for 4.0 release

* Thu Sep 24 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

