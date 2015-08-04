Name:	    mousetweaks	
Version:    3.12.0
Release:	1
Summary:    Mouse accessibility support for the GNOME desktop	

Group:	    Desktop/Gnome/Application	
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

%description
The Mousetweaks package provides mouse accessibility enhancements for the GNOME desktop, such as performing various clicks without using any hardware button. The options can be accessed through the Accessibility tab of the Mouse Preferences of GNOME Control Center or through command-line.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang mousetweaks

rpmclean

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f mousetweaks.lang
%{_bindir}/mousetweaks
%{_datadir}/GConf/gsettings/mousetweaks.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mousetweaks.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mousetweaks.gschema.xml
%{_mandir}/man1/mousetweaks.1.gz
%dir %{_datadir}/mousetweaks
%{_datadir}/mousetweaks/*


%changelog

