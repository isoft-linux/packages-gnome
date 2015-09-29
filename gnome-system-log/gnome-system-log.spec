Name:           gnome-system-log
Version:        3.9.90
Release:        5%{?dist}
Epoch:          1
Summary:        A log file viewer for GNOME

Group:          Applications/System
License:        GPLv2+ and GFDL
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/gnome-system-log/3.9/gnome-system-log-%{version}.tar.xz
Source1:        gnome-system-log
Source2:        org.gnome.logview.policy

BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: docbook-dtds
BuildRequires: desktop-file-utils
BuildRequires: itstool

Obsoletes: gnome-utils < 1:3.3
Obsoletes: gnome-utils-devel < 1:3.3
Obsoletes: gnome-utils-libs < 1:3.3

%description
gnome-system-log lets you view various log files on your system.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnome-system-log.desktop

mv $RPM_BUILD_ROOT%{_bindir}/gnome-system-log $RPM_BUILD_ROOT%{_bindir}/logview
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}
chmod a+x $RPM_BUILD_ROOT%{_bindir}/gnome-system-log
mkdir -p $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/polkit-1/actions

%find_lang %{name} --with-gnome


%post
for d in hicolor HighContrast ; do
  touch --no-create %{_datadir}/icons/$d >&/dev/null || :
done

%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas >&/dev/null || :
  for d in hicolor HighContrast ; do
    touch --no-create %{_datadir}/icons/$d >&/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/$d >&/dev/null || :
  done
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas >&/dev/null || :
for d in hicolor HighContrast ; do
  gtk-update-icon-cache %{_datadir}/icons/$d >&/dev/null || :
done

%files -f %{name}.lang
%doc COPYING COPYING.docs
%{_bindir}/gnome-system-log
%{_bindir}/logview
%{_datadir}/GConf/gsettings/logview.convert
%{_datadir}/applications/gnome-system-log.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-system-log.gschema.xml
%{_datadir}/icons/hicolor/*/apps/logview.png
%{_datadir}/icons/HighContrast/*/apps/logview.png
%{_datadir}/polkit-1/actions/org.gnome.logview.policy
%doc %{_mandir}/man1/gnome-system-log.1.gz

%changelog
