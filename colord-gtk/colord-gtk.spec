Summary:   GTK support library for colord
Name:      colord-gtk
Version:   0.1.26
Release:   2 
License:   LGPLv2+
URL:       http://www.freedesktop.org/software/colord/
Source0:   http://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz

BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: colord-devel >= 0.1.23
BuildRequires: intltool
BuildRequires: lcms2-devel >= 2.2
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools
BuildRequires: gtk3-devel
BuildRequires: gtk-doc

%description
colord-gtk is a support library for colord and provides additional
functionality that requires GTK+.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%setup -q

%build
%configure \
        --disable-gtk-doc \
        --enable-vala \
        --disable-static \
        --disable-rpath \
        --disable-dependency-tracking

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT 

# Remove static libs and libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc README AUTHORS NEWS COPYING
%{_bindir}/cd-convert

%{_libdir}/libcolord-gtk.so.*
%{_libdir}/girepository-1.0/ColordGtk-1.0.typelib
%{_mandir}/man1/cd-convert.1.gz

%files devel
%{_libdir}/libcolord-gtk.so
%{_libdir}/pkgconfig/colord-gtk.pc
%dir %{_includedir}/colord-1
%{_includedir}/colord-1/colord-gtk.h
%dir %{_includedir}/colord-1/colord-gtk
%{_includedir}/colord-1/colord-gtk/*.h
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/ColordGtk-1.0.gir
#%doc %{_datadir}/gtk-doc/html/colord-gtk
%{_datadir}/vala/vapi/colord-gtk.vapi
#%dir %{_datadir}/gtk-doc
#%dir %{_datadir}/gtk-doc/html

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.1.26-2
- Rebuild for 4.0 release

