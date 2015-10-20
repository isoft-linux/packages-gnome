%global gtk3_version 3.12.0
%global gnome_desktop_version 3.11.1
%global libgweather_version 3.9.5
%global gsettings_desktop_schemas_version 3.9.91
%global geoclue_version 2.1.2
%global geocode_glib_version 3.10.0

Name:           gnome-settings-daemon
Version:        3.18.1
Release:        1
Summary:        The daemon sharing settings from GNOME to GTK+/KDE applications

License:        GPLv2+
URL:            http://download.gnome.org/sources/%{name}
Source:         http://download.gnome.org/sources/%{name}/3.13/%{name}-%{version}.tar.xz
Patch0:         %{name}-3.5.4-ppc-no-wacom.patch

BuildRequires:  gtk3-devel >= %{gtk3_version}
BuildRequires:  gnome-desktop3-devel >= %{gnome_desktop_version}
BuildRequires:  xorg-x11-proto-devel libXxf86misc-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libgnomekbd-devel
BuildRequires:  libnotify-devel
BuildRequires:  gettext intltool
BuildRequires:  fontconfig-devel
BuildRequires:  geoclue2 >= %{geoclue_version}
BuildRequires:  geocode-glib-devel >= %{geocode_glib_version}
BuildRequires:  libcanberra-devel
BuildRequires:  polkit-devel
BuildRequires:  autoconf automake libtool
BuildRequires:  libxklavier-devel
BuildRequires:  gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_version}
BuildRequires:  cups-devel
BuildRequires:  upower-devel
BuildRequires:  libgudev-devel
BuildRequires:  libgweather-devel >= %{libgweather_version}
BuildRequires:  librsvg2-devel
BuildRequires:  nss-devel
BuildRequires:  colord-devel >= 0.1.12
BuildRequires:  lcms2-devel >= 2.2
BuildRequires:  libXi-devel libXfixes-devel
BuildRequires:  systemd-devel
BuildRequires:  libXtst-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  xorg-x11-xkbdata
BuildRequires:  libwacom-devel >= 0.7
BuildRequires:  xorg-x11-drv-wacom-devel

Requires: colord
Requires: geoclue2 >= %{geoclue_version}
Requires: geocode-glib%{?_isa} >= %{geocode_glib_version}
Requires: gnome-desktop3%{?_isa} >= %{gnome_desktop_version}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: libgweather%{?_isa} >= %{libgweather_version}

Obsoletes: %{name}-updates < 3.13.1

%description
A daemon to share settings from GNOME to other applications. It also
handles global keybindings, as well as a number of desktop-wide settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .ppc-no-wacom


%build
autoreconf -i -f
%configure --disable-static \
           --enable-profiling \
           --disable-packagekit \
           --enable-systemd \
           --enable-ibus
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name} --with-gnome

mkdir $RPM_BUILD_ROOT%{_libdir}/gnome-settings-daemon-3.0/gtk-modules

%post
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk3-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
gtk3-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS

# list plugins explicitly, so we notice if one goes missing
# some of these don't have a separate gschema
%{_libdir}/gnome-settings-daemon-3.0/a11y-keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/liba11y-keyboard.so

%{_libdir}/gnome-settings-daemon-3.0/clipboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libclipboard.so

%{_libdir}/gnome-settings-daemon-3.0/datetime.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libdatetime.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.datetime.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/housekeeping.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libhousekeeping.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.housekeeping.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/keyboard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libkeyboard.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.keyboard.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/media-keys.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libmedia-keys.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.media-keys.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/mouse.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libmouse.so

%{_libexecdir}/gsd-backlight-helper
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.power.policy
%{_libdir}/gnome-settings-daemon-3.0/power.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libpower.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.power.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/print-notifications.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libprint-notifications.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.print-notifications.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/librfkill.so
%{_libdir}/gnome-settings-daemon-3.0/rfkill.gnome-settings-plugin

%{_libdir}/gnome-settings-daemon-3.0/screensaver-proxy.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libscreensaver-proxy.so

%{_libdir}/gnome-settings-daemon-3.0/smartcard.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libsmartcard.so

%{_libdir}/gnome-settings-daemon-3.0/sound.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libsound.so

%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.peripherals.wacom.gschema.xml

%ifnarch s390 s390x %{?rhel:ppc ppc64}
%{_libdir}/gnome-settings-daemon-3.0/wacom.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libgsdwacom.so
%{_libexecdir}/gsd-wacom-led-helper
%{_libexecdir}/gsd-wacom-oled-helper
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%endif

%{_libdir}/gnome-settings-daemon-3.0/xrandr.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libxrandr.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.xrandr.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/xsettings.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libxsettings.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.xsettings.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/a11y-settings.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/liba11y-settings.so

%{_libdir}/gnome-settings-daemon-3.0/color.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libcolor.so
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.color.gschema.xml

%{_libdir}/gnome-settings-daemon-3.0/liborientation.so
%{_libdir}/gnome-settings-daemon-3.0/orientation.gnome-settings-plugin
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.orientation.gschema.xml

#%{_libdir}/gnome-settings-daemon-3.0/libcursor.so
#%{_libdir}/gnome-settings-daemon-3.0/cursor.gnome-settings-plugin

%{_libdir}/gnome-settings-daemon-3.0/libgsd.so

%{_libexecdir}/gnome-settings-daemon
%{_libexecdir}/gnome-settings-daemon-localeexec
%{_libexecdir}/gsd-locate-pointer
%{_libexecdir}/gsd-printer

/usr/lib/udev/rules.d/*.rules
%{_datadir}/gnome-settings-daemon/
%{_sysconfdir}/xdg/autostart/gnome-settings-daemon.desktop
%{_datadir}/icons/hicolor/*/apps/gsd-xrandr.*
%{_datadir}/GConf/gsettings/gnome-settings-daemon.convert

%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gschema.xml

%{_datadir}/man/man1/gnome-settings-daemon.1.gz
%{_libdir}/gnome-settings-daemon-3.0/libsharing.so
%{_libdir}/gnome-settings-daemon-3.0/sharing.gnome-settings-plugin
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.sharing.gschema.xml

%files devel
%{_includedir}/gnome-settings-daemon-3.0
%{_libdir}/pkgconfig/gnome-settings-daemon.pc
%dir %{_datadir}/gnome-settings-daemon-3.0
%{_datadir}/gnome-settings-daemon-3.0/input-device-example.sh
%{_libexecdir}/gsd-list-wacom
%{_libexecdir}/gsd-test-wacom
%{_libexecdir}/gsd-test-wacom-osd
%{_libexecdir}/gsd-test-a11y-keyboard
%{_libexecdir}/gsd-test-a11y-settings
#%{_libexecdir}/gsd-test-cursor
%{_libexecdir}/gsd-test-datetime
%{_libexecdir}/gsd-test-housekeeping
%{_libexecdir}/gsd-test-input-helper
%{_libexecdir}/gsd-test-keyboard
%{_libexecdir}/gsd-test-media-keys
%{_libexecdir}/gsd-test-mouse
%{_libexecdir}/gsd-test-orientation
%{_libexecdir}/gsd-test-print-notifications
%{_libexecdir}/gsd-test-rfkill
%{_libexecdir}/gsd-test-screensaver-proxy
%{_libexecdir}/gsd-test-smartcard
%{_libexecdir}/gsd-test-sound
%{_libexecdir}/gsd-test-xrandr
%{_libexecdir}/gsd-test-xsettings

%changelog
* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

