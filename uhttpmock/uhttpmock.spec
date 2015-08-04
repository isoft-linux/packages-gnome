%global git_snapshot 1
%global gitid f70ec6b79d5fa6eabea9b5bf53716ebf8aa17c90

%global glib2_version 2.31.0
%global libsoup_version 2.37.91
%global uhm_api_version 0.0

Name:           uhttpmock
Version:        0.3.0
Release:        1
Summary:        HTTP web service mocking library
License:        LGPLv2
URL:            http://gitorious.org/uhttpmock/
%if %git_snapshot
Source0:        uhttpmock-uhttpmock-%{gitid}.tar.gz
%else
Source0:        http://tecnocode.co.uk/downloads/%{name}-%{version}.tar.xz
%endif

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
%if %git_snapshot
%setup -q -n uhttpmock-uhttpmock
./autogen.sh
%else
%setup -q
%endif

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

rpmclean
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
