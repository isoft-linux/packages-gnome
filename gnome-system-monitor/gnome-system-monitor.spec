Name: gnome-system-monitor	
Version: 3.18.2
Release: 2
Summary: Process and resource monitor	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libwnck-3.0) 
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(libsystemd-login)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: desktop-file-utils
BuildRequires: intltool gettext
BuildRequires: itstool

%description
gnome-system-monitor allows to graphically view and manipulate the running
processes on your system. It also provides an overview of available resources
such as CPU and memory.

%prep
%setup -q

%build
%configure --enable-systemd --enable-wnck
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 

%find_lang gnome-system-monitor

%post
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-system-monitor.lang
%{_bindir}/gnome-system-monitor
%dir %{_libexecdir}/gnome-system-monitor
%{_libexecdir}/gnome-system-monitor/*
%{_datadir}/appdata/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/*/gnome-system-monitor
%{_datadir}/polkit-1/actions/*

%changelog
* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0.1-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18


