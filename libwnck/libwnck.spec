Summary: Window Navigator Construction Kit
Name: libwnck
Version: 2.31.0
Release: 1%{?dist}
URL: http://download.gnome.org/sources/libwnck/
#VCS: git:git://git.gnome.org/libwnck
Source0: http://download.gnome.org/sources/libwnck/2.31/%{name}-%{version}.tar.xz
License: LGPLv2+

Requires: startup-notification

BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
BuildRequires:  libXt-devel
BuildRequires:  libXres-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel


%description
libwnck (pronounced "libwink") is used to implement pagers, tasklists,
and other such things. It allows applications to monitor information
about open windows, workspaces, their names/icons, and so forth.

%package devel
Summary: Libraries and headers for libwnck
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build

%configure --disable-static --enable-introspection
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

# This package is merely compat for gtk2 apps, now.
# The binaries are shipped in libwnck3
rm -f $RPM_BUILD_ROOT%{_bindir}/wnckprop
rm -f $RPM_BUILD_ROOT%{_bindir}/wnck-urgency-monitor

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/Wnck-1.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0/Wnck-1.0.gir
%doc %{_datadir}/gtk-doc

%changelog
* Fri May 06 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 2.31.0-1
- Initial build

