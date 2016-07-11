Name: gnome-shell-extensions	
Version: 3.21.2
Release: 1
Summary: Extensions to Modify and extend GNOME Shell functionality and behavior	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)

Requires: gnome-shell

BuildArch: noarch

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
make install DESTDIR=%{buildroot}

%find_lang gnome-shell-extensions

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-shell-extensions.lang
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-shell/extensions/*

%changelog
* Mon Jul 11 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.21.2-1
- Update

* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1
* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

