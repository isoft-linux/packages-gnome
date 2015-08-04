Name:          libmx
Version:       1.4.7
Release:       1
Summary:       A clutter widget toolkit

Group:         System Environment/Libraries
License:       LGPLv2
URL:           http://www.clutter-project.org
Source0:       https://github.com/downloads/clutter-project/mx/mx-%{version}.tar.xz
Patch0:        0001-Replace-GL-data-types-with-equivalent-glib-types.patch

BuildRequires: clutter-devel
BuildRequires: dbus-glib-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gtk2-devel
BuildRequires: pkgconfig
BuildRequires: startup-notification-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gtk-doc

%description
Mx is a clutter widget toolkit that provides a set of standard user interface 
elements, including buttons, progress bars, tooltips, scroll bars and others. 
It also implements some standard layout managers. One other interesting feature 
is the possibility of setting style properties from a css-like file. It is 
currently used by Moblin to provide the user experience.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: clutter-devel, gdk-pixbuf2-devel
Requires: pkgconfig

%description devel
Header files and libraries used for development with MX, a clutter widget 
toolkit, currently used primarily by Moblin.

%package docs
Summary: Documentation files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description docs
This package contains developer documentation for MX, a clutter widget 
toolkit, currently used primarily by Moblin.

%prep
%setup -q -n mx-%{version}
%patch0 -p1 -b .header

%build
%configure --disable-static --enable-introspection --enable-gtk-doc
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang mx-1.0
rpmclean

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f mx-1.0.lang
%defattr(-,root,root,-)
%doc COPYING.LIB README NEWS
%{_bindir}/mx-create-image-cache
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Mx*.typelib
%{_datadir}/mx

%files devel
%defattr(-,root,root,-)
%{_includedir}/mx-1.0
%{_libdir}/pkgconfig/mx*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Mx*.gir

%files docs
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/mx
%{_datadir}/gtk-doc/html/mx-gtk

%changelog
