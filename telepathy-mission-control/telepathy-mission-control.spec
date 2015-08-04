%define tp_glib_ver 0.17.5

Name:           telepathy-mission-control
Version:        5.16.3
Release:        1
Epoch:          1
Summary:        Central control for Telepathy connection manager

Group:          System Environment/Libraries
License:        LGPLv2
URL:            http://telepathy.freedesktop.org/wiki/Mission_Control
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

## upstream patches
# fix failing avatar test, https://bugs.freedesktop.org/show_bug.cgi?id=71001
Patch0049: 0049-account-manager-avatar.py-fix-race-condition-by-comb.patch

BuildRequires:  chrpath
BuildRequires:  dbus-python
BuildRequires:  glib2-devel
BuildRequires:  libxslt-devel
BuildRequires:  NetworkManager-glib-devel
BuildRequires:  pygobject2
BuildRequires:  telepathy-glib-devel >= %{tp_glib_ver}
BuildRequires:  gtk-doc


%description
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, and to remove the need to have in each program the
account definitions and credentials.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       dbus-devel
Requires:       dbus-glib-devel
Requires:       telepathy-glib-devel >= %{tp_glib_ver}


%description    devel
The %{name}-devel package contains libraries and header
files for developing applications that use %{name}.


%prep
%setup -q
%patch0049 -p1 -b .0049


%build
%configure \
    --disable-static \
    --enable-gtk-doc \
    --enable-mcd-plugins \
    --with-connectivity=nm \
    --disable-upower

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# Remove lib64 rpaths
chrpath --delete %{buildroot}%{_libexecdir}/mission-control-5

# Remove .la files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

rpmclean

%check
make check ||:


%post -p /sbin/ldconfig


%postun
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%doc AUTHORS NEWS COPYING
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/im.telepathy.MissionControl.FromEmpathy.gschema.xml
%{_libdir}/libmission-control-plugins.so.*
%{_libexecdir}/mission-control-5
%{_mandir}/man*/*.gz


%files devel
%doc %{_datadir}/gtk-doc/html/mission-control-plugins
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libmission-control-plugins.so


%changelog
