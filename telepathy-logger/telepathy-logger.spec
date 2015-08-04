Name:           telepathy-logger
Version:        0.8.2
Release:        4
Summary:        Telepathy framework logging daemon

Group:          Applications/Communications
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/Logger
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  dbus-devel >= 1.1.0
BuildRequires:  dbus-glib-devel >= 0.82
BuildRequires:  telepathy-glib-devel >= 0.19.2
BuildRequires:  glib2-devel >= 2.25.11
BuildRequires:  sqlite-devel
BuildRequires:  libxml2-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
## Build Requires needed for tests.
#BuildRequires:	python
#BuildRequires:	python-twisted


%description
%{name} is a headless Observer client that logs information
received by the Telepathy framework. It features pluggable
backends to log different sorts of messages, in different formats.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

# more rpath hacks
%if "%{_libdir}" != "/usr/lib"
sed -i.rpath -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif


%build
export CC=cc
export CXX=c++
%configure --disable-static --enable-introspection=yes
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rpmclean

%check
make check ||:


%post -p /sbin/ldconfig


%postun
/sbin/ldconfig
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &>/dev/null ||:


%posttrans
glib-compile-schemas --allow-any-name %{_datadir}/glib-2.0/schemas &>/dev/null ||:


%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_libexecdir}/%{name}
%{_libdir}/libtelepathy-logger.so.3*
%{_datadir}/glib-2.0/schemas/org.freedesktop.Telepathy.Logger.gschema.xml
%{_datadir}/telepathy/clients/Logger.client
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Logger.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Logger.service
%{_libdir}/girepository-1.0/TelepathyLogger-0.2.typelib


%files devel
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libtelepathy-logger.so
%{_libdir}/pkgconfig/telepathy-logger-0.2.pc
%dir %{_includedir}/telepathy-logger-0.2
%{_includedir}/telepathy-logger-0.2/telepathy-logger/
%{_datadir}/gir-1.0/TelepathyLogger-0.2.gir


%changelog
