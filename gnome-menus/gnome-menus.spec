Summary:     	Implementation of the "Desktop Menu Specification" from freedesktop.org
Name:           gnome-menus 
Version:        3.13.3
Release:       	2
License:        GPLv2+
Source0:       	%{name}-%{version}.tar.xz
%description
Implementation of the "Desktop Menu Specification" from freedesktop.org

%package devel
Summary: Files needed for development using %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}
%build
%configure 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang gnome-menus-3.0
%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f gnome-menus-3.0.lang
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%{_sysconfdir}/xdg/menus/gnome-applications.menu
%{_libdir}/girepository-1.0/GMenu-3.0.typelib
%{_datadir}/desktop-directories/AudioVideo.directory
%{_datadir}/desktop-directories/Development.directory
%{_datadir}/desktop-directories/Education.directory
%{_datadir}/desktop-directories/Game.directory
%{_datadir}/desktop-directories/Graphics.directory
%{_datadir}/desktop-directories/Network.directory
%{_datadir}/desktop-directories/Office.directory
%{_datadir}/desktop-directories/System-Tools.directory
%{_datadir}/desktop-directories/Utility-Accessibility.directory
%{_datadir}/desktop-directories/Utility.directory
%{_datadir}/desktop-directories/X-GNOME-Menu-Applications.directory
%{_datadir}/desktop-directories/X-GNOME-Other.directory
%{_datadir}/desktop-directories/X-GNOME-Sundry.directory
%{_datadir}/desktop-directories/X-GNOME-SystemSettings.directory
%{_datadir}/desktop-directories/X-GNOME-Utilities.directory
%{_datadir}/desktop-directories/X-GNOME-WebApplications.directory

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/GMenu-3.0.gir
%changelog
* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.13.3-2
- Rebuild for 4.0 release

* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

