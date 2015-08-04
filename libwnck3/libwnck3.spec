Summary: Window Navigator Construction Kit
Name: libwnck3
Version: 3.14.0
Release: 1
URL: http://download.gnome.org/sources/libwnck/
Source0: http://download.gnome.org/sources/libwnck/3.4/libwnck-%{version}.tar.xz
License: LGPLv2+
Group: System Environment/Libraries

Requires: startup-notification

BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libXres-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libtool, automake, autoconf
BuildRequires:  gnome-common
Conflicts: libwnck < 2.30.4-2.fc15

%description
libwnck (pronounced "libwink") is used to implement pagers, tasklists,
and other such things. It allows applications to monitor information
about open windows, workspaces, their names/icons, and so forth.

%package devel
Summary: Libraries and headers for libwnck
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n libwnck-%{version}

%build
rm -f libtool
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang libwnck-3.0

rpmclean
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f libwnck-3.0.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/lib*.so.*
%{_bindir}/wnck-urgency-monitor
%{_libdir}/girepository-1.0/Wnck-3.0.typelib

%files devel
%{_bindir}/wnckprop
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0/Wnck-3.0.gir
%doc %{_datadir}/gtk-doc

%changelog
