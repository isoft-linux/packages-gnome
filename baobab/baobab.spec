Name:	    baobab	
Version:    3.16.1
Release:	1
Summary:    A graphical directory tree analyzer	

Group:		Desktop/Gnome/Runtime/Application
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

%description
Baobab is able to scan either specific directories or the whole filesystem, in
order to give the user a graphical tree representation including each
directory size or percentage in the branch.  It also auto-detects in real-time
any change made to your home folder as far as any mounted/unmounted device.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang baobab
rpmclean

%post
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
touch --no-create %{_datadir}/icons/HighContrast
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/HighContrast;
fi

glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
touch --no-create %{_datadir}/icons/HighContrast
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/HighContrast;
fi

glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f baobab.lang
%{_bindir}/baobab
%{_datadir}/appdata/*.xml
%{_datadir}/applications/org.gnome.baobab.desktop
%{_datadir}/dbus-1/services/org.gnome.baobab.service
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_datadir}/help/*/baobab
%{_datadir}/icons/hicolor/*/*/*

%{_mandir}/man1/baobab.1.gz

%changelog

