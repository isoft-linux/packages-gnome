Name:           libgxps
Version:        0.2.3.2
Release:        2 
Summary:        GObject based library for handling and rendering XPS documents

License:        LGPLv2+
URL:            http://live.gnome.org/libgxps
Source0:        http://ftp.gnome.org/pub/gnome/sources/%{name}/0.2/%{name}-%{version}.tar.xz

BuildRequires:  gtk3-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  cairo-devel
BuildRequires:  libarchive-devel
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  lcms2-devel
BuildRequires:  chrpath

%description
libgxps is a GObject based library for handling and rendering XPS
documents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        Command-line utility programs for manipulating XPS files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
The %{name}-tools contains command-line programs for manipulating XPS format
documents using the %{name} library.


%prep
%setup -q


%build
%configure --disable-static --enable-man
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/xpsto*


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libgxps

%files tools
%{_bindir}/xpsto*
%{_mandir}/man1/xpsto*.1.gz


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.2.3.2-2
- Rebuild for 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

