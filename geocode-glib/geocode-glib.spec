%global json_glib_version 0.16.2

Name:           geocode-glib
Version:        3.20.1
Release:        1
Summary:        Geocoding helper library

License:        LGPLv2+
URL:            http://www.gnome.org/
Source0:        http://download.gnome.org/sources/geocode-glib/3.12/geocode-glib-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  json-glib-devel >= %{json_glib_version}
BuildRequires:  libsoup-devel

Requires:       json-glib%{?_isa} >= %{json_glib_version}

%description
geocode-glib is a convenience library for the geocoding (finding longitude,
and latitude from an address) and reverse geocoding (finding an address from
coordinates). It uses Nominatim service to achieve that. It also caches
(reverse-)geocoding requests for faster results and to avoid unnecessary server
load.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING.LIB NEWS README
%{_libdir}/libgeocode-glib.so.*
%{_libdir}/girepository-1.0/GeocodeGlib-1.0.typelib
%{_datadir}/icons/gnome/scalable/places/*.svg

%files devel
%{_includedir}/geocode-glib-1.0/
%{_libdir}/libgeocode-glib.so
%{_libdir}/pkgconfig/geocode-glib-1.0.pc
%{_datadir}/gir-1.0/GeocodeGlib-1.0.gir
%{_datadir}/gtk-doc/html/geocode-glib-*


%changelog
* Sat Jul 09 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.1-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

