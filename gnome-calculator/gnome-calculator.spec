Name:	    gnome-calculator	
Version:    3.16.0
Release:	1
Summary:    A desktop calculator	

Group:		Desktop/Gnome/Application
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: gtksourceview-devel
%description
gnome-calculator is a powerful graphical calculator with financial,
logical and scientific modes. It uses a multiple precision package
to do its arithmetic to give a high degree of accuracy.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} DATADIRNAME=share

%find_lang gnome-calculator
rpmclean

%post
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-calculator.lang
%{_bindir}/gcalccmd
%{_bindir}/gnome-calculator
%{_datadir}/appdata/gnome-calculator.appdata.xml
%{_datadir}/applications/gnome-calculator.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_libexecdir}/gnome-calculator-search-provider
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/gnome-calculator-search-provider.ini

%{_datadir}/help/*/gnome-calculator
%{_mandir}/man1/gcalccmd.1.gz
%{_mandir}/man1/gnome-calculator.1.gz

%changelog
