%define _python_bytecompile_errors_terminate_build 0

Name: gedit-plugins
Version: 3.20.0
Release: 1
Summary: Plugins for Gedit Text editor
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz
BuildRequires:  gedit-devel
BuildRequires:  libgit2-glib-devel
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  gucharmap-devel
BuildRequires:  intltool
BuildRequires:  itstool
Requires:       vte3 >= 0.38.1 
Requires:       gedit

%description
Various plugins for Gedit text editor.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} 

%find_lang gedit-plugins

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas/ >/dev/null 2>&1 ||:

%files -f gedit-plugins.lang
%{_libdir}/gedit/plugins/*
%{_datadir}/gedit/plugins/*
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml
%{_datadir}/help/*/gedit
%{_datadir}/appdata/*.xml
%changelog
* Mon Jul 11 2016 zhouyang <yang.zhou@i-soft.com.cn> - 3.20.0-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 3.18.0-2
- Rebuild for 4.0 release

