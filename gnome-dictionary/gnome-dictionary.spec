Name: gnome-dictionary	
Version: 3.18.0
Release: 2
Summary:    Dictionary application for GNOME	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
%description
gnome-dictionary lets you look up words in dictionary sources.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 

%find_lang gnome-dictionary

%post
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-dictionary.lang
%{_bindir}/gnome-dictionary
%{_libdir}/libgdict-1.0.so.*
%{_datadir}/applications/*.desktop
%dir %{_datadir}/gdict-1.0
%{_datadir}/gdict-1.0/*
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
#%dir %{_datadir}/gnome-dictionary
#%{_datadir}/gnome-dictionary/*
%{_datadir}/help/*/gnome-dictionary
%{_datadir}/appdata/*.appdata.xml
%{_mandir}/man1/gnome-dictionary.1.gz
%{_libdir}/girepository-1.0/Gdict-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Dictionary.service


%files devel
%dir %{_includedir}/gdict-1.0
%{_includedir}/gdict-1.0/*
%{_libdir}/libgdict-1.0.so
%{_libdir}/pkgconfig/gdict-1.0.pc
%{_datadir}/gir-1.0/Gdict-1.0.gir
%{_datadir}/gtk-doc/html/gdict

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

