Name:           libgit2-glib
Version:        0.23.6
Release:        3 
Summary:        Git library for GLib

License:        LGPLv2+
URL:            https://live.gnome.org/Libgit2-glib
Source0:        http://download.gnome.org/sources/libgit2-glib/0.22/libgit2-glib-%{version}.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  libgit2-devel
BuildRequires:  pygobject3-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
# Depend on python3-gobject for the python3 gi overrides directory.
# If we ever get a libgit2-glib consumer that does not depend on python3,
# it would probably make sense to split it to a separate subpackage.
Requires:       python3-gobject

%description
libgit2-glib is a glib wrapper library around the libgit2 git access library.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --enable-more-warnings=yes
make %{?_smp_mflags}


%install
%make_install
# Remove unwanted la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING NEWS
%{_libdir}/libgit2-glib-1.0.so.*
%{_libdir}/girepository-1.0/Ggit-1.0.typelib
%{python3_sitearch}/gi/overrides/*

%files devel
%{_includedir}/libgit2-glib-1.0/
%{_libdir}/libgit2-glib-1.0.so
%{_libdir}/pkgconfig/libgit2-glib-1.0.pc
%{_datadir}/gir-1.0/Ggit-1.0.gir
%{_datadir}/vala/vapi/ggit-1.0.deps
%{_datadir}/vala/vapi/ggit-1.0.vapi

%doc %{_datadir}/gtk-doc/


%changelog
* Fri Nov 06 2015 Cjacker <cjacker@foxmail.com> - 0.23.6-3
- Rebuild with python3.5

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.23.6-2
- Rebuild for 4.0 release

