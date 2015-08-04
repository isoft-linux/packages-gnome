Name:		libzapojit
Version:	0.0.3
Release:	1
Summary:    GLib/GObject wrapper for the SkyDrive and Hotmail REST APIs	

Group:		Desktop/Gnome/Runtime/Libraries
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: gnome-online-accounts-devel

%description
GLib/GObject wrapper for the SkyDrive and Hotmail REST APIs. It supports SkyDrive file and folder objects, and the following SkyDrive operations: - Deleting a file, folder or photo. - Listing the contents of a folder. - Reading the properties of a file, folder or photo. - Uploading files and photos.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Group:   Desktop/Gnome/Development/ibraries
%description devel
%{summary}.

%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rpmclean

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/girepository-1.0/Zpj-0.0.typelib
%{_libdir}/libzapojit-0.0.so.*
%{_docdir}/libzapojit
%{_datadir}/gir-1.0/Zpj-0.0.gir

%files devel
%{_libdir}/libzapojit-0.0.so
%dir %{_includedir}/libzapojit-0.0
%{_includedir}/libzapojit-0.0/*
%{_libdir}/pkgconfig/zapojit-0.0.pc
%{_datadir}/gtk-doc/html/libzapojit-0.0
