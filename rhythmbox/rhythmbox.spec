Name:		rhythmbox
Version:	3.3.1
Release: 	1	
Summary:    Gnome music player	

License:	GPL
URL:	    https://wiki.gnome.org/Apps/Rhythmbox/	
Source0:	%{name}-%{version}.tar.xz

BuildRequires:  gstreamer-devel
BuildRequires:  libtdb-devel
BuildRequires:  libgpod-devel
BuildRequires:  libmx-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  intltool
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  totem-devel
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  itstool
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(clutter-gst-2.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)


Requires:	gstreamer, libtdb

%description
Rhythmbox is your one-stop multimedia application, 
supporting a music library, multiple playlists, internet radio, and more.


%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
This package contains the development files to build rhythmbox plugin. 

%prep
%setup -q


%build
export CC=clang
export CXX=clang++

%configure \
    --disable-schemas-compile \
    --enable-libnotify \
    --enable-mmkeys \
    --disable-lirc \
    --enable-vala \
    --enable-python \
    --enable-fm-radio \
    --enable-browser-plugin \
    --disable-daap \
    --enable-visualizer \
    --with-gudev \
    --with-ipod \
    --with-mtp \
    --with-libsecret \
    --without-brasero \
    --without-webkit
    
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 
%find_lang rhythmbox


%post
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f rhythmbox.lang
%{_bindir}/rhythmbox
%{_bindir}/rhythmbox-client
%{_libdir}/girepository-1.0/MPID-3.0.typelib
%{_libdir}/girepository-1.0/RB-3.0.typelib
%{_libdir}/*.so.*
%{_libdir}/mozilla/plugins/librhythmbox-itms-detection-plugin.so
%{_libdir}/rhythmbox
%{_libexecdir}/rhythmbox-metadata
%{_datadir}/applications/rhythmbox-device.desktop
%{_datadir}/applications/rhythmbox.desktop
%{_datadir}/dbus-1/services/org.gnome.Rhythmbox3.service
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.gschema.xml
%{_datadir}/help/*/rhythmbox
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/rhythmbox
%{_mandir}/man1/rhythmbox-client.1.gz
%{_mandir}/man1/rhythmbox.1.gz

%{_datadir}/appdata/rhythmbox.appdata.xml
%files devel
%{_includedir}/rhythmbox
%{_libdir}/*.so
%{_libdir}/pkgconfig/rhythmbox.pc
%{_datadir}/gir-1.0/MPID-3.0.gir
%{_datadir}/gir-1.0/RB-3.0.gir
%{_datadir}/gtk-doc/html/rhythmbox


%changelog
* Tue Jul 12 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.3.1-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.2-3
- Rebuild for 4.0 release

