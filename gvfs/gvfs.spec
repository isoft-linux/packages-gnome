%define libbluray_ver 0.6.0
%define libcdio_ver 0.92
%define libcdio_paranoia_ver 10.2+0.90+1 
Summary: Backends for the gio framework in GLib
Name: gvfs
Version: 1.26.1
Release: 2 
License: LGPLv2+
Group: System Environment/Libraries
URL: http://www.gtk.org
Source0: http://download.gnome.org/sources/gvfs/1.26/gvfs-%{version}.tar.xz

BuildRequires: libbluray-devel
BuildRequires: libcdio-devel
BuildRequires: libcdio-paranoia-devel

BuildRequires: pkgconfig
BuildRequires: glib2-devel >= 2.21.2
BuildRequires: dbus-glib-devel
BuildRequires: libsoup-devel >= 2.25.2
BuildRequires: intltool
BuildRequires: gettext-devel
BuildRequires: libsmbclient-devel
BuildRequires: libarchive-devel
BuildRequires: libexif-devel
BuildRequires: libmtp-devel
BuildRequires: libplist-devel
BuildRequires: libimobiledevice-devel

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

# The patch touches Makefile.am files:
BuildRequires: automake autoconf
BuildRequires: libtool

%description
The gvfs package provides backend implementations for the gio
framework in GLib. It includes ftp, sftp, cifs.


%package devel
Summary: Development files for gvfs
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The gvfs-devel package contains headers and other files that are
required to develop applications using gvfs.

%prep
%setup -q 

%build
%configure \
    --enable-http \
    --enable-avahi \
    --enable-udev \
    --enable-fuse \
    --enable-udisks2 \
    --enable-libsystemd-login \
    --enable-gudev \
    --enable-cdda \
    --enable-obexftp \
    --enable-gphoto2 \
    --enable-keyring \
    --enable-bluray \
    --enable-libmtp \
    --enable-samba \
    --enable-gtk \
    --enable-archive \
    --enable-afp \
    --disable-google \
    --with-bash-completion-dir=%{_sysconfdir}/bash_completion.d/
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang gvfs
rpmclean
%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
# Reload .mount files:
killall -USR1 gvfsd >&/dev/null || :
# Update desktop files mime mappings:
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ &> /dev/null ||:

#%post smb
#glib-compile-schemas /usr/share/glib-2.0/schemas/ &> /dev/null ||:
#%postun smb
#glib-compile-schemas /usr/share/glib-2.0/schemas/ &> /dev/null ||:

%postun
/sbin/ldconfig
# Update desktop files mime mappings:
update-desktop-database &> /dev/null ||:
glib-compile-schemas /usr/share/glib-2.0/schemas/ &> /dev/null ||:

%files -f gvfs.lang
%defattr(-, root, root, -)
%{_bindir}/*
%{_libdir}/gio/modules/*
%{_libdir}/tmpfiles.d/*
%dir %{_libdir}/gvfs
%{_libdir}/gvfs/*
%{_libexecdir}/*
%{_datadir}/glib-2.0/schemas/*.xml
%dir %{_datadir}/gvfs
%{_datadir}/gvfs/*
%{_datadir}/GConf/gsettings/gvfs-smb.convert
%{_datadir}/GConf/gsettings/gvfs-dns-sd.convert
%{_datadir}/dbus-1/services/*
%{_mandir}/man?/*
%{_sysconfdir}/bash_completion.d/gvfs*
%{_libdir}/systemd/user/*.service

%files devel
%defattr(-, root, root, -)
%dir %{_includedir}/gvfs-client
%{_includedir}/gvfs-client/*

%changelog
* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

