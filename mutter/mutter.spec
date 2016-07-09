%global gtk3_version 3.19.8
%global gsettings_desktop_schemas_version 3.19.3
%global clutter_version 1.25.6
Name:          mutter
Version:       3.21.2
Release:       1
Summary:       Window and compositing manager based on Clutter

License:       GPLv2+
#VCS:          git:git://git.gnome.org/mutter
URL:           http://www.gnome.org
Source0:       http://download.gnome.org/sources/%{name}/3.10/%{name}-%{version}.tar.xz
Patch0:        mutter_fix_logic-op_error.patch


BuildRequires: clutter-devel  >= %{clutter_version}
BuildRequires: pango-devel
BuildRequires: startup-notification-devel
BuildRequires: gnome-desktop3-devel
BuildRequires: gtk3-devel  >= %{gtk3_version}
BuildRequires: pkgconfig
BuildRequires: gobject-introspection-devel 
BuildRequires: libSM-devel
BuildRequires: libX11-devel
BuildRequires: libXdamage-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXcursor-devel
BuildRequires: libXcomposite-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbfile-devel
BuildRequires: pam-devel
BuildRequires: upower-devel
BuildRequires: xkeyboard-config-devel
BuildRequires: zenity
BuildRequires: desktop-file-utils
# Bootstrap requirements
BuildRequires: gtk-doc gnome-common intltool
BuildRequires: libcanberra-devel
BuildRequires: gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_version}
BuildRequires: automake, autoconf, libtool
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(clutter-egl-1.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(clutter-wayland-1.0)
BuildRequires: pkgconfig(clutter-wayland-compositor-1.0)
BuildRequires: pkgconfig(wayland-server)

# Make sure this can't be installed with an old gnome-shell build because of
# an ABI change.
Conflicts: gnome-shell < 3.9.90

Requires: startup-notification
Requires: dbus-x11
Requires: zenity

%description
Mutter is a window and compositing manager that displays and manages
your desktop via OpenGL. Mutter combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Mutter can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as GNOME Shell. For
this reason, Mutter is very extensible via plugins, which are used both
to add fancy visual effects and to rework the window management
behaviors to meet the needs of the environment.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing Mutter plugins. Also includes
utilities for testing Metacity/Mutter themes.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -f -i
(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; fi; 
%configure --disable-static --enable-compile-warnings=no )

SHOULD_HAVE_DEFINED="HAVE_SM HAVE_RANDR HAVE_STARTUP_NOTIFICATION"

for I in $SHOULD_HAVE_DEFINED; do
  if ! grep -q "define $I" config.h; then
    echo "$I was not defined in config.h"
    grep "$I" config.h
    exit 1
  else
    echo "$I was defined as it should have been"
    grep "$I" config.h
  fi
done

#make %{?_smp_mflags} V=1
make V=1

%install
%make_install

#Remove libtool archives.
rm -rf %{buildroot}/%{_libdir}/*.la

%find_lang %{name}

# Mutter contains a .desktop file so we just need to validate it desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc %{_mandir}/man1/mutter.1.gz
%{_bindir}/mutter
%{_datadir}/applications/*.desktop
%{_libdir}/lib*.so.*
%{_libdir}/mutter/
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
#%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-*.xml
%{_libexecdir}/mutter-restart-helper
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml


%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
# exclude as these should be in a devel package (if packaged at all)
%exclude %{_datadir}/gtk-doc

%changelog
* Fri Jul 08 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.21.2-1
- Update

* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1 

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

