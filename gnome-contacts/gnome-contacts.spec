Name: gnome-contacts	
Version: 3.18.0
Release: 2
Summary:    Contacts manager for GNOME	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: folks-devel
BuildRequires: cheese-libs-devel

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

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

