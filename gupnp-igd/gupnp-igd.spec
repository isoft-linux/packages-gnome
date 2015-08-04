Name:	    gupnp-igd	
Version:    0.2.4
Release:	1
Summary:    Library to handle UPnP IGD port mapping	

Group:		Desktop/Gnome/Runtime/Libraries
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: gupnp-devel

%description
gupnp-igd is a library to handle UPnP IGD port mapping.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Group:   Desktop/Gnome/Development/Libraries
%description devel
%{summary}.



%prep
%setup -q

%build
%configure --disable-static

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rpmclean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/girepository-1.0/GUPnPIgd-1.0.typelib
%{_libdir}/libgupnp-igd-1.0.so.*

%files devel
%{_includedir}/gupnp-igd-1.0
%{_libdir}/libgupnp-igd-1.0.so
%{_libdir}/pkgconfig/gupnp-igd-1.0.pc
%{_datadir}/gir-1.0/GUPnPIgd-1.0.gir
%{_datadir}/gtk-doc/html/gupnp-igd


%changelog

