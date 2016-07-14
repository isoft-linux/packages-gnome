%global	dbus_ver	0.95
%global	dbus_glib_ver	0.90
%global	glib_ver	2.36.0
%global gobj_ver	1.30
%global vala_ver	0.16.0

Name:           telepathy-glib
Version:        0.99.11
Release:        3
Summary:        GLib bindings for Telepathy

License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  gtk-doc >= 1.17
BuildRequires:  dbus-devel >= %{dbus_ver}
BuildRequires:	dbus-glib-devel >= %{dbus_glib_ver}
BuildRequires:	glib2-devel >= %{glib_ver}
BuildRequires:	gobject-introspection-devel >= %{gobj_ver}
BuildRequires:	vala-devel >= %{vala_ver}
BuildRequires:	vala-tools
BuildRequires:	libxslt
BuildRequires:	python
BuildRequires:  intltool

%description
Telepathy-glib is the glib bindings for the telepathy unified framework
for all forms of real time conversations, including instant messaging, IRC, 
voice calls and video calls.

%package vala
Summary:    Vala bindings for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   vala


%description vala
Vala bindings for %{name}.

%package 	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-vala = %{version}-%{release}
Requires:	dbus-devel >= %{dbus_ver}
Requires:	dbus-glib-devel >= %{dbus_glib_ver}
Requires:	glib2-devel >= %{glib_ver}
Requires:	pkgconfig


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q 


%build
%configure --enable-static=no --enable-introspection=yes --enable-vala-bindings=yes --enable-compile-warnings=no
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%check
make check ||:


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README NEWS
%{_libdir}/libtelepathy-glib*.so.*
%{_libdir}/girepository-1.0/TelepathyGLib-1.typelib
%{_libdir}/girepository-1.0/TelepathyGLibDBus-1.typelib

%files vala
%{_datadir}/vala/vapi/telepathy-glib-1.deps
%{_datadir}/vala/vapi/telepathy-glib-1.vapi


