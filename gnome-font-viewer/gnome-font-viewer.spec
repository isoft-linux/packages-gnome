Name:	    gnome-font-viewer	
Version:    3.16.2
Release: 2
Summary:    Utility for previewing fonts for GNOME	

Group:	    Desktop/Gnome/Application	
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

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
make install DESTDIR=%{buildroot} DATADIRNAME=share


%find_lang gnome-font-viewer

rpmclean

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
