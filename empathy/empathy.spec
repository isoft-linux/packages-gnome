Name:	    empathy	
Version:    3.12.12
Release:	1
Summary:    Instant Messaging Client for GNOME	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: telepathy-glib-devel, telepathy-farstream-devel, telepathy-logger-devel
BuildRequires: telepathy-mission-control-devel
BuildRequires: folks-devel webkitgtk-devel 
BuildRequires: intltool
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(clutter-gst-2.0)
BuildRequires: pkgconfig(cogl-1.0)
BuildRequires: itstool

%description
Empathy is powerful multi-protocol instant messaging client which
supports Jabber, GTalk, MSN, IRC, Salut, and other protocols.
It is built on top of the Telepathy framework.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang empathy-tpaw
%find_lang empathy
cat empathy-tpaw.lang >>empathy.lang



%post
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
update-desktop-database -q> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk3-update-icon-cache ]; then
  /usr/bin/gtk3-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:


%files -f empathy.lang
%{_bindir}/*
%{_libdir}/empathy
%{_libdir}/mission-control-plugins.0/mcp-account-manager-goa.so
%{_libexecdir}/*
%{_datadir}/GConf/gsettings/empathy.convert
%dir %{_datadir}/adium
%{_datadir}/adium/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*
%dir %{_datadir}/empathy
%{_datadir}/empathy/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/*/empathy
%{_datadir}/telepathy/clients/*
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/empathy-accounts.1.gz
%{_mandir}/man1/empathy.1.gz


%changelog
* Wed Jul 06 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.12.12-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.12.11-2
- Rebuild for 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.12.11
