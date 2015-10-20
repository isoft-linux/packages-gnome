Name:          zenity
Version:       3.18.0
Release:       1
Summary:       Display dialog boxes from shell scripts
License:       LGPLv2+
URL:           https://wiki.gnome.org/Projects/Zenity
Source:        https://download.gnome.org/sources/zenity/3.12/zenity-%{version}.tar.xz

BuildRequires: gtk3-devel >= 3.0.0
BuildRequires: libnotify-devel >= 0.6.1
BuildRequires: which
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: itstool

%description
Zenity lets you display Gtk+ dialog boxes from the command line and through
shell scripts. It is similar to gdialog, but is intended to be saner. It comes
from the same family as dialog, Xdialog, and cdialog.

%prep
%setup -q


%build
%configure --disable-webkitgtk
make V=1 %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# we don't want a perl dependency just for this
rm $RPM_BUILD_ROOT%{_bindir}/gdialog

%find_lang zenity --with-gnome

%files -f zenity.lang
%doc COPYING AUTHORS NEWS THANKS README
%{_bindir}/zenity
%{_datadir}/zenity
%{_mandir}/man1/zenity.1.gz


%changelog
* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1 

