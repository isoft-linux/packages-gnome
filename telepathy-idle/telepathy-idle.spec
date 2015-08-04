%global run_tests 0

Name:           telepathy-idle
Version:        0.2.0
Release:        1
Summary:        IRC connection manager for Telepathy

Group:          Applications/Communications
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	telepathy-glib-devel >= 0.21.0
BuildRequires:  libxslt
%if %{run_tests}
# Build Requires needed for tests.
BuildRequires:	python
BuildRequires:	python-twisted
BuildRequires:	dbus-python
BuildRequires:	pygobject2
%endif

   

%description
A full-featured IRC connection manager for the Telepathy project.


%prep
%setup -q




%build
export CC=cc
export CXX=c++

%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rpmclean


%if %{run_tests}
%check
#make check
%endif

%files
%doc AUTHORS COPYING NEWS
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man8/%{name}.8.gz


%changelog
