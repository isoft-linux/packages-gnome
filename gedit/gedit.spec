%define _python_bytecompile_errors_terminate_build 0

Name: gedit 
Version: 3.18.1
Release: 3
Summary: Text editor for the GNOME desktop

License: GPL
URL: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/gedit/3.18/%{name}-%{version}.tar.xz

BuildRequires: gnome-common
BuildRequires: pkgconfig(enchant)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtksourceview-3.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(libpeas-gtk-1.0)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: which
BuildRequires: autoconf, automake, libtool
BuildRequires: intltool
BuildRequires: yelp-tools
BuildRequires: itstool
BuildRequires: vala-tools
BuildRequires: python3-devel
BuildRequires: python3-gobject
BuildRequires: /usr/bin/appstream-util

%description
gedit is a small, but powerful text editor designed specifically for
the GNOME desktop. It has most standard text editor functions and fully
supports international text in Unicode. Advanced features include syntax
highlighting and automatic indentation of source code, printing and editing
of multiple documents in one window.

gedit is extensible through a plugin system, which currently includes
support for spell checking, comparing files, viewing CVS ChangeLogs, and
adjusting indentation levels. Further plugins can be found in the
gedit-plugins package.



%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q

%build
export CC=cc
export CXX=c++
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} 

%find_lang gedit 

%post
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f gedit.lang
%{_bindir}/gedit
%{_bindir}/gnome-text-editor
%dir %{_libdir}/gedit
%{_libdir}/gedit/*
%dir %{_libexecdir}/gedit
%{_libexecdir}/gedit/gedit-bugreport.sh
%{_datadir}/GConf/gsettings/gedit.convert
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.gedit.service
%dir %{_datadir}/gedit
%dir %{_datadir}/gedit/logo
%{_datadir}/gedit/logo/*
%dir %{_datadir}/gedit/plugins
%{_datadir}/gedit/plugins/*
%{_datadir}/glib-2.0/schemas/*.xml
%{python3_sitearch}/gi/overrides/*
%{_datadir}/help/*/gedit
%{_mandir}/man1/gedit.1.gz

%files devel
%{_includedir}/gedit-*
%{_libdir}/pkgconfig/gedit.pc
%{_datadir}/gedit/gir-1.0/Gedit-3.0.gir
%{_datadir}/vala/vapi/gedit.deps
%{_datadir}/vala/vapi/gedit.vapi
%{_datadir}/gtk-doc/html/gedit

%changelog
* Fri Nov 06 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-3
- Update to 3.18.1

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

