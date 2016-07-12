Name:	    gnome-user-docs	
Version:    3.20.2
Release:	1
Summary:    GNOME User Documentation	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: itstool
BuildRequires: gettext
BuildArch: noarch

%description
This package contains end-user documentation for the GNOME desktop environment.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%files
%{_datadir}/help/*/system-admin-guide
%{_datadir}/help/*/gnome-help

%changelog
* Tue Jul 12 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.2-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

