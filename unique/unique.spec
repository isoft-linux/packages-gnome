Name:           unique
Version:        3.0.2
Release:        2
Summary:        Single instance support for applications

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gnome.org/~ebassi/source/
Source0:        http://download.gnome.org/sources/libunique/1.1/libunique-%{version}.tar.xz

# Fix build -- upstream dead (replaced with GtkApplication)
Patch1:    fix-disable-deprecated.patch

BuildRequires:  dbus-glib-devel
BuildRequires:  gnome-doc-utils >= 0.3.2
BuildRequires:  libtool
BuildRequires:  glib2-devel >= 2.12.0
BuildRequires:  gtk2-devel >= 2.11.0
BuildRequires:  gtk-doc >= 1.11
BuildRequires:  pkgconfig(gtk+-3.0)

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
%patch1 -p1 -b .disable-deprecated

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
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so
%{_includedir}/unique-3.0/unique/unique.h
%{_includedir}/unique-3.0/unique/uniqueapp.h
%{_includedir}/unique-3.0/unique/uniquebackend.h
%{_includedir}/unique-3.0/unique/uniqueenumtypes.h
%{_includedir}/unique-3.0/unique/uniquemessage.h
%{_includedir}/unique-3.0/unique/uniqueversion.h

%changelog
* Wed Jul 13 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.0.2-2
- Update

* Fri May 06 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn> - 1.1.6-1
- 1.1.6
