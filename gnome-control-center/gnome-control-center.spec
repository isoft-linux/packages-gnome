Name:		gnome-control-center
Version:	3.16.2
Release:	1
Summary:    The GNOME Control Center	

Group:		Desktop/Gnome/Application
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
Patch0:     gnome-control-center-add-external-desktop-support.patch
Patch1:     gnome-cc-remove-goa.patch
Patch2:     gnome-control-center-DIRTY.patch

BuildRequires: gnome-menus-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libpwquality-devel
BuildRequires: ibus-devel
BuildRequires: grilo-devel
BuildRequires: colord-gtk-devel
BuildRequires: krb5-devel
BuildRequires: libgtop2-devel
BuildRequires: gnome-settings-daemon-devel
BuildRequires: clutter-gtk-devel
BuildRequires: gnome-bluetooth-devel

Requires: cups-pk-helper 
%description
The control center is GNOME's main interface for configuration of
various aspects of your desktop and system.

%prep
%setup -q
#%patch0 -p1
#%patch2 -p1

%build
%configure --enable-ibus
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}  DATADIRNAME=share
%find_lang gnome-control-center-2.0
%find_lang gnome-control-center-2.0-timezones
cat gnome-control-center-2.0-timezones.lang >>gnome-control-center-2.0.lang 
rpmclean

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
