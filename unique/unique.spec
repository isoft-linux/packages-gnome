Name:           unique
Version:        1.1.6
Release:        1%{?dist}
Summary:        Single instance support for applications

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gnome.org/~ebassi/source/
Source0:        http://download.gnome.org/sources/libunique/1.1/libunique-%{version}.tar.bz2

# Fix build -- upstream dead (replaced with GtkApplication)
Patch0:    fix-unused-but-set-variable.patch
Patch1:    fix-disable-deprecated.patch
Patch2:    libunique-1.1.6-format-security.patch

BuildRequires:  dbus-glib-devel
BuildRequires:  gnome-doc-utils >= 0.3.2
BuildRequires:  libtool
BuildRequires:  glib2-devel >= 2.12.0
BuildRequires:  gtk2-devel >= 2.11.0
BuildRequires:  gtk-doc >= 1.11

%description
Unique is a library for writing single instance applications, that is
applications that are run once and every further call to the same binary
either exits immediately or sends a command to the running instance.

%package devel
Summary: Libraries and headers for Unique
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: dbus-glib-devel
Requires: gtk2-devel

%description devel
Headers and libraries for Unique.

%prep
%setup -q -n libunique-%{?version}
%patch0 -p1 -b .unused-but-set-variable
%patch1 -p1 -b .disable-deprecated
%patch2 -p1 -b .format-security

%build
%configure --enable-gtk-doc --disable-static --enable-introspection=no --enable-maintainer-flags=no
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.*

%files devel
%doc %{_datadir}/gtk-doc
%{_includedir}/unique-1.0/
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so

%changelog
* Fri May 06 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 1.1.6-1
- 1.1.6
