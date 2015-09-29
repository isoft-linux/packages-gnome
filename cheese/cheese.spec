Name:           cheese
Epoch:          2
Version:        3.18.0
Release:        1%{?dist}
Summary:        Application for taking pictures and movies from a webcam

Group:          Amusements/Graphics
License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Cheese
#VCS: git:git://git.gnome.org/cheese
Source0:        https://download.gnome.org/sources/%{name}/3.18/%{name}-%{version}.tar.xz
# Upstream fix for desktop file validation.
Patch0:         cheese-3.18.0-fix-desktop-translation.patch

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libXtst-devel
BuildRequires:  vala-devel
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: gstreamer-plugins-good
Requires: gstreamer-plugins-bad
Requires: gnome-video-effects

%description
Cheese is a Photobooth-inspired GNOME application for taking pictures and
videos from a webcam. It can also apply fancy graphical effects.

%package camera-service
Summary:        Webcam D-Bus service
Group:          System Environment/Libraries
License:        GPLv3+
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description camera-service
This package contains a D-Bus service needed for applications that
want to display a webcam dialog in their interface.

%package libs
Summary:        Webcam display and capture widgets
Group:          System Environment/Libraries
License:        GPLv2+

%description libs
This package contains libraries needed for applications that
want to display a webcam in their interface.

%package libs-devel
Summary:        Development files for %{name}-libs
Group:          Development/Libraries
License:        GPLv2+
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a webcam display widget.


%prep
%setup -q
%patch0 -p1


%build
%configure --disable-static
make V=1 %{?_smp_mflags}


%install
%make_install

rm -f %{buildroot}%{_libdir}/libcheese.{a,la}
rm -f %{buildroot}%{_libdir}/libcheese-gtk.{a,la}

%find_lang %{name} --with-gnome

chrpath --delete %{buildroot}%{_bindir}/cheese
chrpath --delete %{buildroot}%{_libdir}/libcheese-gtk.so.*


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Cheese.desktop


%post
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :


%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :


%post libs
/sbin/ldconfig
if [ $1 -eq 1 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%postun libs
/sbin/ldconfig
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%doc AUTHORS README
%{_bindir}/cheese
%{_datadir}/applications/org.gnome.Cheese.desktop
%{_datadir}/icons/hicolor/*/apps/cheese.png
%{_datadir}/icons/hicolor/symbolic/apps/cheese-symbolic.svg
%{_datadir}/appdata/org.gnome.Cheese.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Cheese.service
%{_mandir}/man1/cheese.1*

%files camera-service
%license COPYING.GPL3
%{_libexecdir}/gnome-camera-service
%{_datadir}/dbus-1/services/org.gnome.Camera.service

%files -f %{name}.lang libs
%license COPYING
%{_libdir}/libcheese.so.*
%{_libdir}/libcheese-gtk.so.*
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_libdir}/girepository-1.0/Cheese-3.0.typelib

%files libs-devel
%{_libdir}/libcheese.so
%{_libdir}/libcheese-gtk.so
%{_includedir}/cheese/
%{_datadir}/gtk-doc/
%{_libdir}/pkgconfig/cheese.pc
%{_libdir}/pkgconfig/cheese-gtk.pc
%{_datadir}/gir-1.0/Cheese-3.0.gir


%changelog
