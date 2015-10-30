Name:	    epiphany	
Version:    3.18.0
Release:	2
Summary:    Web browser for GNOME	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

BuildRequires: webkitgtk4-devel

%description
Epiphany is the web browser for the GNOME desktop. Its goal is to be
simple and easy to use. Epiphany ties together many GNOME components
in order to let you focus on the Web content, instead of the browser
application.

%prep
%setup -q

%build
%configure --enable-compile-warnings=no
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang epiphany

%post
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f epiphany.lang
%{_bindir}/*
%dir %{_libdir}/epiphany
%{_libdir}/epiphany/*
%{_libexecdir}/epiphany-search-provider
%{_datadir}/GConf/gsettings/epiphany.convert
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%dir %{_datadir}/epiphany
%{_datadir}/epiphany/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-shell/search-providers/epiphany-search-provider.ini
%{_datadir}/help/*/epiphany
%{_mandir}/man1/epiphany.1.gz


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

