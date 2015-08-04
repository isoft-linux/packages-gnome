Name:	    gnome-user-docs	
Version:    3.16.1
Release:	1
Summary:    GNOME User Documentation	

Group:		gnome
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

%description
This package contains end-user documentation for the GNOME desktop environment.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rpmclean
%files
%{_datadir}/help/*/system-admin-guide
%{_datadir}/help/*/gnome-help

