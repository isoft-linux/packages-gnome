Summary:	JavaScript interpreter and libraries
Name:		mozjs24
Version:	24.2.0
Release:	4
License:	MPLv2.0
URL:		http://www.mozilla.org/js/
Source0:	http://ftp.mozilla.org/pub/mozilla.org/js/mozjs-%{version}.tar.bz2
BuildRequires:	pkgconfig(nspr)
BuildRequires:	readline-devel
BuildRequires:	/usr/bin/zip
BuildRequires:	/usr/bin/python

Patch0:		js17-build-fixes.patch
Patch1:		mozjs24-0001-Add-AArch64-support.patch

%description
JavaScript is the Netscape-developed object scripting language used in millions
of web pages and server applications worldwide. Netscape's JavaScript is a
super set of the ECMA-262 Edition 3 (ECMAScript) standard scripting language,
with only mild differences from the published standard.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n mozjs-%{version}
# Delete bundled sources
rm js/src/editline -rf
rm js/src/ctypes/libffi -rf
%patch0 -p1
%patch1 -p1
chmod a+x configure

%build
%configure \
  --disable-static \
  --with-system-nspr \
  --enable-threadsafe \
  --enable-readline \
  --enable-xterm-updates
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# For some reason the headers and pkg-config file are executable
find %{buildroot}%{_includedir} -type f -exec chmod a-x {} \;
chmod a-x  %{buildroot}%{_libdir}/pkgconfig/*.pc
# Upstream does not honor --disable-static yet
rm -f %{buildroot}%{_libdir}/*.a
# This is also statically linked; once that is fixed that we could
# consider shipping it.
rm -f %{buildroot}%{_bindir}/js24

# However, delete js-config since everything should use
# the pkg-config file.
rm -f %{buildroot}%{_bindir}/js24-config

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE README
%{_libdir}/*.so

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-24

%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 24.2.0-4
- Rebuild for 4.0 release

