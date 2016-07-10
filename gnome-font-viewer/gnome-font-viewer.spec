Name:	    gnome-font-viewer	
Version:    3.20.2
Release:    1
Summary:    Utility for previewing fonts for GNOME	

License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires: intltool
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gtk+-3.0)

%description
Use gnome-font-viewer, the Font Viewer, to preview fonts and display
information about a specified font. You can use the Font Viewer to display the
name, style, type, size, version and copyright of the font.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} 


%find_lang gnome-font-viewer


%post
update-desktop-database -q> /dev/null ||:

%postun
update-desktop-database -q> /dev/null ||:

%files -f gnome-font-viewer.lang
%{_bindir}/gnome-font-viewer
%{_bindir}/gnome-thumbnail-font
%{_datadir}/appdata/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/thumbnailers/gnome-font-viewer.thumbnailer
%{_datadir}/applications/org.gnome.font-viewer.desktop
%{_datadir}/dbus-1/services/org.gnome.font-viewer.service


%changelog
* Sun Jul 10 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.2-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.16.2-3
- Rebuild for 4.0 release

