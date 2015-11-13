Name: gnome-disk-utility	
Version: 3.18.2
Release: 2 
Summary: Disks application for dealing with storage devices	

License: GPL
URL: http://www.gnome.org
Source0: %{name}-%{version}.tar.xz

BuildRequires: appstream-glib 
BuildRequires: desktop-file-utils
BuildRequires: docbook-style-xsl
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: intltool
# for xsltproc
BuildRequires: libxslt
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libsystemd-login)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(udisks2)

Requires:      udisks2

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

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
%{_datadir}/appdata/org.gnome.DiskUtility.appdata.xml
%{_datadir}/applications/org.gnome.DiskUtility.desktop
%{_datadir}/dbus-1/services/org.gnome.DiskUtility.service
%{_mandir}/man1/gnome-disk-image-mounter.1.gz
%{_mandir}/man1/gnome-disks.1.gz


%changelog
* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1 