%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/gtypes.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/telepathy-interfaces.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-account-manager.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-account.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-call-content-media-description.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-call-content.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-call-stream-endpoint.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-call-stream.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-channel-dispatch-operation.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-channel-dispatcher.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-channel-request.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-channel.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-client.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-connection-manager.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-connection.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-debug.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-generic.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-logger.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-protocol.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-cli-tls-cert.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-account-manager.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-account.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-call-content-media-description.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-call-content.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-call-stream-endpoint.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-call-stream.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-channel-dispatch-operation.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-channel-dispatcher.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-channel-request.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-channel.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-client.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-connection-manager.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-connection.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-debug.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-generic.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-logger.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-protocol.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/_gen/tp-svc-tls-cert.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/asv.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/cli-call.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/cli-channel.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/cli-connection.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/cli-misc.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/cli-proxy.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/dbus-properties-mixin.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/gnio-util.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/gtypes.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/interfaces.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/sliced-gvalue.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-account-manager.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-account.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-call.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-channel-dispatch-operation.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-channel-dispatcher.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-channel-request.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-channel.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-client.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-connection-manager.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-connection.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-debug.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-generic.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-interface.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-logger.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-properties-interface.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-protocol.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/svc-tls.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/telepathy-glib-dbus.h
%{_includedir}/telepathy-glib-1-dbus/telepathy-glib/value-array.h
%{_includedir}/telepathy-glib-1/telepathy-glib/_gen/error-str.h
%{_includedir}/telepathy-glib-1/telepathy-glib/_gen/genums.h
%{_includedir}/telepathy-glib-1/telepathy-glib/_gen/telepathy-enums.h
%{_includedir}/telepathy-glib-1/telepathy-glib/account-channel-request.h
%{_includedir}/telepathy-glib-1/telepathy-glib/account-manager.h
%{_includedir}/telepathy-glib-1/telepathy-glib/account-request.h
%{_includedir}/telepathy-glib-1/telepathy-glib/account.h
%{_includedir}/telepathy-glib-1/telepathy-glib/add-dispatch-operation-context.h
%{_includedir}/telepathy-glib-1/telepathy-glib/automatic-client-factory.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-call-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-call-content.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-call-stream.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-client.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-connection-manager.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-connection.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-contact-list.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-media-call-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-media-call-content.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-media-call-stream.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-password-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-protocol.h
%{_includedir}/telepathy-glib-1/telepathy-glib/base-room-config.h
%{_includedir}/telepathy-glib-1/telepathy-glib/call-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/call-content-media-description.h
%{_includedir}/telepathy-glib-1/telepathy-glib/call-content.h
%{_includedir}/telepathy-glib-1/telepathy-glib/call-stream-endpoint.h
%{_includedir}/telepathy-glib-1/telepathy-glib/call-stream.h
%{_includedir}/telepathy-glib-1/telepathy-glib/capabilities.h
%{_includedir}/telepathy-glib-1/telepathy-glib/channel-dispatch-operation.h
%{_includedir}/telepathy-glib-1/telepathy-glib/channel-dispatcher.h
%{_includedir}/telepathy-glib-1/telepathy-glib/channel-filter.h
%{_includedir}/telepathy-glib-1/telepathy-glib/channel-manager-request.h
%{_includedir}/telepathy-glib-1/telepathy-glib/channel-manager.h
%{_includedir}/telepathy-glib-1/telepathy-glib/channel-request.h
%{_includedir}/telepathy-glib-1/telepathy-glib/channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/client-factory.h
%{_includedir}/telepathy-glib-1/telepathy-glib/client-message.h
%{_includedir}/telepathy-glib-1/telepathy-glib/client.h
%{_includedir}/telepathy-glib-1/telepathy-glib/cm-message.h
%{_includedir}/telepathy-glib-1/telepathy-glib/connection-contact-list.h
%{_includedir}/telepathy-glib-1/telepathy-glib/connection-manager.h
%{_includedir}/telepathy-glib-1/telepathy-glib/connection.h
%{_includedir}/telepathy-glib-1/telepathy-glib/contact-operations.h
%{_includedir}/telepathy-glib-1/telepathy-glib/contact-search-result.h
%{_includedir}/telepathy-glib-1/telepathy-glib/contact-search.h
%{_includedir}/telepathy-glib-1/telepathy-glib/contact.h
%{_includedir}/telepathy-glib-1/telepathy-glib/dbus-tube-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/dbus.h
%{_includedir}/telepathy-glib-1/telepathy-glib/debug-client.h
%{_includedir}/telepathy-glib-1/telepathy-glib/debug-message.h
%{_includedir}/telepathy-glib-1/telepathy-glib/debug-sender.h
%{_includedir}/telepathy-glib-1/telepathy-glib/debug.h
%{_includedir}/telepathy-glib-1/telepathy-glib/defs.h
%{_includedir}/telepathy-glib-1/telepathy-glib/dtmf.h
%{_includedir}/telepathy-glib-1/telepathy-glib/enums.h
%{_includedir}/telepathy-glib-1/telepathy-glib/errors.h
%{_includedir}/telepathy-glib-1/telepathy-glib/file-transfer-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/gnio-unix.h
%{_includedir}/telepathy-glib-1/telepathy-glib/group-mixin.h
%{_includedir}/telepathy-glib-1/telepathy-glib/handle-channel-context.h
%{_includedir}/telepathy-glib-1/telepathy-glib/handle-repo-dynamic.h
%{_includedir}/telepathy-glib-1/telepathy-glib/handle-repo-static.h
%{_includedir}/telepathy-glib-1/telepathy-glib/handle-repo.h
%{_includedir}/telepathy-glib-1/telepathy-glib/handle.h
%{_includedir}/telepathy-glib-1/telepathy-glib/heap.h
%{_includedir}/telepathy-glib-1/telepathy-glib/intset.h
%{_includedir}/telepathy-glib-1/telepathy-glib/logger.h
%{_includedir}/telepathy-glib-1/telepathy-glib/message-mixin.h
%{_includedir}/telepathy-glib-1/telepathy-glib/message.h
%{_includedir}/telepathy-glib-1/telepathy-glib/observe-channel-context.h
%{_includedir}/telepathy-glib-1/telepathy-glib/presence-mixin.h
%{_includedir}/telepathy-glib-1/telepathy-glib/protocol.h
%{_includedir}/telepathy-glib-1/telepathy-glib/proxy-subclass.h
%{_includedir}/telepathy-glib-1/telepathy-glib/proxy.h
%{_includedir}/telepathy-glib-1/telepathy-glib/room-info.h
%{_includedir}/telepathy-glib-1/telepathy-glib/room-list.h
%{_includedir}/telepathy-glib-1/telepathy-glib/run.h
%{_includedir}/telepathy-glib-1/telepathy-glib/signalled-message.h
%{_includedir}/telepathy-glib-1/telepathy-glib/simple-approver.h
%{_includedir}/telepathy-glib-1/telepathy-glib/simple-handler.h
%{_includedir}/telepathy-glib-1/telepathy-glib/simple-observer.h
%{_includedir}/telepathy-glib-1/telepathy-glib/simple-password-manager.h
%{_includedir}/telepathy-glib-1/telepathy-glib/stream-tube-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/stream-tube-connection.h
%{_includedir}/telepathy-glib-1/telepathy-glib/telepathy-glib.h
%{_includedir}/telepathy-glib-1/telepathy-glib/text-channel.h
%{_includedir}/telepathy-glib-1/telepathy-glib/tls-certificate-rejection.h
%{_includedir}/telepathy-glib-1/telepathy-glib/tls-certificate.h
%{_includedir}/telepathy-glib-1/telepathy-glib/util.h
%{_includedir}/telepathy-glib-1/telepathy-glib/variant-util.h
%{_includedir}/telepathy-glib-1/telepathy-glib/version.h
%{_libdir}/libtelepathy-glib-1-dbus.so
%{_libdir}/libtelepathy-glib-1.so
%{_datadir}/gir-1.0/TelepathyGLib-1.gir
%{_datadir}/gir-1.0/TelepathyGLibDBus-1.gir
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseCallChannel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseCallContent.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseCallStream.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseChannel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseConnection.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseConnectionManager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseMediaCallChannel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseMediaCallContent.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseMediaCallStream.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpBaseRoomConfig.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpCMMessage.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpCallContentMediaDescription.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpCallStreamEndpoint.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpChannelManager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpChannelManagerRequest.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpClientMessage.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpDebugClient.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpDebugMessage.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpDynamicHandleRepo.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpIntset.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpMessage.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpSignalledMessage.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpStaticHandleRepo.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpTLSCertificate.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/TpTLSCertificateRejection.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/annotation-glossary.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-cli.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-client.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-codegen.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-dbus.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-protocol.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-service-base.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-service-dbus.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-service-handles.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/ch-utilities.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/home.png
%{_datadir}/gtk-doc/html/telepathy-glib-1/index.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/index.sgml
%{_datadir}/gtk-doc/html/telepathy-glib-1/left-insensitive.png
%{_datadir}/gtk-doc/html/telepathy-glib-1/left.png
%{_datadir}/gtk-doc/html/telepathy-glib-1/right-insensitive.png
%{_datadir}/gtk-doc/html/telepathy-glib-1/right.png
%{_datadir}/gtk-doc/html/telepathy-glib-1/style.css
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-1.devhelp2
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpGroupMixin.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpHeap.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpMessageMixin.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpPresenceMixinInterface.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-TpSvcInterface.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-account-channel-request.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-account-manager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-account-request.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-account.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-add-dispatch-operation-context.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-asv.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-automatic-client-factory.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-base-client.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-base-contact-list.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-base-password-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-base-protocol.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-call-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-call-content.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-call-stream.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-capabilities.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-auth.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-contactsearch.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-dispatch-operation.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-dispatcher.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-file-transfer.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-filter.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-group.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-media.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-request.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-room.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-roomlist.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-text.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel-tube.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-account-manager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-anonymity.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-call-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-call-content.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-call-misc.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-call-stream.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-channel-dispatcher.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-client.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-connection-manager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-connection-protocol-specifics.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-connection.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-cli-service-point.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-client-factory.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-client.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-addressing.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-aliasing.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-avatars.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-balance.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-caps.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-cellular.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-client-types.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-contact-info.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-contact-list.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-location.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-mail.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-manager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-powersaving.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-presence.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-renaming.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-requests.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection-sidecars.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-connection.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-contact-search-result.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-contact-search.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-contact.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-dbus-properties-mixin.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-dbus-tube-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-dbus.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-debug-sender.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-debug.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-dtmf.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-enums.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-errors.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-file-transfer-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-gnio-util.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-gtypes.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-handle-channel-context.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-handle-repo.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-handle.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-interfaces.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-logger.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-observe-channel-context.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-protocol.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-proxy-dbus-core.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-proxy-subclass.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-proxy.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-room-info.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-room-list.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-run.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-simple-approver.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-simple-handler.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-simple-observer.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-simple-password-manager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-sliced-gvalue.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-stream-tube-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-stream-tube-connection.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-account-manager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-account.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-anonymity.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-auth.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-call.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-contactsearch.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-dispatch-operation.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-dispatcher.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-file-transfer.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-ft-metadata.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-group.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-request.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-room.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-roomlist.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-securable.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-text.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel-tube.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-client.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-connection-manager.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-connection.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-debug.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-generic.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-logger.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-protocol.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-service-point.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc-tls.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-svc.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-text-channel.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-util.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-value-array.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-vardict.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-variant-util.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/telepathy-glib-version.html
%{_datadir}/gtk-doc/html/telepathy-glib-1/up-insensitive.png
%{_datadir}/gtk-doc/html/telepathy-glib-1/up.png



%changelog
* Thu Jul 14 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.99.11-3
- Update

* Thu Jul 14 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.99.11-2
- Update

* Wed Jul 13 2016 zhouyang <yang.zhou@i-soft.com.cn> - 0.99.11-1
- Update

* Thu Oct 29 2015 Cjacker <cjacker@foxmail.com> - 0.24.1-2
- Rebuild for 4.0 release

