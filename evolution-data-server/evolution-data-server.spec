Name:	    evolution-data-server	
Version:	3.16.3
Release:	1
Summary:	Evolution Data Server

Group:		Desktop/Gnome/Runtime/Libraries
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
Group:          Desktop/Gnome/Development/Libraries
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
make install DESTDIR=%{buildroot} DATADIRNAME=share

%find_lang evolution-data-server-3.16
rpmclean

%post
/sbin/ldconfig
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/sbin/ldconfig
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f evolution-data-server-3.16.lang
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
