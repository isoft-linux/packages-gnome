%define _unpackaged_files_terminate_build 0
%define	name		libIDL
%define	version		0.8.14
%define	release		1
%define epoch		1

Summary:	Library for parsing IDL (Interface Definition Language)
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		%{epoch}
License:	LGPL
Group:	 	System Environment/Libraries	
URL:		ftp://ftp.gnome.org
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	glib2 >= 2.2.0

%description
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

%package devel
Summary:	Libraries and include files for %{name}.
Group:		Development/Libraries
Requires:	%{name}

%description devel
Development files for %{name}

%prep
%setup -q

%build
export CFLAGS="-fPIC $RPM_OPT_FLAGS" 
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_infodir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/libIDL-config-2
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libIDL-2.0.pc
%dir %{_includedir}/libIDL-2.0
%{_includedir}/libIDL-2.0/libIDL/*.h
%{_libdir}/*.a

%changelog
* Sun Aug 02 2015 Cjacker <cjacker@foxmail.com>
- build for new release.

* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

