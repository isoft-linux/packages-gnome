%global glib2_version 2.31.0
%global libsoup_version 2.37.91
%global uhm_api_version 0.0

Name:           uhttpmock
Version:        0.5.0
Release:        2
Summary:        HTTP web service mocking library
License:        LGPLv2
URL:            http://gitorious.org/uhttpmock/
Source0:        http://tecnocode.co.uk/downloads/%{name}-%{version}.tar.xz

BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  libsoup-devel >= %{libsoup_version}
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  vala-tools
BuildRequires:  vala-devel
BuildRequires:  gnome-common

Requires:       glib2 >= %{glib2_version}
Requires:       libsoup >= %{libsoup_version}

%description
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS.
It provides a library, libuhttpmock, which implements recording and
playback of HTTP request–response traces.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries, header files and documentation for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure \
    --enable-gtk-doc \
    --enable-introspection \
    --enable-vala=yes \
    --disable-static
make %{?_smp_mflags}

%check
#make check

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libuhttpmock-%{uhm_api_version}.so.*
%{_libdir}/girepository-1.0/Uhm-%{uhm_api_version}.typelib

%files devel
%{_libdir}/libuhttpmock-%{uhm_api_version}.so
%{_includedir}/libuhttpmock-%{uhm_api_version}/
%{_libdir}/pkgconfig/libuhttpmock-%{uhm_api_version}.pc
%{_datadir}/gir-1.0/Uhm-%{uhm_api_version}.gir
%{_datadir}/vala/vapi/libuhttpmock-%{uhm_api_version}.deps
%{_datadir}/vala/vapi/libuhttpmock-%{uhm_api_version}.vapi
%{_datadir}/gtk-doc/html/libuhttpmock*

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.5.0-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to 0.5.0 

