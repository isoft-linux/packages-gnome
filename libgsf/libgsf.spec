Summary: GNOME Structured File library
Name: libgsf
Version: 1.14.38
Release: 1
License: LGPLv2
Source: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/1.14/%{name}-%{version}.tar.xz
URL: http://www.gnome.org/projects/libgsf/

BuildRequires: bzip2-devel
BuildRequires: chrpath
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: libxml2-devel

Obsoletes: libgsf-gnome < 1.14.22
Obsoletes: libgsf-python < 1.14.26

%description
A library for reading and writing structured files (e.g. MS OLE and Zip)

%package devel
Summary: Support files necessary to compile applications with libgsf
Requires: libgsf = %{version}-%{release}, glib2-devel, libxml2-devel
Requires: pkgconfig
Obsoletes: libgsf-gnome-devel < 1.14.22

%description devel
Libraries, headers, and support files necessary to compile applications using 
libgsf.

%prep
%setup -q
%build
%configure --disable-gtk-doc --disable-static --enable-introspection=yes

make %{?_smp_mflags} V=1

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=%{buildroot} install

%find_lang %{name}

# Remove lib rpaths
chrpath --delete %{buildroot}%{_bindir}/gsf*


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f libgsf.lang
%doc AUTHORS COPYING COPYING.LIB README
%{_libdir}/libgsf-1.so.*
%{_libdir}/girepository-1.0/Gsf-1.typelib
%{_bindir}/gsf-office-thumbnailer
%{_mandir}/man1/gsf-office-thumbnailer.1.gz
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gsf-office.thumbnailer

%files devel
%{_bindir}/gsf
%{_bindir}/gsf-vba-dump
%{_libdir}/libgsf-1.so
%{_libdir}/pkgconfig/libgsf-1.pc
%dir %{_includedir}/libgsf-1
%{_includedir}/libgsf-1/gsf
%{_datadir}/gtk-doc/html/gsf
%{_datadir}/gir-1.0/Gsf-1.gir
%{_mandir}/man1/gsf.1.gz
%{_mandir}/man1/gsf-vba-dump.1.gz

%changelog
* Sat Jul 09 2016 zhouyang <yang.zhou@i-soft.com.cn> - 1.14.38-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 1.14.34-2
- Rebuild for 4.0 release

* Thu Sep 24 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

