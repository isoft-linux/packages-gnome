Name:	    gnome-system-monitor	
Version:    3.16.0
Release:	1
Summary:     Process and resource monitor	

Group:		Desktop/Gnome/Application
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

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
make install DESTDIR=%{buildroot} DATADIRNAME=share

%find_lang gnome-system-monitor
rpmclean


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


