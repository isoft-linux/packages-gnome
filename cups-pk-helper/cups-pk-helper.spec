Name:           cups-pk-helper
Version:        0.2.5
Release:        1 
Summary:        A helper that makes system-config-printer use PolicyKit

Group:          System Environment/Base
License:        GPLv2+
URL:            http://www.freedesktop.org/wiki/Software/cups-pk-helper/
Source0:        http://www.freedesktop.org/software/cups-pk-helper/releases/cups-pk-helper-%{version}.tar.xz

Patch0:         polkit_result.patch

BuildRequires:  libtool >= 1.4.3
BuildRequires:  cups-devel >= 1.2
BuildRequires:  glib2-devel >= 2.29.8
BuildRequires:  gtk2-devel >= 2.12.0
BuildRequires:  dbus-glib-devel >= 0.74
BuildRequires:  polkit-devel >= 0.97
BuildRequires:  intltool >= 0.40.6
BuildRequires:  gettext-devel >= 0.17
BuildRequires:  gnome-common >= 2.26
BuildRequires:  autoconf automake libtool

Requires:       cups-libs >= 1.2
Requires:       dbus >= 1.2
Requires:       dbus-glib >= 0.74
Requires:       glib2 >= 2.29.8


%description
cups-pk-helper is an application which makes cups configuration
interfaces available under control of PolicyKit.

%prep
%setup -q
%patch0 -p1 -b .polkit-result


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_libexecdir}/cups-pk-helper-mechanism
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf
%{_datadir}/dbus-1/system-services/org.opensuse.CupsPkHelper.Mechanism.service
%{_datadir}/polkit-1/actions/org.opensuse.cupspkhelper.mechanism.policy

%changelog
