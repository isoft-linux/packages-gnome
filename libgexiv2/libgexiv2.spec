Name:           libgexiv2
Version:        0.10.3
Release:        1
Summary:        Gexiv2 is a GObject-based wrapper around the Exiv2 library

Group:          System Environment/Libraries
License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/gexiv2
Source0:        https://download.gnome.org/sources/gexiv2/0.10/gexiv2-0.10.3.tar.xz

BuildRequires:  exiv2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libtool
BuildRequires:  python-devel
BuildRequires:  pygobject3-devel

%description
libgexiv2 is a GObject-based wrapper around the Exiv2 library. 
It makes the basic features of Exiv2 available to GNOME applications.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package    python
Summary:    Python2 bindings for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   pygobject3

%description    python
This package contains the python2 bindings for %{name}

%package    python3
Summary:    Python3 bindings for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   python3-gobject 

%description    python3
This package contains the python3 bindings for %{name}

%prep
%setup -q -n gexiv2-%{version}

%build
autoreconf -ivf
%configure --enable-introspection
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT LIB=%{_lib}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

rpmclean

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING MAINTAINERS 
%{_libdir}/libgexiv2.so.*
%{_libdir}/girepository-1.0/GExiv2-*.typelib

%files devel
%{_includedir}/gexiv2/
%{_datadir}/gir-1.0/GExiv2-*.gir
%{_libdir}/libgexiv2.so
%{_libdir}/pkgconfig/gexiv2.pc
%{_datadir}/vala/vapi/gexiv2.vapi


%files python
%{python_sitearch}/gi/overrides/GExiv2.py*

%files python3
%{python3_sitearch}/gi/overrides/GExiv2.py

%changelog
