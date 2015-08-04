Name:	    gnome-disk-utility	
Version:    3.16.1
Release:	1
Summary:    Disks application for dealing with storage devices	

Group:		Desktop/Gnome/Application
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: libdvdread-devel
BuildRequires: gnome-settings-daemon-devel
BuildRequires: libpwquality-devel

%description
The GNOME Disk Utility package provides applications used for dealing with storage devices.

%prep
%setup -q


%build
%configure --enable-compile-warnings=no
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

cat >>$RPM_BUILD_ROOT%{_datadir}/applications/gnome-disks.desktop <<EOF
Categories=GNOME;GTK;Settings;X-GNOME-SystemSettings;X-GNOME-Settings-Panel;
OnlyShowIn=GNOME;Unity;
NoDisplay=true
EOF

mv $RPM_BUILD_ROOT%{_datadir}/applications/gnome-disks.desktop $RPM_BUILD_ROOT%{_datadir}/applications/gnome-disks-panel.desktop
%find_lang gnome-disk-utility
rpmclean

%post
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f gnome-disk-utility.lang
%{_bindir}/gnome-disk-image-mounter
%{_bindir}/gnome-disks
%{_libdir}/gnome-settings-daemon-3.0/gdu-sd-plugin.gnome-settings-plugin
%{_libdir}/gnome-settings-daemon-3.0/libgdu-sd.a
%{_libdir}/gnome-settings-daemon-3.0/libgdu-sd.so
%{_datadir}/applications/gnome-disk-image-mounter.desktop
%{_datadir}/applications/gnome-disk-image-writer.desktop
%{_datadir}/applications/gnome-disks-panel.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.settings-daemon.plugins.gdu-sd.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/gnome-disk-image-mounter.1.gz
%{_mandir}/man1/gnome-disks.1.gz


%changelog

