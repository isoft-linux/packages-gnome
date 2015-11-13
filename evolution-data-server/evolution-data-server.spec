%define glib2_version 2.40.0
%define gtk3_version 3.6.0
%define gcr_version 3.4
%define gtk_doc_version 1.9
%define goa_version 3.8
%define intltool_version 0.35.5
%define libsecret_version 0.5
%define libgdata_version 0.10.0
%define libgweather_version 3.5.0
%define libical_version 0.46
%define libsoup_version 2.42
%define sqlite_version 3.5
%define webkitgtk_version 2.4.9
%define json_glib_version 1.0.4

Name: evolution-data-server	
Version: 3.18.2
Release: 2
Summary: Backend data server for Evolution 

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

Requires: dconf

### Build Dependencies ###

BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: gperf
BuildRequires: gtk-doc >= %{gtk_doc_version}
BuildRequires: intltool >= %{intltool_version}
BuildRequires: libdb-devel
BuildRequires: libtool
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: systemd

BuildRequires: pkgconfig(gcr-3)  >= %{gcr_version}
BuildRequires: pkgconfig(gcr-base-3)  >= %{gcr_version}
BuildRequires: pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gmodule-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(goa-1.0) >= %{goa_version}
BuildRequires: pkgconfig(libgdata) >= %{libgdata_version}
BuildRequires: pkgconfig(gweather-3.0) >= %{libgweather_version}
BuildRequires: pkgconfig(libical) >= %{libical_version}
BuildRequires: pkgconfig(libsecret-unstable) >= %{libsecret_version}
BuildRequires: pkgconfig(libsoup-2.4) >= %{libsoup_version}
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(nspr)
BuildRequires: pkgconfig(nss) >= %{nss_version}
BuildRequires: pkgconfig(sqlite3) >= %{sqlite_version}
BuildRequires: pkgconfig(webkitgtk-3.0) >= %{webkitgtk_version}
BuildRequires: pkgconfig(json-glib-1.0) >= %{json_glib_version}

BuildRequires: openldap-devel
BuildRequires: pkgconfig(openssl)

%description
The %{name} package provides a unified backend for programs that work
with contacts, tasks, and calendar information.

It was originally developed for Evolution (hence the name), but is now used
by other packages.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(goa-1.0) >= %{goa_version}
Requires: pkgconfig(libgdata) >= %{libgdata_version}
Requires: pkgconfig(gweather-3.0) >= %{libgweather_version}
Requires: pkgconfig(libical) >= %{libical_version}
Requires: pkgconfig(libsecret-unstable) >= %{libsecret_version}
Requires: pkgconfig(libsoup-2.4) >= %{libsoup_version}
Requires: pkgconfig(sqlite3) >= %{sqlite_version}
Requires: pkgconfig(webkitgtk-3.0) >= %{webkitgtk_version}
Requires: pkgconfig(json-glib-1.0) >= %{json_glib_version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q 

%build
%configure \
    --disable-uoa \
    --disable-static \
    --enable-vala-bindings \
    --enable-compile-warnings=no 

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang evolution-data-server-3.18

%post
/sbin/ldconfig
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/sbin/ldconfig
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f evolution-data-server-3.18.lang
%dir %{_libdir}/evolution-data-server
%{_libdir}/evolution-data-server/*
%{_libdir}/girepository-1.0/EBook-1.2.typelib
%{_libdir}/girepository-1.0/EBookContacts-1.2.typelib
%{_libdir}/girepository-1.0/EDataServer-1.2.typelib
%{_libdir}/*.so.*
%{_libexecdir}/*
%{_datadir}/GConf/gsettings/evolution-data-server.convert
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.AddressBook.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Calendar.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.Sources.service
%{_datadir}/dbus-1/services/org.gnome.evolution.dataserver.UserPrompter.service
%{_datadir}/glib-2.0/schemas/*.xml
%dir %{_datadir}/pixmaps/evolution-data-server
%{_datadir}/pixmaps/evolution-data-server/*

%files devel
%dir %{_includedir}/evolution-data-server
%{_includedir}/evolution-data-server/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/EBook-1.2.gir
%{_datadir}/gir-1.0/EBookContacts-1.2.gir
%{_datadir}/gir-1.0/EDataServer-1.2.gir
#%{_datadir}/gtk-doc/html/*
%{_datadir}/vala/vapi/*

%changelog
* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Mon Nov 02 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-3
- Rebuild with icu 56.1

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

