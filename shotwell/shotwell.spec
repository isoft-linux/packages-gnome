Name:           shotwell
Version:        0.23.2
Release:        1 
Summary:        A photo organizer for the GNOME desktop

# LGPLv2+ for the code
# CC-BY-SA for some of the icons
License:        LGPLv2+ and CC-BY-SA
URL:            http://www.yorba.org/shotwell/
Source0:        https://download.gnome.org/sources/shotwell/0.22/shotwell-0.22.0.tar.xz

BuildRequires:  vala-devel >= 0.20.1
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(libexif) >= 0.4.90
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkitgtk-3.0)

# Needed by the publishing plugins
BuildRequires:  pkgconfig(rest-0.7)

# used by shotwell-settings-migrator
Requires:       dconf

%description
Shotwell is an easy-to-use, fast photo organizer designed for the GNOME
desktop.  It allows you to import photos from your camera or disk, organize
them by date and subject matter, even ratings.  It also offers basic photo
editing, like crop, red-eye correction, color adjustments, and straighten.
Shotwell's non-destructive photo editor does not alter your master photos,
making it easy to experiment and correct errors.


%prep
%setup -q


%build
./configure \
  --prefix=%{_prefix} \
  --lib=%{_lib} \
  --disable-schemas-compile \
  --disable-icon-update

make %{?_smp_mflags}


%install
export XDG_DISABLE_MAKEFILE_UPDATES=1
# otherwise gettext always returns English text regardless of LANGUAGE asked
export LANG=en_US.utf8
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/shotwell.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/shotwell-viewer.desktop

%find_lang %{name} --with-gnome

%post
update-desktop-database &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f %{name}.lang
%doc README COPYING MAINTAINERS NEWS THANKS AUTHORS
%{_bindir}/shotwell
%{_libdir}/shotwell
%{_libexecdir}/shotwell
%{_datadir}/shotwell
%{_datadir}/applications/shotwell.desktop
%{_datadir}/applications/shotwell-viewer.desktop
%{_datadir}/appdata/shotwell.appdata.xml
%{_datadir}/GConf/gsettings/shotwell.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/shotwell.*


%changelog
* Tue Jul 12 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.23.2-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.22.0-4
- Rebuild for 4.0 release

* Thu Oct 22 2015 Cjacker <cjacker@foxmail.com> - 0.22.0-3
- Rebuild with new LibRaw

