Summary: A high-performance CORBA Object Request Broker.
Name: ORBit2
Version: 2.14.19
Release: 2
Source: %{name}-%{version}.tar.bz2
Patch0: ORBit2-2.14.3-ref-leaks.patch  
Patch1: ORBit2-allow-deprecated.patch  
Patch2: ORBit2-make-j-safety.patch
License: LGPL/GPL
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL: http://www.gnome.org/projects/ORBit2/
BuildRequires: libIDL-devel
BuildRequires: glib2-devel

BuildRequires: pkgconfig
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gtk-doc

%description
ORBit is a high-performance CORBA (Common Object Request Broker 
Architecture) ORB (object request broker). It allows programs to 
send requests and receive replies from other programs, regardless 
of the locations of the two programs. CORBA is an architecture that 
enables communication between program objects, regardless of the 
programming language they're written in or the operating system they
run on.

You will need to install this package and ORBit-devel if you want to 
write programs that use CORBA technology.

%package devel
Summary: Development libraries, header files and utilities for ORBit.
#Requires: indent
Requires: glib2-devel
Requires: libIDL-devel >= %{libidl_version}
Requires: ORBit2 = %{version}
Requires: glib2-devel >= %{glib2_version}
Conflicts: ORBit-devel <= 1:0.5.8

%description devel
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker) with support for the 
C language.

This package contains the header files, libraries and utilities 
necessary to write programs that use CORBA technology. If you want to
write such programs, you'll also need to install the ORBIT package.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
 
%build
libtoolize --force --copy
aclocal
autoconf
%configure --enable-gtk-doc --enable-purify
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/ORBit-2.0/*.*a
rm -f $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/*.*a


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_libdir}/orbit-2.0/*.so*

%files devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_bindir}/orbit-idl-2
%{_bindir}/typelib-dump
%{_bindir}/orbit2-config
%{_bindir}/ior-decode-2
%{_includedir}/*
%{_datadir}/aclocal/*
%{_datadir}/idl/orbit-2.0
%{_bindir}/linc-cleanup-sockets
%{_datadir}/gtk-doc

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 2.14.19-2
- Rebuild for 4.0 release

* Sun Aug 02 2015 Cjacker <cjacker@foxmail.com>
- build for new release

* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

