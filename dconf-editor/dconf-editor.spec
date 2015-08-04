%define glib2_version 2.42.0

Name:           dconf-editor
Version:        3.16.1
Release:        2 
Summary:        Configuration editor for dconf 

Group:   Applications/System

License:        LGPLv2+
URL:            http://live.gnome.org/dconf
Source0:        http://download.gnome.org/sources/dconf/0.4/%{name}-%{version}.tar.xz

BuildRequires:  glib2-devel >= %{glib2_version}
Requires:       dbus
Requires:		glib2
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  autoconf automake libtool
BuildRequires:  gobject-introspection-devel >= 0.9.3


%description
docnf-editor allows you to browse and modify dconf databases.


%prep
%setup -q

%build
export CC=cc
export CXX=c++

(if ! test -x configure; then NOCONFIGURE=1 ./autogen.sh; CONFIGFLAGS=--enable-gtk-doc; fi;
 %configure $CONFIGFLAGS \
	--disable-static \
    --disable-man \
)
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang dconf
rpmclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi

%files -f dconf.lang
%defattr(-,root,root,-)
%{_bindir}/dconf-editor
%{_datadir}/dbus-1/services/ca.desrt.dconf-editor.service
%{_datadir}/applications/ca.desrt.dconf-editor.desktop
%{_datadir}/appdata/*.xml
%{_datadir}/glib-*/schemas/*
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/dconf-editor.1.gz
#%{_datadir}/gir-1.0/dconf-0.3.gir

%changelog
* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

