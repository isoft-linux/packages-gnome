%global _changelog_trimtime %(date +%s -d "1 year ago")

%global with_nautilus 0

%global with_enca 1
%global with_libcue 1
%global with_thunderbird 1
%global with_rss 1

Name:           tracker
Version:        1.6.0
Release:        2%{?dist}
Summary:        Desktop-neutral search tool and indexer

License:        GPLv2+
URL:            https://wiki.gnome.org/Projects/Tracker
Source0:        https://download.gnome.org/sources/%{name}/1.6/%{name}-%{version}.tar.xz

# only autostart in Gnome, see also
# https://bugzilla.redhat.com/show_bug.cgi?id=771601
Patch0:         0001-Only-autostart-in-GNOME-771601.patch

BuildRequires:  desktop-file-utils
BuildRequires:  firefox
BuildRequires:  giflib-devel
BuildRequires:  graphviz
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  appstream-glib
%if 0%{?with_thunderbird}
BuildRequires:  thunderbird
%endif
BuildRequires:  vala-devel
%if 0%{?with_enca}
BuildRequires:  pkgconfig(enca)
%endif
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
%if 0%{?with_libcue}
BuildRequires:  pkgconfig(libcue)
%endif
BuildRequires:  pkgconfig(libexif)
%if 0%{?with_rss}
BuildRequires:  pkgconfig(libgrss)
%endif
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libmediaart-2.0)
%if 0%{?with_nautilus}
BuildRequires:  pkgconfig(libnautilus-extension)
%endif
BuildRequires:  pkgconfig(libnm-glib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vorbisfile)


%description
Tracker is a powerful desktop-neutral first class object database,
tag/metadata database, search tool and indexer.

It consists of a common object database that allows entities to have an
almost infinite number of properties, metadata (both embedded/harvested as
well as user definable), a comprehensive database of keywords/tags and
links to other entities.

It provides additional features for file based objects including context
linking and audit trails for a file object.

It has the ability to index, store, harvest metadata. retrieve and search
all types of files and other first class objects

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the static libraries and header files needed for
developing with tracker

%package needle
Summary:        Tracker search tool
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      paperbox <= 0.4.4
Obsoletes:      tracker-ui-tools < 1.1.4
Obsoletes:      tracker-search-tool <= 0.12.0

%description needle
Graphical frontend to tracker search.

%package preferences
Summary:        Tracker preferences
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      tracker-ui-tools < 1.1.4

%description preferences
Graphical frontend to tracker configuration.

%package firefox-plugin
Summary:        A simple bookmark exporter for Tracker
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description firefox-plugin
This Firefox addon exports your bookmarks to Tracker, so that you can search
for them for example using tracker-needle.

%if 0%{?with_nautilus}
%package nautilus-plugin
Summary:        Tracker's nautilus plugin
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description nautilus-plugin
Tracker's nautilus plugin, provides 'tagging' functionality. Ability to perform
search in nautilus using tracker is built-in directly in the nautilus package.
%endif

%if 0%{?with_thunderbird}
%package thunderbird-plugin
Summary:        Thunderbird extension to export mails to Tracker
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description thunderbird-plugin
A simple Thunderbird extension to export mails to Tracker.
%endif

%package docs
Summary:        Documentations for tracker
BuildArch:      noarch

%description docs
This package contains the documentation for tracker


%prep
%setup -q

%patch0 -p1 -b .autostart-gnome

%build
%configure --disable-static \
           --enable-gtk-doc \
           --enable-libflac \
           --enable-libvorbis \
           --enable-miner-evolution=no \
           --with-firefox-plugin-dir=%{_libdir}/firefox/extensions \
           --disable-mp3 \
%if %{with_nautilus}
           --enable-nautilus-extension \
%else
           --disable-nautilus-extension \
%endif
           --enable-libmediaart \
%if 0%{?with_thunderbird}
           --with-thunderbird-plugin-dir=%{_libdir}/thunderbird/extensions \
%endif
           --with-unicode-support=libicu \
           --disable-functional-tests
# Disable the functional tests for now, they use python bytecodes.

make V=1 %{?_smp_mflags}


%install
%make_install

find %{buildroot} -type f -name "*.la" -delete
rm -rf %{buildroot}%{_datadir}/tracker-tests

# Remove .so symlinks for private libraries -- no external users are supposed
# to link with them.
rm -f %{buildroot}%{_libdir}/tracker-1.0/*.so

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/tracker-*.desktop


%post -p /sbin/ldconfig

%post preferences
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%postun preferences
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%posttrans preferences
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/tracker*
%{_libexecdir}/tracker*
%{_datadir}/tracker/
%{_datadir}/dbus-1/services/org.freedesktop.Tracker*
%{_libdir}/libtracker*-1.0.so.*
%{_libdir}/tracker-1.0/
%{_libdir}/girepository-1.0/Tracker-1.0.typelib
%{_libdir}/girepository-1.0/TrackerControl-1.0.typelib
%{_libdir}/girepository-1.0/TrackerMiner-1.0.typelib
%{_mandir}/*/tracker*.gz
%config(noreplace) %{_sysconfdir}/xdg/autostart/tracker*.desktop
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/tracker
%{_datadir}/glib-2.0/schemas/*
%exclude %{_bindir}/tracker-needle
%exclude %{_bindir}/tracker-preferences
%exclude %{_datadir}/tracker/tracker-needle.ui
%exclude %{_datadir}/tracker/tracker-preferences.ui
%exclude %{_mandir}/man1/tracker-preferences.1*
%exclude %{_mandir}/man1/tracker-needle.1*

%files devel
%{_includedir}/tracker-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/tracker*.*
%{_datadir}/gir-1.0/Tracker-1.0.gir
%{_datadir}/gir-1.0/TrackerControl-1.0.gir
%{_datadir}/gir-1.0/TrackerMiner-1.0.gir

%files needle
%{_bindir}/tracker-needle
%{_datadir}/appdata/tracker-needle.appdata.xml
%{_datadir}/applications/tracker-needle.desktop
%{_datadir}/tracker/tracker-needle.ui
%{_mandir}/man1/tracker-needle.1*

%files preferences
%{_bindir}/tracker-preferences
%{_datadir}/appdata/tracker-preferences.appdata.xml
%{_datadir}/applications/tracker-preferences.desktop
%{_datadir}/icons/*/*/apps/tracker.*
%{_datadir}/tracker/tracker-preferences.ui
%{_mandir}/man1/tracker-preferences.1*

%files firefox-plugin
%{_datadir}/xul-ext/trackerfox/
%{_libdir}/firefox/extensions/trackerfox@bustany.org

%if 0%{?with_nautilus}
%files nautilus-plugin
%{_libdir}/nautilus/extensions-3.0/libnautilus-tracker-tags.so
%endif

%if 0%{?with_thunderbird}
%files thunderbird-plugin
%{_datadir}/xul-ext/trackerbird/
%{_libdir}/thunderbird/extensions/trackerbird@bustany.org
%{_datadir}/applications/trackerbird-launcher.desktop
%endif

%files docs
%license docs/reference/COPYING
%{_datadir}/gtk-doc/html/libtracker-control/
%{_datadir}/gtk-doc/html/libtracker-miner/
%{_datadir}/gtk-doc/html/libtracker-sparql/
%{_datadir}/gtk-doc/html/ontology/


%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 1.6.0-2
- Rebuild for 4.0 release

