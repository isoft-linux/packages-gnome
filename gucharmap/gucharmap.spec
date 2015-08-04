Name:	    gucharmap	
Version:    3.16.2
Release:	1
Summary:    Unicode character picker and font browser	

Group:		Desktop/Gnome/Application
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

%description
This program allows you to browse through all the available Unicode
characters and categories for the installed fonts, and to examine their
detailed properties. It is an easy way to find the character you might
only know by its Unicode name or code point.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Group:   Desktop/Gnome/Development/Libraries
%description devel
%{summary}.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang gucharmap
rpmclean

%post
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f gucharmap.lang
%{_bindir}/charmap
%{_bindir}/gnome-character-map
%{_bindir}/gucharmap
%{_libdir}/girepository-1.0/Gucharmap-2.90.typelib
%{_libdir}/libgucharmap_2_90.so.7
%{_libdir}/libgucharmap_2_90.so.7.0.0
%{_datadir}/appdata/gucharmap.appdata.xml
%{_datadir}/applications/gucharmap.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Charmap.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Charmap.gschema.xml
%{_datadir}/help/*/gucharmap

%files devel
%dir %{_includedir}/gucharmap-2.90
%{_includedir}/gucharmap-2.90/*
%{_libdir}/libgucharmap_2_90.so
%{_libdir}/pkgconfig/gucharmap-2.90.pc
%{_datadir}/gir-1.0/Gucharmap-2.90.gir

%changelog
