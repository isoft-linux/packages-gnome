Name:		gnome-backgrounds
Version:	3.16.0
Release:	1
Summary:	Backgrounds picture for gnome

Group:		Desktop/Applications
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

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

