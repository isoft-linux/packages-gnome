Summary: Microsoft CHM viewer 
Name:    chmsee
Version: 2.0 
Release: 1 
License: LGPL
Group:  Applications/Multimedia 
Source: %{name}-%{version}.tar.gz
Source10: chmlib-0.40.tar.bz2 
Patch0:  chmsee-link-to-internal-chmlib.patch
BuildRequires: webkitgtk-devel
Requires:webkitgtk

%description
chmsee is a gtk3 chm viewer based on chmlib and webkit engine.

%prep
%setup -a10

%build
export CC=clang
export CXX=clang++

pushd chmlib-0.40
CFLAGS+="-fPIC" ./configure --prefix=`pwd`/../interbin --disable-shared --enable-static
make %{?_smp_mflags}
make install
popd

#for internal static compiled chmlib
sed -i "s|find_library(LIBCHM chm)|find_library(LIBCHM chm `pwd`/interbin/lib)|g" CMakeLists.txt
cat %{PATCH0}|patch -p1
mkdir build
pushd build
CFLAGS="-I`pwd`/../interbin/include" LDFLAGS="-L`pwd`/../interbin/lib" LIBS="-lchm" %cmake ..
make %{?_smp_mflags}
popd

%install
pushd build
%{__make} install DESTDIR="%{buildroot}"
popd

%find_lang chmsee
rpmclean
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f chmsee.lang
%defattr(-, root, root, -)
%{_bindir}/chmsee
%{_datadir}/applications/chmsee.desktop
%dir %{_datadir}/chmsee
%{_datadir}/chmsee/*
%{_datadir}/icons/hicolor/*/mimetypes/chm.*
%{_datadir}/pixmaps/chmsee-icon.png
