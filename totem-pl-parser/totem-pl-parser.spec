Name:	    totem-pl-parser	
Version:    3.10.6
Release:	1
Summary:    Totem Playlist Parser library	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: gmime-devel
BuildRequires: intltool
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libsoup-2.4)

%description
A library to parse and save playlists, as used in music and movie players

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 

%find_lang totem-pl-parser

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f totem-pl-parser.lang
%{_libdir}/libtotem-plparser-mini.so.*
%{_libdir}/libtotem-plparser.so.*

%files devel
%{_includedir}/totem-pl-parser
%{_libdir}/libtotem-plparser-mini.so
%{_libdir}/libtotem-plparser.so
%{_libdir}/pkgconfig/totem-plparser-mini.pc
%{_libdir}/pkgconfig/totem-plparser.pc
%{_datadir}/gtk-doc/html/totem-pl-parser


%changelog
* Tue Jul 12 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.10.6-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.10.5-2
- Rebuild for 4.0 release


