Name:	    sushi	
Version:    3.18.0 
Release:	2
Summary:    A quick previewer for Nautilus	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

BuildRequires: libmusicbrainz5-devel
BuildRequires: webkitgtk4-devel 
BuildRequires: libevince-devel

%description
Sushi is a quick previewer for Nautilus, the GNOME desktop file manager.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang sushi


%post
#glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
#glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f sushi.lang
%{_bindir}/sushi
%{_libdir}/sushi/girepository-1.0/Sushi-1.0.typelib
%{_libdir}/sushi/libsushi-1.0.so
%{_libexecdir}/sushi-start
%{_datadir}/dbus-1/services/org.gnome.Sushi.service
#%{_datadir}/glib-2.0/schemas/org.gnome.sushi.gschema.xml
%{_datadir}/sushi/gir-1.0/Sushi-1.0.gir
%dir %{_datadir}/sushi
%{_datadir}/sushi/*

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

