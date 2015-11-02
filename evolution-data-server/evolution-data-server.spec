Name:	    evolution-data-server	
Version:	3.18.1
Release:	3
Summary:	Evolution Data Server

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

BuildRequires: libgdata-devel
BuildRequires: gnome-online-accounts-devel
BuildRequires: libgweather-devel

%description
Evolution Data Server

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

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
* Mon Nov 02 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-3
- Rebuild with icu 56.1

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

