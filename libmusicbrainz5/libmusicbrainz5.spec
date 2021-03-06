Summary: Library for accessing MusicBrainz servers
Name: libmusicbrainz5
Version: 5.1.0
Release: 1
License: LGPLv2
URL: http://www.musicbrainz.org/
Source0: libmusicbrainz-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(neon)
Obsoletes: libmusicbrainz4 < 4.0.3-5

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: libmusicbrainz4-devel < 4.0.3-5

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.


%prep
%setup -q -n libmusicbrainz-%{version}
# omit "Generated on ..." timestamps that induce multilib conflicts
# this is *supposed* to be the doxygen default in fedora these days, but
# it seems there's still a bug or 2 there -- Rex
echo "HTML_TIMESTAMP      = NO" >> Doxyfile.cmake


%build
%{cmake} .

make %{?_smp_mflags} V=1
make %{?_smp_mflags} docs


%install

make install/fast DESTDIR=%{buildroot}

rm -f docs/installdox

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS.txt COPYING.txt NEWS.txt README.md
%{_libdir}/libmusicbrainz5.so.1*

%files devel
%doc docs/*
%{_includedir}/musicbrainz5/
%{_libdir}/libmusicbrainz5.so
%{_libdir}/pkgconfig/libmusicbrainz5.pc


%changelog
* Tue Jul 12 2016 zhouyang <yang.zhou@i-soft.com.cn> - 5.1.0-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 5.0.1-11
- Rebuild for 4.0 release

