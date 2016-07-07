Name:		yelp
Version:	3.21.3
Release:	1
Summary:    Help browser for the GNOME desktop	
   
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: yelp-xsl-devel
BuildRequires: pkgconfig(libexslt)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-unix-print-3.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: intltool
BuildRequires: libgcrypt-devel
BuildRequires: libgpg-error-devel
#for autogen.sh
BuildRequires: gnome-common
#BuildRequires: webkitgtk4-devel

Requires: libyelp = %{version}-%{release}

%description
Help browser for the GNOME desktop


%package -n libyelp 
Summary: Runtime libraries for %{name}
%description -n libyelp 
Runtime libraries of %{summary}.

%package -n libyelp-devel
Summary: Development files for %{name}
Requires: lib%{name} = %{version}-%{release}
%description -n libyelp-devel 
Development files of %{summary}.

%prep
%setup -q

%build
export CC=cc
export CXX=c++
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%find_lang yelp

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
%dir %{_libdir}/yelp
#%{_libdir}/yelp/libyelpcommon.so
%{_libdir}/yelp/web-extensions/libyelpwebextension.so

%{_datadir}/yelp-xsl/*
%{_datadir}/yelp/*

%files -n libyelp-devel
%dir %{_includedir}/libyelp
%{_includedir}/libyelp/*
%{_libdir}/libyelp.so
%dir %{_datadir}/gtk-doc/html/libyelp
%{_datadir}/gtk-doc/html/libyelp/*

%changelog
* Wed Jul 06 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.21.3-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Thu Sep 24 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

