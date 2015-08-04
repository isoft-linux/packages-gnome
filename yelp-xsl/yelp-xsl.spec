Name:           yelp-xsl
Version:        3.16.1
Release:        1
Summary:        XSL stylesheets for the yelp help browser

License:        LGPLv2+
Group:          Applications/System
URL:            http://download.gnome.org/sources/yelp-xsl
Source0:        http://download.gnome.org/sources/yelp-xsl/3.10/yelp-xsl-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  libxml2-devel
BuildRequires:  python-libxml2
BuildRequires:  libxslt-devel
BuildRequires:  intltool
BuildRequires:  itstool


%description
This package contains XSL stylesheets that are used by the yelp help browser.


%package devel
Summary: Developer documentation for yelp-xsl
Requires: pkgconfig
Requires: %{name} = %{version}-%{release}

%description devel
The yelp-xsl-devel package contains developer documentation for the
XSL stylesheets in yelp-xsl.


%prep
%setup -q


%build
%configure --enable-doc
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"


%files
%doc README COPYING AUTHORS
%{_datadir}/yelp-xsl


%files devel
%{_datadir}/pkgconfig/yelp-xsl.pc


%changelog
