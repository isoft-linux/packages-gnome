%define poppler_version 0.10.1
%define glib2_version 2.15.0
%define gtk3_version 2.9.4
%define dbus_version 0.60
%define theme_version 2.17.1

Name: evince
Version: 3.18.2
Release: 2
Summary: Document viewer

License: GPLv2+ and GFDL
URL: http://projects.gnome.org/evince/
Source0: http://download.gnome.org/sources/%{name}/2.26/%{name}-%{version}.tar.xz


BuildRequires:  pkgconfig(adwaita-icon-theme)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0) 
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  libtiff-devel
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  gtk-doc
BuildRequires:  yelp-tools
BuildRequires:  intltool
BuildRequires:  desktop-file-utils 

# For autoconf.sh
BuildRequires:  gnome-common >= 2.26
BuildRequires:  appstream-glib

# for the nautilus properties page
BuildRequires: pkgconfig(libnautilus-extension)
# for the djvu backend
BuildRequires: djvulibre-devel
# for the xps backend
BuildRequires:  pkgconfig(libgxps)

Requires:   libevince = %{version}-%{release}
Requires(pre): desktop-file-utils
Requires(pre): gtk3

%description
Evince is simple multi-page document viewer. It can display and print
Portable Document Format (PDF), PostScript (PS) and Encapsulated PostScript
(EPS) files. When supported by the document format, evince allows searching
for text, copying text to the clipboard, hypertext navigation,
table-of-contents bookmarks and editing of forms.

Support for other document formats such as DVI and DJVU can be added by
installing additional backends.

%package nautilus-extension 
Summary: Evince nautilus extension

%description nautilus-extension 
Evince nautilus extension

%package -n libevince
Summary: Evince runtime libraries

%description -n libevince 
Evince runtime libraries

%package -n libevince-devel
Summary: Evince development libraries
Requires: libevince = %{version}-%{release}

%description -n libevince-devel
Evince development libraries

%prep
%setup -q
%build
export CC=cc
export CXX=c++

%configure \
    --enable-compile-warnings=no \
    --disable-static \
    --disable-scrollkeeper \
    --with-print=gtk \
    --enable-comics=yes \
    --enable-djvu=yes \
    --enable-xps=yes \
    --enable-ps=yes \
    --enable-pdf=yes \
    --enable-nautilus \
    --enable-libgnome-desktop \
    --enable-introspection 

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang evince --with-gnome

unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# don't ship icon caches
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT


%post
update-desktop-database &> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database &> /dev/null ||:

touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%post -n libevince -p /sbin/ldconfig
%postun -n libevince -p /sbin/ldconfig

%files -f evince.lang
%defattr(-,root,root,-)
%doc README COPYING NEWS AUTHORS
%{_bindir}/*
%{_datadir}/evince/*
%{_mandir}/man1/*
%{_datadir}/thumbnailers/evince.thumbnailer
%{_datadir}/help/*/evince
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/GConf/gsettings/evince.convert
%{_datadir}/applications/evince-previewer.desktop
%{_datadir}/applications/evince.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Evince.gschema.xml
%{_libdir}/mozilla/plugins/libevbrowserplugin.so
%{_datadir}/appdata/*.xml

%files nautilus-extension
%{_libdir}/nautilus/extensions-3.0/libevince-properties-page.so

%files -n libevince
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%dir %{_libdir}/evince
%{_libdir}/evince/*
%{_libexecdir}/*
%{_datadir}/gir-*/*
%{_datadir}/dbus-1/services/org.gnome.evince.Daemon.service

%files -n libevince-devel
%defattr(-,root,root,-)
%{_includedir}/evince
%{_libdir}/*.so
%{_libdir}/pkgconfig/evince-*.pc
%{_datadir}/gtk-doc/html/*
%{_libdir}/girepository-1.0/*.typelib

%changelog
* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-7
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

