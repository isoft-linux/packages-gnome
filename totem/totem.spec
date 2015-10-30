Name: totem 
Version: 3.18.1
Release: 2
Summary: Movie player for GNOME 

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz
Requires: grilo-plugins
Requires: iso-codes
Requires: gstreamer-plugins-base
Requires: gstreamer-plugins-good
Requires: gstreamer-plugins-bad
Requires: gstreamer-plugins-ugly

BuildRequires: totem-pl-parser-devel
BuildRequires: gstreamer-devel 
BuildRequires: clutter-devel 
BuildRequires: clutter-gst3
BuildRequires: nautilus-devel
BuildRequires: grilo-devel libpeas-devel

%description
Totem package contains the official movie player of the GNOME Desktop based on GStreamer. It features a playlist, a full-screen mode, seek and volume controls, as well as keyboard navigation. This is useful for playing any GStreamer supported file, DVD, VCD or digital CD.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q


%build
%configure --disable-static --enable-compile-warnings=no --enable-cxx-warnings=no
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang totem


%post
/sbin/ldconfig ||:
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
 /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
/sbin/ldconfig
update-desktop-database -q> /dev/null ||:

touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
 /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f totem.lang
%{_bindir}/totem
%{_bindir}/totem-audio-preview
%{_bindir}/totem-video-thumbnailer
%{_libdir}/girepository-1.0/Totem-1.0.typelib
%{_libdir}/libtotem.so.*
%{_libdir}/nautilus/extensions-3.0/libtotem-properties-page.so
%dir %{_libdir}/totem/plugins
%{_libdir}/totem/plugins/*
%{_datadir}/GConf/gsettings/opensubtitles.convert
%{_datadir}/GConf/gsettings/pythonconsole.convert
%{_datadir}/GConf/gsettings/totem.convert
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.totem.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.totem.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.totem.plugins.opensubtitles.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.totem.plugins.pythonconsole.gschema.xml
%{_datadir}/help/*/totem
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/thumbnailers/totem.thumbnailer
%{_datadir}/dbus-1/services/org.gnome.Totem.service
%dir %{_datadir}/totem
%{_datadir}/totem/*
%{_mandir}/man1/totem-video-thumbnailer.1.gz
%{_mandir}/man1/totem.1.gz


%files devel
%{_includedir}/totem
%{_libdir}/libtotem.so
%{_libdir}/pkgconfig/totem.pc
%{_datadir}/gir-1.0/Totem-1.0.gir
%{_datadir}/gtk-doc/html/totem

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1 

