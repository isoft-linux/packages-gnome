Name:	    gmime	
Version:    2.6.20 
Release:	1
Summary:    Library for creating and parsing MIME messages	

Group:		Desktop/Gnome/Runtime libraries
License:	GPL
URL:		http://www.gnome.org
Source0:	%{name}-%{version}.tar.xz

%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Group:   Desktop/Gnome/Development libraries
%description devel
%{summary}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rpmclean
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/girepository-1.0/GMime-2.6.typelib
%{_libdir}/libgmime-2.6.so.*

%files devel
%dir %{_includedir}/gmime-2.6
%{_includedir}/gmime-2.6/*
%{_libdir}/libgmime-2.6.so
%{_libdir}/pkgconfig/gmime-2.6.pc
%{_datadir}/gir-1.0/GMime-2.6.gir
%{_datadir}/gtk-doc/html/gmime-2.6
%{_datadir}/vala/vapi/gmime-2.6.deps
%{_datadir}/vala/vapi/gmime-2.6.vapi
%changelog

