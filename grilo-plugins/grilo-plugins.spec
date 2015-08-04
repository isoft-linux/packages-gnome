Name:	    grilo-plugins	
Version:    0.2.14
Release:	1
Summary:    Plugins for the Grilo framework	

Group:		Desktop/Gnome/Runtime/Base
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: grilo-devel
BuildRequires: avahi-glib-devel
BuildRequires: gupnp-devel
BuildRequires: rest-devel
BuildRequires: libsoup-devel
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
- Metadata Store
- Pocket
- Podcasts
- Radio France
- Shoutcast
- The Guardian Videos
- UPnP
- Vimeo
- Youtube

%prep
%setup -q


%build
#we do not like tracker
%configure \
    --disable-tracker \
    --disable-dmap \
    --enable-compile-warnings=no
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} DATADIRNAME=share

%find_lang grilo-plugins
rpmclean

%files -f grilo-plugins.lang
%{_libdir}/grilo-0.2/grl-apple-trailers.xml
%{_libdir}/grilo-0.2/grl-bliptv.xml
#%{_libdir}/grilo-0.2/grl-bookmarks.xml
%{_libdir}/grilo-0.2/grl-filesystem.xml
%{_libdir}/grilo-0.2/grl-flickr.xml
%{_libdir}/grilo-0.2/grl-freebox.xml
%{_libdir}/grilo-0.2/grl-gravatar.xml
%{_libdir}/grilo-0.2/grl-jamendo.xml
%{_libdir}/grilo-0.2/grl-lastfm-albumart.xml
%{_libdir}/grilo-0.2/grl-local-metadata.xml
%{_libdir}/grilo-0.2/grl-magnatune.xml
%{_libdir}/grilo-0.2/grl-metadata-store.xml
%{_libdir}/grilo-0.2/grl-optical-media.xml
%{_libdir}/grilo-0.2/grl-pocket.xml
%{_libdir}/grilo-0.2/grl-podcasts.xml
%{_libdir}/grilo-0.2/grl-raitv.xml
%{_libdir}/grilo-0.2/grl-shoutcast.xml
%{_libdir}/grilo-0.2/grl-tmdb.xml
#%{_libdir}/grilo-0.2/grl-tracker.xml
#%{_libdir}/grilo-0.2/grl-dmap.xml
%{_libdir}/grilo-0.2/grl-vimeo.xml
%{_libdir}/grilo-0.2/grl-youtube.xml
%{_libdir}/grilo-0.2/libgrlappletrailers.so
%{_libdir}/grilo-0.2/libgrlbliptv.so
#%{_libdir}/grilo-0.2/libgrlbookmarks.so
%{_libdir}/grilo-0.2/libgrlfilesystem.so
%{_libdir}/grilo-0.2/libgrlflickr.so
%{_libdir}/grilo-0.2/libgrlfreebox.so
%{_libdir}/grilo-0.2/libgrlgravatar.so
%{_libdir}/grilo-0.2/libgrljamendo.so
%{_libdir}/grilo-0.2/libgrllastfm-albumart.so
%{_libdir}/grilo-0.2/libgrllocalmetadata.so
%{_libdir}/grilo-0.2/libgrlmagnatune.so
%{_libdir}/grilo-0.2/libgrlmetadatastore.so
%{_libdir}/grilo-0.2/libgrloptical-media.so
%{_libdir}/grilo-0.2/libgrlpocket.so
%{_libdir}/grilo-0.2/libgrlpodcasts.so
%{_libdir}/grilo-0.2/libgrlraitv.so
%{_libdir}/grilo-0.2/libgrlshoutcast.so
%{_libdir}/grilo-0.2/libgrltmdb.so
#%{_libdir}/grilo-0.2/libgrltracker.so
%{_libdir}/grilo-0.2/libgrlvimeo.so
%{_libdir}/grilo-0.2/libgrlyoutube.so
%{_datadir}/help/*/grilo-plugins
#%{_libdir}/grilo-0.2/libgrldmap.so
%{_libdir}/grilo-0.2/grl-dleyna.xml
%{_libdir}/grilo-0.2/grl-lua-factory.xml
%{_libdir}/grilo-0.2/grl-opensubtitles.xml
%{_libdir}/grilo-0.2/libgrldleyna.so
%{_libdir}/grilo-0.2/libgrlluafactory.so
%{_libdir}/grilo-0.2/libgrlopensubtitles.so
%{_datadir}/grilo-plugins/grl-lua-factory/grl-euronews.gresource.xml
%{_datadir}/grilo-plugins/grl-lua-factory/grl-euronews.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.gresource.xml
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-metrolyrics.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-musicbrainz.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.gresource.xml
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.lua


%changelog
