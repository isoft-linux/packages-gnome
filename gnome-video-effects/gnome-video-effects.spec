Name:           gnome-video-effects
Version:        0.4.1
Release:        4%{?dist}
Summary:        Collection of GStreamer video effects

License:        GPLv2
URL:            http://live.gnome.org/GnomeVideoEffects
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.4/%{name}-%{version}.tar.xz
Buildarch:      noarch

BuildRequires:  intltool

Requires:       frei0r-plugins

%description
A collection of GStreamer effects to be used in different GNOME Modules.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS  COPYING NEWS README
%{_datadir}/pkgconfig/gnome-video-effects.pc
%{_datadir}/gnome-video-effects


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.4.1-4
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

