%global _changelog_trimtime %(date +%s -d "1 year ago")
%global _hardened_build 1

%define pango_version 1.2.0
%define gtk3_version 2.99.2
%define pam_version 0.99.8.1-11
%define desktop_file_utils_version 0.2.90
%define nss_version 3.11.1
%define fontconfig_version 2.6.0

Summary: The GNOME Display Manager
Name: gdm
Version: 3.18.0
Release: 2
Epoch: 1
License: GPLv2+
URL: http://download.gnome.org/sources/gdm
#VCS: git:git://git.gnome.org/gdm
Source: http://download.gnome.org/sources/gdm/3.12/gdm-%{version}.tar.xz
Patch0: gdm-remove-selinux-in-pam.patch
Patch1: gdm-remove-force-user-to-allow-gnome-initial-setup-launch.patch
Patch10: gdm-disable-wayland-default.patch

BuildRequires: pkgconfig(libcanberra-gtk)
BuildRequires: pango-devel >= 0:%{pango_version}
BuildRequires: gtk3-devel >= 0:%{gtk3_version}
BuildRequires: pam-devel >= 0:%{pam_version}
BuildRequires: fontconfig >= 0:%{fontconfig_version}
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires: libtool automake autoconf
BuildRequires: libattr-devel
BuildRequires: gettext
BuildRequires: libdmx-devel
BuildRequires: gobject-introspection-devel
BuildRequires: autoconf automake libtool
BuildRequires: intltool
%ifnarch s390 s390x ppc ppc64
BuildRequires: xorg-x11-server-Xorg
%endif
BuildRequires: nss-devel >= %{nss_version}
BuildRequires: iso-codes-devel
BuildRequires: libxklavier-devel >= 4.0
BuildRequires: upower-devel >= 0.9.7
BuildRequires: libXdmcp-devel
BuildRequires: dbus-glib-devel
BuildRequires: GConf2-devel
BuildRequires: pkgconfig(accountsservice) >= 0.6.3
BuildRequires: pkgconfig(libsystemd-login)
BuildRequires: pkgconfig(libsystemd-daemon)
BuildRequires: pkgconfig(ply-boot-client)
BuildRequires: systemd
BuildRequires: dconf

Requires(pre):    /usr/sbin/useradd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

Provides: service(graphical-login) = %{name}

Requires: accountsservice
Requires: dconf
Requires: gnome-session
Requires: gnome-settings-daemon >= 2.21.92
Requires: gnome-shell
Requires: iso-codes
# We need 1.0.4-5 since it lets us use "localhost" in auth cookies
Requires: libXau >= 1.0.4-4
Requires: pam >= 0:%{pam_version}
Requires: /sbin/nologin
Requires: setxkbmap
Requires: systemd >= 186
Requires: xorg-x11-server-utils
Requires: xorg-x11-xinit

Obsoletes: gdm-libs < 1:3.12.0-3
Provides: gdm-libs%{?_isa} = %{epoch}:%{version}-%{release}

# Swallow up old fingerprint/smartcard plugins
Obsoletes: gdm-plugin-smartcard < 1:3.2.1
Provides: gdm-plugin-smartcard = %{epoch}:%{version}-%{release}

Obsoletes: gdm-plugin-fingerprint < 1:3.2.1
Provides: gdm-plugin-fingerprint = %{epoch}:%{version}-%{release}

%package devel
Summary: Development files for gdm
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The gdm-devel package contains headers and other
files needed to build custom greeters.

%description
GDM provides the graphical login screen, shown shortly after boot up,
log out, and when user-switching.

%description devel
Development files and headers for writing GDM greeters.

%prep
%setup -q
%patch1 -p1
%patch10 -p1

%build
export CC=cc
export CXX=c++

autoreconf -i -f
intltoolize -f

for i in `ls data/pam-lfs/gdm*.pam`; do
echo $i
sed -i 's/system-account/system-auth/g' $i
sed -i 's/system-password/system-auth/g' $i
sed -i 's/system-session/system-auth/g' $i
done

%configure --with-pam-prefix=%{_sysconfdir} \
           --with-default-pam-config=lfs \
           --with-run-dir=/run/gdm \
           --enable-split-authentication \
           --enable-profiling      \
           --enable-console-helper \
           --with-plymouth \
           --without-selinux \
           --enable-systemd-journal \
           --with-systemd \
           --enable-compile-warnings=no 

# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool

make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdm/Init
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdm/PreSession
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdm/PostSession

make install DESTDIR=$RPM_BUILD_ROOT 

