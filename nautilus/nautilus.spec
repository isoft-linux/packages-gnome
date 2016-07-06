Name: nautilus
Version: 3.18.1
Release: 3
Summary: Gnome File Manager

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz
BuildRequires: libexif-devel  >= 0.6.20
BuildRequires: libnotify-devel
BuildRequires: tracker-devel
BuildRequires: gtk3-devel atk-devel gnome-desktop3-devel

Requires: gvfs

%description
Gnome File Manager

%package devel
Summary:    Development libraries and headers for nautilus extension.
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files for %{name} extension.

%prep
%setup -q

%build

%configure \
    --disable-packagekit \
    --disable-update-mimedb \
    --disable-schemas-compile \
    --disable-xmp \
    --disable-tracker \
    --disable-selinux
     
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang nautilus

%clean
rm -rf $RPM_BUILD_ROOT


%post
glib-compile-schemas /usr/share/glib-2.0/schemas >/dev/null 2>&1 ||:
update-desktop-database ||:

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas >/dev/null 2>&1 ||:
update-desktop-database ||:

%files -f nautilus.lang
%{_sysconfdir}/xdg/autostart/nautilus-autostart.desktop
%{_bindir}/nautilus
%{_bindir}/nautilus-autorun-software
%{_libdir}/girepository-1.0/Nautilus-3.0.typelib
%{_libdir}/libnautilus-extension.so.*
%dir %{_libdir}/nautilus
%{_libdir}/nautilus/*
%{_libexecdir}/nautilus-convert-metadata
%{_datadir}/GConf/gsettings/nautilus.convert
%{_datadir}/appdata/*
%{_datadir}/applications/nautilus-autorun-software.desktop
%{_datadir}/applications/nautilus-classic.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.service
%{_datadir}/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
%{_datadir}/gnome-shell/search-providers/nautilus-search-provider.ini
%{_mandir}/man1/nautilus.1.gz


%files devel
%dir %{_includedir}/nautilus
%{_includedir}/nautilus/*
%{_libdir}/libnautilus-extension.so
%{_libdir}/pkgconfig/libnautilus-extension.pc
%{_datadir}/gir-1.0/Nautilus-3.0.gir
%dir %{_datadir}/gtk-doc/html/libnautilus-extension
%{_datadir}/gtk-doc/html/libnautilus-extension/*

%changelog
* Wed Jul 06 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.18.1-4
- disable selinux option

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1 

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

