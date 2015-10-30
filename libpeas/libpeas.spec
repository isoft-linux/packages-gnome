Name: libpeas
Version: 1.16.0
Release: 2
Summary: Plug-ins implementation convenience library	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz
BuildRequires: python-devel
BuildRequires: python3-devel

%description
libpeas is a convenience library making adding plug-ins support
to GTK+ and glib-based applications.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q

%build
%configure --disable-static --disable-seed
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 
%find_lang libpeas

%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :


%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk3-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans
gtk3-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :


%files -f libpeas.lang
%{_libdir}/girepository-1.0/Peas-1.0.typelib
%{_libdir}/girepository-1.0/PeasGtk-1.0.typelib
%dir %{_libdir}/libpeas-1.0
%dir %{_libdir}/libpeas-1.0/loaders
%{_libdir}/libpeas-1.0/loaders/libpythonloader.so
%{_libdir}/libpeas-1.0/loaders/libpython3loader.so
#%{_libdir}/libpeas-1.0/loaders/libseedloader.so
%{_libdir}/libpeas-1.0.so.*
%{_libdir}/libpeas-gtk-1.0.so.*
%{_datadir}/icons/hicolor/*/actions/libpeas-plugin.*

%files devel
%{_bindir}/peas-demo
%dir %{_includedir}/libpeas-1.0
%{_includedir}/libpeas-1.0/*
%{_libdir}/libpeas-1.0.so
%{_libdir}/libpeas-gtk-1.0.so
%dir %{_libdir}/peas-demo
%dir %{_libdir}/peas-demo/plugins
%{_libdir}/peas-demo/plugins/*
%{_libdir}/pkgconfig/libpeas-1.0.pc
%{_libdir}/pkgconfig/libpeas-gtk-1.0.pc
%{_datadir}/gir-1.0/Peas-1.0.gir
%{_datadir}/gir-1.0/PeasGtk-1.0.gir
%dir %{_datadir}/gtk-doc/html/libpeas
%{_datadir}/gtk-doc/html/libpeas/*

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 1.16.0-2
- Rebuild for 4.0 release

* Thu Sep 24 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

