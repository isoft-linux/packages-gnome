Name:		telepathy-haze
Version:	0.8.0
Release:	1
Summary:	A multi-protocol Libpurple connection manager for Telepathy

Group:		Applications/Communications
License:	GPLv2+
URL:		http://developer.pidgin.im/wiki/Telepathy

Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	dbus-python
BuildRequires:	libpurple-devel >= 2.7
BuildRequires:	pygobject2
#BuildRequires:	python-twisted-words
BuildRequires:	telepathy-glib-devel >= 0.15.1
BuildRequires:  libxslt
  

%description
telepathy-haze is a connection manager built around libpurple, the core of
Pidgin (formerly Gaim), as a Summer of Code project under the Pidgin umbrella.
Ultimately, any protocol supported by libpurple will be supported by
telepathy-haze; for now, XMPP, MSN and AIM are known to work acceptably, and
others will probably work too.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_datadir}/telepathy/managers/haze.manager

rpmclean

%check
make check ||:


%files
%doc COPYING NEWS
%{_libexecdir}/telepathy-haze
%{_datadir}/dbus-1/services/*.haze.service
%{_mandir}/man8/telepathy-haze.8*


%changelog
