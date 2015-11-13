Name: gnome-control-center
Version: 3.18.2
Release: 2
Summary: The GNOME Control Center	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(cheese-gtk) 
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(colord)
BuildRequires: pkgconfig(colord-gtk)
BuildRequires: pkgconfig(gdk-wayland-3.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gnome-settings-daemon) 
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(goa-backend-1.0)
BuildRequires: pkgconfig(grilo-0.2)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libnm-glib-vpn) >= 0.9.8
BuildRequires: pkgconfig(libnm-gtk) >= 0.9.8
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(mm-glib)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(smbclient)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libXxf86misc-devel
BuildRequires: chrpath
BuildRequires: gnome-common
BuildRequires: cups-devel
BuildRequires: docbook-style-xsl
BuildRequires: pkgconfig(gnome-bluetooth-1.0)
BuildRequires: pkgconfig(libwacom)

Requires: gnome-settings-daemon
Requires: alsa-lib
Requires: gnome-desktop3
Requires: dbus-x11
Requires: gsettings-desktop-schemas
Requires: gtk3
Requires: gnome-bluetooth
# for user accounts
Requires: accountsservice
# For the user languages
Requires: iso-codes
Requires: vino
# For the printers panel
Requires: cups-pk-helper
# For the network panel
Requires: network-manager-applet
# For the info/details panel
Requires: glx-utils
# For the keyboard panel
Requires: libgnomekbd 
# For the color panel
Requires: colord

%description
The control center is GNOME's main interface for configuration of
various aspects of your desktop and system.

%prep
%setup -q

%build
%configure --enable-ibus
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang gnome-control-center-2.0
%find_lang gnome-control-center-2.0-timezones
cat gnome-control-center-2.0-timezones.lang >>gnome-control-center-2.0.lang 

%post
update-desktop-database -q> /dev/null ||:

%postun
update-desktop-database -q> /dev/null ||:


%files -f gnome-control-center-2.0.lang
%{_bindir}/gnome-control-center
%{_libexecdir}/cc-remote-login-helper
%{_libexecdir}/gnome-control-center-search-provider
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/gnome-control-center
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.ControlCenter.service
%{_datadir}/gnome-control-center
%{_datadir}/gnome-control-center/*
%{_datadir}/gnome-shell/search-providers/gnome-control-center-search-provider.ini
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/gnome-control-center.1.gz
%{_datadir}/pkgconfig/gnome-keybindings.pc
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.datetime.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.remote-login-helper.policy
%{_datadir}/polkit-1/actions/org.gnome.controlcenter.user-accounts.policy
%{_datadir}/polkit-1/rules.d/gnome-control-center.rules
%{_datadir}/sounds/gnome/default/alerts/bark.ogg
%{_datadir}/sounds/gnome/default/alerts/drip.ogg
%{_datadir}/sounds/gnome/default/alerts/glass.ogg
%{_datadir}/sounds/gnome/default/alerts/sonar.ogg

%changelog
* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