# docs go elsewhere
rm -rf $RPM_BUILD_ROOT/%{_prefix}/doc

# create log dir
mkdir -p $RPM_BUILD_ROOT/var/log/gdm

# remove the gdm Xsession as we're using the xdm one
#rm -f $RPM_BUILD_ROOT%{_sysconfdir}/gdm/Xsession
(cd $RPM_BUILD_ROOT%{_sysconfdir}/gdm; ln -sf ../X11/xinit/Xsession .)

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/autostart/LoginWindow

mkdir -p $RPM_BUILD_ROOT/run/gdm

find $RPM_BUILD_ROOT -name '*.a' -delete
find $RPM_BUILD_ROOT -name '*.la' -delete

# don't install fallback greeter
rm -rf $RPM_BUILD_ROOT%{_datadir}/gdm/greeter/applications/gdm-simple-greeter.desktop
rm -rf $RPM_BUILD_ROOT%{_datadir}/gdm/greeter/applications/polkit-gnome-authentication-agent-1.desktop

%find_lang gdm --with-gnome

%pre
/usr/sbin/useradd -M -u 42 -d /var/lib/gdm -s /sbin/nologin -r gdm > /dev/null 2>&1
/usr/sbin/usermod -d /var/lib/gdm -s /sbin/nologin gdm >/dev/null 2>&1
# ignore errors, as we can't disambiguate between gdm already existed
# and couldn't create account with the current adduser.
exit 0

%post
/sbin/ldconfig
touch --no-create /usr/share/icons/hicolor >&/dev/null || :

%systemd_post gdm.service

%preun
#%gconf_schema_remove gdm-simple-greeter
%systemd_preun gdm.service

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk3-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi
%systemd_postun

%posttrans
gtk3-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f gdm.lang
%dir %{_sysconfdir}/gdm
%config(noreplace) %{_sysconfdir}/gdm/custom.conf
%config %{_sysconfdir}/gdm/Init/*
%config %{_sysconfdir}/gdm/PostLogin/*
%config %{_sysconfdir}/gdm/PreSession/*
%config %{_sysconfdir}/gdm/PostSession/*
%config %{_sysconfdir}/pam.d/gdm-autologin
%config %{_sysconfdir}/pam.d/gdm-password
# not config files
%{_sysconfdir}/gdm/Xsession
%{_datadir}/gdm/gdm.schemas
%{_sysconfdir}/dbus-1/system.d/gdm.conf
%dir %{_sysconfdir}/gdm/Init
%dir %{_sysconfdir}/gdm/PreSession
%dir %{_sysconfdir}/gdm/PostSession
%dir %{_sysconfdir}/gdm/PostLogin
#%{_datadir}/gnome-session/sessions/gdm-shell.session
%{_datadir}/pixmaps/*.png
%{_datadir}/glib-2.0/schemas/org.gnome.login-screen.gschema.xml
%{_libexecdir}/gdm-host-chooser
%{_libexecdir}/gdm-session-worker
%{_libexecdir}/gdm-simple-chooser
%{_sbindir}/gdm
%{_bindir}/gdmflexiserver
%{_bindir}/gdm-screenshot
%{_datadir}/dconf/profile/gdm
%{_datadir}/gdm/greeter/applications/*
%{_datadir}/gdm/greeter/autostart/*
%{_datadir}/gdm/greeter-dconf-defaults
%{_datadir}/gdm/locale.alias
%{_datadir}/gdm/gdb-cmd
%{_libdir}/girepository-1.0/Gdm-1.0.typelib
%{_libdir}/libgdm*.so*
%dir %{_localstatedir}/log/gdm
%attr(1770, gdm, gdm) %dir %{_localstatedir}/lib/gdm
%attr(0711, root, gdm) %dir /run/gdm
%attr(1755, root, gdm) %dir %{_localstatedir}/cache/gdm
%{_datadir}/icons/hicolor/*/*/*.png
%config %{_sysconfdir}/pam.d/gdm
%config %{_sysconfdir}/pam.d/gdm-pin
%config %{_sysconfdir}/pam.d/gdm-smartcard
%config %{_sysconfdir}/pam.d/gdm-fingerprint
%{_sysconfdir}/pam.d/gdm-launch-environment
%{_unitdir}/gdm.service
%{_libexecdir}/gdm-wayland-session
%{_libexecdir}/gdm-x-session


%files devel
%dir %{_includedir}/gdm
%{_includedir}/gdm/*.h
%{_datadir}/gir-1.0/Gdm-1.0.gir
%{_libdir}/pkgconfig/gdm.pc

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 1:3.18.0-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

