%global	dbus_ver	0.95
%global	dbus_glib_ver	0.90
%global	glib_ver	2.36.0
%global gobj_ver	1.30
%global vala_ver	0.16.0

Name:           telepathy-glib
Version:        0.24.1
Release:        2
Summary:        GLib bindings for Telepathy

License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gtk-doc >= 1.17
BuildRequires:  dbus-devel >= %{dbus_ver}
BuildRequires:	dbus-glib-devel >= %{dbus_glib_ver}
BuildRequires:	glib2-devel >= %{glib_ver}
BuildRequires:	gobject-introspection-devel >= %{gobj_ver}
BuildRequires:	vala-devel >= %{vala_ver}
BuildRequires:	vala-tools
BuildRequires:	libxslt
BuildRequires:	python

%description
Telepathy-glib is the glib bindings for the telepathy unified framework
for all forms of real time conversations, including instant messaging, IRC, 
voice calls and video calls.


%package vala
Summary:	Vala bindings for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	vala


%description vala
Vala bindings for %{name}.


%package 	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-vala = %{version}-%{release}
Requires:	dbus-devel >= %{dbus_ver}
Requires:	dbus-glib-devel >= %{dbus_glib_ver}
Requires:	glib2-devel >= %{glib_ver}
Requires:	pkgconfig


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q 


%build
%configure --enable-static=no --enable-introspection=yes --enable-vala-bindings=yes --enable-compile-warnings=no
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%check
make check ||:


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README NEWS
%{_libdir}/libtelepathy-glib*.so.*
%{_libdir}/girepository-1.0/TelepathyGLib-0.12.typelib


%files vala
%{_datadir}/vala/vapi/telepathy-glib.deps
%{_datadir}/vala/vapi/telepathy-glib.vapi


%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libtelepathy-glib.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/telepathy-1.0/%{name}/
%{_datadir}/gir-1.0/TelepathyGLib-0.12.gir


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.24.1-2
- Rebuild for 4.0 release

