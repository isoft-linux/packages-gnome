# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global grilo_version 0.2.12
%global goa_version 3.17.91

Name:		grilo-plugins
Version:	0.2.16
Release:	1%{?dist}
Summary:	Plugins for the Grilo framework

Group:		Applications/Multimedia
License:	LGPLv2+
Url:		https://live.gnome.org/Grilo
Source0:	http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/%{release_version}/grilo-plugins-%{version}.tar.xz

BuildRequires:	avahi-gobject-devel
BuildRequires:	grilo-devel >= %{grilo_version}
BuildRequires:	glib2-devel
BuildRequires:	gom-devel
BuildRequires:	gnome-online-accounts-devel >= %{goa_version}
BuildRequires:	libgcrypt-devel
BuildRequires:	libxml2-devel
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libarchive-devel
BuildRequires:	libmediaart-devel
BuildRequires:	libsoup-devel
BuildRequires:	lua-devel
BuildRequires:	rest-devel
BuildRequires:	sqlite-devel
BuildRequires:	libgdata-devel
BuildRequires:	totem-pl-parser-devel
BuildRequires:	tracker-devel
BuildRequires:	gmime-devel
BuildRequires:	json-glib-devel

Requires:	gnome-online-accounts%{_isa} >= %{goa_version}
Requires:	grilo%{_isa} >= %{grilo_version}

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Apple Trailers
- Bookmarks
- Euronews
- Filesystem
- Flickr
- Freebox
- Gravatar
- iTunes Music Sharing
- Jamendo
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Pocket
- Podcasts
- Radio France
- Shoutcast
- The Guardian Videos
- Tracker
- Vimeo
- Youtube

%prep
%setup -q

%build
%configure				\
	--disable-static		\
	--disable-shoutcast		\
	--enable-bookmarks		\
	--disable-dmap			\
	--enable-filesystem		\
	--enable-flickr			\
	--enable-freebox		\
	--enable-gravatar		\
	--enable-jamendo		\
	--enable-lastfm-albumart	\
	--enable-localmetadata		\
	--enable-lua-factory		\
	--enable-metadata-store		\
	--enable-podcasts		\
	--enable-tmdb			\
	--enable-tracker		\
	--enable-vimeo			\
	--enable-youtube		\
	--enable-tracker

# Silence unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove files that will not be packaged
rm -f $RPM_BUILD_ROOT%{_libdir}/grilo-%{release_version}/*.la
rm -f $RPM_BUILD_ROOT%{_bindir}/*

%find_lang grilo-plugins --with-gnome

%files -f grilo-plugins.lang
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/examples/example-tmdb.c
%{_datadir}/grilo-plugins/
%{_libdir}/grilo-%{release_version}/*.so*
%{_libdir}/grilo-%{release_version}/*.xml

%changelog
