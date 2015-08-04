Name:		yelp
Version:	3.16.1
Release:	1
Summary:    Help browser for the GNOME desktop	
   
Group:		Desktop/Gnome/Application
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: yelp-xsl-devel
#for autogen.sh
BuildRequires: gnome-common
BuildRequires: webkitgtk-devel

Requires: libyelp = %{version}-%{release}

%description
Help browser for the GNOME desktop


%package -n libyelp 
Summary: Runtime libraries for %{name}
Group:   Desktop/Gnome/Runtime libraries
%description -n libyelp 
Runtime libraries of %{summary}.

%package -n libyelp-devel
Summary: Development files for %{name}
Requires: lib%{name} = %{version}-%{release}
Group:   Desktop/Gnome/Development libraries
%description -n libyelp-devel 
Development files of %{summary}.

%prep
%setup -q


%build
export CC=cc
export CXX=c++
%configure --disable-static DATADIRNAME=share
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang yelp
rpmclean

%post -n libyelp -p /sbin/ldconfig
%postun -n libyelp -p /sbin/ldconfig

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


%files -f yelp.lang
%{_bindir}/gnome-help
%{_bindir}/yelp
%{_datadir}/applications/yelp.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.yelp.gschema.xml
%{_datadir}/yelp/icons/hicolor/*/*/*

%files -n libyelp
%{_libdir}/libyelp.so.*
%{_datadir}/yelp-xsl/*
%{_datadir}/yelp/*

%files -n libyelp-devel
%dir %{_includedir}/libyelp
%{_includedir}/libyelp/*
%{_libdir}/libyelp.so
%dir %{_datadir}/gtk-doc/html/libyelp
%{_datadir}/gtk-doc/html/libyelp/*

