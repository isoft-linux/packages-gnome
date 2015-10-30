Name:		gnome-online-accounts
Version:	3.18.1
Release:	2
Summary:	Gnome online accounts library

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
Patch0:     gnome-online-accounts-remove-webkit.patch

BuildRequires: telepathy-glib-devel	
BuildRequires: libaccounts-glib-devel
BuildRequires:  json-glib-devel
BuildRequires:  libsecret-devel >= 0.7
BuildRequires:  libsoup-devel >= 2.41
BuildRequires:  rest-devel

#Requires:	

%description
Gnome online accounts library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
#autoreconf -ivf 
%configure \
  --disable-static \
  --enable-exchange \
  --enable-imap-smtp \
  --enable-kerberos \
  --enable-telepathy \
  --enable-compile-warnings=no 

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

%find_lang gnome-online-accounts
%find_lang gnome-online-accounts-tpaw
cat  gnome-online-accounts-tpaw.lang >>gnome-online-accounts.lang

%post
/sbin/ldconfig
gtk3-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun 
/sbin/ldconfig
gtk3-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f gnome-online-accounts.lang
%{_libdir}/girepository-1.0/Goa-1.0.typelib
%{_libdir}/*.so.*
%{_libexecdir}/goa-daemon
%{_libexecdir}/goa-identity-service
%{_datadir}/dbus-1/services/org.gnome.OnlineAccounts.service
%{_datadir}/dbus-1/services/org.gnome.Identity.service
%dir %{_datadir}/gnome-online-accounts
%{_datadir}/gnome-online-accounts/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/glib-2.0/schemas/org.gnome.online-accounts.gschema.xml
%{_mandir}/man8/goa-daemon.8.gz

%files devel
%dir %{_includedir}/goa-1.0
%{_includedir}/goa-1.0/*
%dir %{_libdir}/goa-1.0
%{_libdir}/goa-1.0/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/goa-1.0.pc
%{_libdir}/pkgconfig/goa-backend-1.0.pc
%{_datadir}/gir-1.0/Goa-1.0.gir

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Thu Sep 24 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

