Name:	    totem-pl-parser	
Version:    3.10.5
Release:	1
Summary:    Totem Playlist Parser library	

Group:		Desktop/Gnome/Runtime/Libraries
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: gmime-devel

%description
A library to parse and save playlists, as used in music and movie players

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Group:   Desktop/Gnome/Development/Libraries
%description devel
%{summary}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} DATADIRNAME=share

%find_lang totem-pl-parser
rpmclean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f totem-pl-parser.lang
%{_libdir}/girepository-1.0/TotemPlParser-1.0.typelib
%{_libdir}/libtotem-plparser-mini.so.*
%{_libdir}/libtotem-plparser.so.*

%files devel
%{_includedir}/totem-pl-parser
%{_libdir}/libtotem-plparser-mini.so
%{_libdir}/libtotem-plparser.so
%{_libdir}/pkgconfig/totem-plparser-mini.pc
%{_libdir}/pkgconfig/totem-plparser.pc
%{_datadir}/gir-1.0/TotemPlParser-1.0.gir
%{_datadir}/gtk-doc/html/totem-pl-parser


%changelog

