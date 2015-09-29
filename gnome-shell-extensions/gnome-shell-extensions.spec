Name: gnome-shell-extensions	
Version: 3.18.0
Release: 1
Summary: Extensions to Modify and extend GNOME Shell functionality and behavior	

Group:	    Desktop/Gnome/Runtime	
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
Requires:   gnome-shell

%description
GNOME Shell Extensions is a collection of extensions providing additional and
optional functionality to GNOME Shell.

Enabled extensions:
  * alternate-tab
  * apps-menu
  * auto-move-windows
  * drive-menu
  * launch-new-instance
  * native-window-placement
  * places-menu
  * systemMonitor
  * user-theme
  * window-list
  * windowsNavigator
  * workspace-indicator


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} DATADIRNAME=share

%find_lang gnome-shell-extensions
rpmclean

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-shell-extensions.lang
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-shell/extensions/*

%changelog
* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

