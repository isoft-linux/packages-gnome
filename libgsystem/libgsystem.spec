Name:           libgsystem
Version:        2015.2
Release:        2%{?dist}
Summary:        GIO-based library with Unix/Linux specific API

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/LibGSystem
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgsystem/%{version}/libgsystem-%{version}.tar.xz

BuildRequires: git
# We always run autogen.sh
BuildRequires: autoconf automake libtool
# For docs
BuildRequires: gtk-doc
# Core requirements
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: libattr-devel
BuildRequires: libcap-devel
BuildRequires: gobject-introspection-devel

%description
LibGSystem is a GIO-based library targeted primarily
for use by operating system components.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gobject-introspection-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -Sgit


%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
make check

%files
%doc README COPYING
%{_libdir}/%{name}.so.*
%{_libdir}/girepository-*/*.typelib

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-*/*.gir


%changelog
* Fri Nov 06 2015 Cjacker <cjacker@foxmail.com> - 2015.2-2
- Initial build

