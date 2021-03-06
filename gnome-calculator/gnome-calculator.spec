Name: gnome-calculator	
Version: 3.21.2
Release: 1
Summary: A desktop calculator	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtksourceview-3.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: mpfr-devel
BuildRequires: appstream-glib 
BuildRequires: pkgconfig(libsoup-2.4)

BuildRequires: vala

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
make install DESTDIR=%{buildroot}

%find_lang gnome-calculator

%post
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-calculator.lang
%{_bindir}/gcalccmd
%{_bindir}/gnome-calculator
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/gnome-calculator.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml

%{_libexecdir}/gnome-calculator-search-provider
%{_libdir}/gnome-calculator/libcalculator.so
%{_libdir}/gnome-calculator/libcalculator.a
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/gnome-calculator-search-provider.ini

%{_datadir}/help/*/gnome-calculator
%{_mandir}/man1/gcalccmd.1.gz
%{_mandir}/man1/gnome-calculator.1.gz

%changelog
* Sat Jul 09 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.21.2-1
- Update

* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

