Summary:        A GTK+ GUI builder.
Name:           glade
Version:        3.20.0
Release:        1	
License:        GPL
URL:            http://glade.gnome.org/
Source:         glade-%{version}.tar.xz
Patch0:         glade-remove-user-survey.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-root

Requires:      libglade
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: pango-devel >= %{pango_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: gobject-introspection
BuildRequires: gettext

%description
Glade is a free user interface builder for GTK+ and the GNOME GUI
desktop. Glade can produce C source code. Support for C++, Ada95,
Python, and Perl is also available, via external tools which process
the XML interface description files output by GLADE.

%package -n libglade
Summary: Runtime library for glade.

%description -n libglade 
This package contains runtime libraries for glade.

%package -n libglade-devel
Summary: Development headers and libraries for glade.
Requires: libglade = %{version}-%{release}

%description -n libglade-devel 
%{summary}

%prep
%setup -q
%patch0 -p1
%build
%configure --enable-gladeui
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall 
rm -rf %{buildroot}%{_datadir}/icons/hicolor/*.cache
for i in ca el en_GB gl hi hu ja sl zh_CN
do
    rm -rf %{buildroot}%{_datadir}/help/$i/glade/figures/main-window.png
    pushd %{buildroot}%{_datadir}/help/$i/glade/figures
        ln -sf usr/share/help/C/glade/figures/main-window.png .
    popd
done

%find_lang %{name}
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/appdata/glade.appdata.xml
%{_datadir}/applications/glade.desktop
%{_datadir}/help/*/glade
%{_datadir}/icons/hicolor/*/apps/glade.*
%{_datadir}/icons/hicolor/scalable/apps/glade-symbolic.svg
%{_mandir}/man1/*.gz

%files -n libglade
%defattr(-,root,root)
%{_libdir}/girepository-?.?/Gladeui-2.0.typelib
%{_libdir}/glade/modules/*
%{_libdir}/*.so.*
%dir %{_datadir}/glade
%{_datadir}/glade/*

%files -n libglade-devel
%defattr(-,root,root)
%dir %{_includedir}/libgladeui-?.?
%{_includedir}/libgladeui-?.?/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-?.?/*.gir
%{_datadir}/gtk-doc/html/*


%post
for dir in /usr/share/icons/*; do
  if test -d "$dir"; then
    if test -f "$dir/index.theme"; then
      /usr/bin/gtk3-update-icon-cache --quiet "$dir"
    fi
  fi
done

update-desktop-database ||:

%postun
for dir in /usr/share/icons/*; do
  if test -d "$dir"; then
    if test -f "$dir/index.theme"; then
      /usr/bin/gtk3-update-icon-cache --quiet "$dir"
    fi
  fi
done
update-desktop-database ||:


%changelog
* Mon Jul 11 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.0-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.19.0-4
- Rebuild for 4.0 release

