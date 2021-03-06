Name:		gnome-backgrounds
Version:	3.20
Release:	1
Summary:	Backgrounds picture for gnome

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: intltool
BuildArch: noarch

%description
Backgrounds picture for gnome

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang gnome-backgrounds

%files -f gnome-backgrounds.lang
%dir %{_datadir}/backgrounds/gnome
%{_datadir}/backgrounds/gnome/*
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/*


%changelog
* Sat Jul 09 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.0-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

