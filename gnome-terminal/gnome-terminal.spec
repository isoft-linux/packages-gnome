Name:	    gnome-terminal	
Version:	3.16.2
Release:	1
Summary:    Terminal emulator for GNOME	

Group:		Desktop/Gnome/Application
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

BuildRequires: vte3-devel
BuildRequires: nautilus-devel
BuildRequires: gnome-shell-devel

%description
gnome-terminal is a terminal emulator for GNOME. It features the ability to use
multiple terminals in a single window (tabs) and profiles support.

%prep
%setup -q

%build
%configure --disable-static --disable-migration --disable-schemas-compile
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang gnome-terminal
rpmclean

%post
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-terminal.lang
%{_bindir}/gnome-terminal
%{_libdir}/nautilus/extensions-3.0/libterminal-nautilus.so
#%{_libexecdir}/gnome-terminal-migration
%{_libexecdir}/gnome-terminal-server
%{_datadir}/appdata/gnome-terminal.appdata.xml
%{_datadir}/applications/gnome-terminal.desktop
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_datadir}/gnome-shell/search-providers/gnome-terminal-search-provider.ini
%{_datadir}/help/*/gnome-terminal



%changelog

