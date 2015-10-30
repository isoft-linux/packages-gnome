Name:	    libmediaart	
Version:    1.9.0 
Release:	2
Summary:    Library for managing media art caches	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

%description
Library tasked with managing, extracting and handling media art caches.

%package devel
Summary: Development files for %{name} 
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%check
#failed at chroot build for dbus-launch need an X11 env.
make check ||:

%files
%{_libdir}/libmediaart-*.so.*
%{_libdir}/girepository-1.0/MediaArt-*.typelib

%files devel
%{_libdir}/libmediaart-*.so
%dir %{_includedir}/libmediaart-*
%{_includedir}/libmediaart-*/*
%{_libdir}/pkgconfig/libmediaart-*.pc
%{_datadir}/gir-1.0/MediaArt-*.gir
%dir %{_datadir}/gtk-doc/html/libmediaart
%{_datadir}/gtk-doc/html/libmediaart/*
%{_datadir}/vala/vapi/libmediaart-*.vapi


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 1.9.0-2
- Rebuild for 4.0 release


