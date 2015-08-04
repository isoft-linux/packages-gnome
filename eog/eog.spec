Name:	    eog	
Version:    3.16.2
Release:	1
Summary:    Eye of GNOME image viewer	

Group:		Desktop/Gnome/Application/Multimedia
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: gnome-desktop3-devel

%description
The Eye of GNOME image viewer (eog) is the official image viewer for the
GNOME desktop. It can view single image files in a variety of formats, as
well as large image collections.

eog is extensible through a plugin system.

%package devel
Summary: Plugin development files for %{name}
Requires: %{name} = %{version}-%{release}
Group:   Desktop/Gnome/Development libraries
%description devel
Plugin development files of %{summary}.


%prep
%setup -q


%build
%configure --disable-static --enable-compile-warnings=no
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang eog

rpmclean

%post
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
if [ $1 -eq 1 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

update-desktop-database -q ||:


%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk3-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
update-desktop-database -q ||:

%posttrans
gtk3-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :


%files -f eog.lang
%{_bindir}/eog
%{_datadir}/help/*/eog
%{_libdir}/eog/girepository-1.0/Eog-3.0.typelib
%{_libdir}/eog
%{_datadir}/GConf/gsettings/eog.convert
%{_datadir}/appdata/eog.appdata.xml
%{_datadir}/applications/eog.desktop
%dir %{_datadir}/eog
%{_datadir}/eog/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/glib-2.0/schemas/*

%files devel
%{_datadir}/eog/gir-1.0/Eog-3.0.gir
%dir %{_includedir}/eog-3.0
%{_includedir}/eog-3.0/*
%{_libdir}/pkgconfig/eog.pc
%{_datadir}/gtk-doc/html/eog
