Name:           libgweather
Version:        3.16.1
Release:        1
Summary:        A library for weather information

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.gnome.org
#VCS: git:git://git.gnome.org/libgweather
Source0:        http://download.gnome.org/sources/libgweather/3.13/%{name}-%{version}.tar.xz

BuildRequires:  dbus-devel
BuildRequires:  geocode-glib-devel
BuildRequires:  gtk3-devel >= 2.90.0
BuildRequires:  gtk-doc
BuildRequires:  libsoup-devel >= 2.4
BuildRequires:  libxml2-devel >= 2.6
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  autoconf automake libtool
BuildRequires:  gobject-introspection-devel >= 0.10
BuildRequires:  gnome-common
BuildRequires:  vala-devel
BuildRequires:  vala-tools

Requires: adwaita-icon-theme

%description
libgweather is a library to access weather information from online
services for numerous locations.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure --disable-static --disable-gtk-doc
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT DATADIRNAME=share
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name} --all-name

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f %{name}.lang
%doc COPYING
%{_libdir}/libgweather-3.so.*
%{_libdir}/girepository-1.0/GWeather-3.0.typelib
%dir %{_datadir}/libgweather
%{_datadir}/libgweather/Locations.xml
%{_datadir}/libgweather/locations.dtd
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather.gschema.xml

%files devel
%{_includedir}/libgweather-3.0
%{_libdir}/libgweather-3.so
%{_libdir}/pkgconfig/gweather-3.0.pc
%{_datadir}/gir-1.0/GWeather-3.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libgweather-3.0
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/gweather-3.0.vapi


%changelog
