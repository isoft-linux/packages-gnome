Summary:	High-level API for X Keyboard Extension
Name:		libxklavier
Version:	5.3
Release: 	2
License:	LGPLv2+
Group:		Development/Libraries
URL: http://www.freedesktop.org/wiki/Software/LibXklavier
BuildRequires: libxml2-devel
BuildRequires: libxkbfile-devel
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libxml2-devel
BuildRequires: glib2-devel >= 2.6.0
BuildRequires: iso-codes-devel
BuildRequires: gobject-introspection-devel
Requires: iso-codes
Source: http://download.gnome.org/sources/libxklavier/5.3/%{name}-%{version}.tar.xz

%description
libxklavier is a library providing a high-level API for the X Keyboard
Extension (XKB). This library is intended to support XFree86 and other
commercial X servers. It is useful for creating XKB-related software
(layout indicators etc).

%package devel
Summary: Development files for libxklavier
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libxml2-devel

%description devel
This package contains libraries, header files and developer documentation
needed to develop libxklavier applications.

%prep
%setup -q

%build
%configure \
  --disable-static \
  --with-xkb-base='%{_datadir}/X11/xkb' \
  --with-xkb-bin-base='%{_bindir}'

make V=1 %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README COPYING.LIB
%{_libdir}/libxklavier.so.16*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Xkl-1.0.typelib

%files devel
%{_libdir}/pkgconfig/libxklavier.pc
%{_libdir}/libxklavier.so
%{_includedir}/libxklavier/
%{_datadir}/gtk-doc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Xkl-1.0.gir

%changelog
* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

