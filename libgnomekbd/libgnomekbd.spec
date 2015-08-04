Name:           libgnomekbd
Version:        3.6.0
Release:        3%{?dist}
Summary:        A keyboard configuration library

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gswitchit.sourceforge.net
# VCS: git:git://git.gnome.org/libgnomekbd
Source0:        http://download.gnome.org/sources/libgnomekbd/3.6/libgnomekbd-%{version}.tar.xz

BuildRequires:  gtk3-devel >= 3.0.0
BuildRequires:  cairo-devel
BuildRequires:  libxklavier-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  chrpath
BuildRequires:  gobject-introspection-devel

Obsoletes:      libgnomekbd-capplet < 3.3.90-2

%description
The libgnomekbd package contains a GNOME library which manages
keyboard configuration and offers various widgets related to
keyboard configuration.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The libgnomekbd-devel package contains libraries and header files for
developing applications that use libgnomekbd.


%prep
%setup -q

%build
%configure --disable-static \
           --disable-compile-warnings \
           --enable-introspection
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgnomekbdui.so.8.0.0

desktop-file-install --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  $RPM_BUILD_ROOT%{_datadir}/applications/gkbd-keyboard-display.desktop

%find_lang %{name}

#%preun
#%gconf_schema_remove desktop_gnome_peripherals_keyboard_xkb

%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS COPYING.LIB
%{_libdir}/*.so.*
%{_datadir}/libgnomekbd
%{_datadir}/glib-2.0/schemas/org.gnome.libgnomekbd*.gschema.xml
%{_libdir}/girepository-1.0/Gkbd-3.0.typelib
%{_bindir}/gkbd-keyboard-display
%{_datadir}/applications/gkbd-keyboard-display.desktop
%{_datadir}/GConf/gsettings/libgnomekbd.convert


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Gkbd-3.0.gir


%changelog
