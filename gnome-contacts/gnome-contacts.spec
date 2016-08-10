Name: gnome-contacts	
Version: 3.20.0
Release: 3
Summary: Contacts manager for GNOME	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz
BuildRequires: folks-devel
BuildRequires: cheese-libs-devel

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  intltool
BuildRequires:  vala-tools
BuildRequires:  vala-devel
BuildRequires:  appstream-glib
BuildRequires:  libxslt 
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(cheese-gtk)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(folks-eds)
BuildRequires:  pkgconfig(folks-telepathy)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0) 
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires:       geocode-glib
Requires:       gtk3

%description
gnome-contacts is a standalone contacts manager for GNOME desktop.

%prep
%setup -q

%build
export CC=cc
export CXX=c++

%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 

%find_lang gnome-contacts


%post
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f gnome-contacts.lang
%{_bindir}/gnome-contacts
%{_libexecdir}/gnome-contacts-search-provider
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.Contacts.service
%{_datadir}/gnome-shell/search-providers/org.gnome.Contacts.search-provider.ini
%{_mandir}/man1/gnome-contacts.1.gz

%changelog
* Wed Aug 10 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.0-3
- Update

* Sun Jul 10 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.0-1
- Update

* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

