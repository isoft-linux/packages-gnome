Name:           telepathy-farstream
Version:        0.6.2
Release:        2
Summary:        Telepathy client library to handle Call channels

License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Telepathy-Farsight
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  telepathy-glib-devel >= 0.19.0
BuildRequires:  farstream-devel >= 0.2.0
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  python-devel

## Obsolete telepathy-farsight(-python) with Fedora 17.
Provides:       telepathy-farsight = %{version}
Obsoletes:      telepathy-farsight < 0.0.20
Provides:       telepathy-farsight-python = %{version}
Obsoletes:      telepathy-farsight-python < 0.0.20
# Obsolete telepathy-farstream-python with Fedora 18 since gobject-introspection is
# provided now
Provides:       %{name}-python = %{version}
Obsoletes:      %{name}-python < 0.6.0


%description
%{name} is a Telepathy client library that uses Farstream to handle
Call channels.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       telepathy-glib-devel >= 0.19.0
Requires:       farstream-devel >= 0.2.0
Requires:       dbus-devel
Requires:       dbus-glib-devel
Requires:       pkgconfig

## Obsolete telepathy-farsight with Fedora 17
Provides:       telepathy-farsight-devel = %{version}
Obsoletes:      telepathy-farsight-devel < 0.0.20


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
%configure --enable-static=no
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%check
make check ||:

%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc NEWS README COPYING
%{_libdir}/libtelepathy-farstream*.so.*
%{_libdir}/girepository-1.0/TelepathyFarstream-0.6.typelib


%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libtelepathy-farstream.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/telepathy-1.0/%{name}/
%{_datadir}/gir-1.0/TelepathyFarstream-0.6.gir


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.6.2-2
- Rebuild for 4.0 release

