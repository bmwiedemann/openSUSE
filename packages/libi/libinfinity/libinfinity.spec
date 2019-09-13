#
# spec file for package libinfinity
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _version 0.7
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           libinfinity
Version:        0.7.1
Release:        0
Summary:        Implementation of the Infinote collaborative editing protocol
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://gobby.0x539.de/
Source0:        http://releases.0x539.de/libinfinity/%{name}-%{version}.tar.gz
Source1:        infinoted.service
Source2:        infinoted.sysconfig
Source3:        infinoted.conf
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         infinoted-add-conf-subdir.patch
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.38
BuildRequires:  pkgconfig(gnutls) >= 2.12.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libdaemon)
BuildRequires:  pkgconfig(libgsasl) >= 0.2.21
BuildRequires:  pkgconfig(libxml-2.0)

%description
libinfinity is an implementation of the Infinote protocol written in
GObject-based C. Infinote is a protocol for collaborative editing
multiple documents and is portable to both Windows and Unix-like
platforms.

%package -n libinfinity-1_0-0
Summary:        Implementation of the Infinote collaborative editing protocol
Group:          Development/Libraries/GNOME
Recommends:     %{name}-lang
# Needed to make lang package installable
Provides:       %{name} = %{version}

%description -n libinfinity-1_0-0
libinfinity is an implementation of the Infinote protocol written in
GObject-based C. Infinote is a protocol for collaborative editing
multiple documents and is portable to both Windows and Unix-like
platforms.

%package devel
Summary:        Implementation of the Infinote collaborative editing protocol
Group:          Development/Libraries/GNOME
Requires:       libgnutls-devel
Requires:       libgsasl-devel
Requires:       libinfinity-1_0-0 = %{version}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk+-2.0)
Requires:       pkgconfig(libxml-2.0)

%description devel
libinfinity is an implementation of the Infinote protocol written in
GObject-based C. Infinote is a protocol for collaborative editing
multiple documents and is portable to both Windows and Unix-like
platforms.

%package -n infinoted
Summary:        Server for Collaborative Document Edition
Group:          Development/Libraries/GNOME
Requires:       libinfinity-1_0-0 = %{version}

%description -n infinoted
Infinoted is a server for collaborative edition of documents via the
Infinote protocol. It is typically used with Gobby as a client.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
# -fno-strict-aliasing added 2009-05-07. Need for 0.3.0 -- vuntz
CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
      --disable-static \
      --with-systemd \
      --with-gio
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}-%{_version}
find %{buildroot} -type f -name "*.la" -delete -print
# Install systemd service file
install -d -m 0755 %{buildroot}%{_unitdir}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/infinoted.service
install -d -m 0755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcinfinoted
# Create sysconfig data
install -D -m 0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.infinoted
install -d -m 0755 %{buildroot}/srv/infinoted
# Create infinoted default configuration
install -d -m 0755 %{buildroot}%{_sysconfdir}/xdg/infinoted
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/xdg/infinoted/infinoted.conf
# Note: the infinoted binary is versioned, and we could use update-alternatives
# to provide it also non-versioned. However, the init.d, sysconfig and xdg
# config files are not versioned, and it will actually be bad for the user to
# have them versioned (potential loss of configuration, for example). So let's
# just unversion the binary and man page
mv %{buildroot}%{_bindir}/infinoted-%{_version} %{buildroot}%{_bindir}/infinoted
mv %{buildroot}%{_mandir}/man1/infinoted-%{_version}.1 %{buildroot}%{_mandir}/man1/infinoted.1
%fdupes %{buildroot}

%post -n libinfinity-1_0-0 -p /sbin/ldconfig
%postun -n libinfinity-1_0-0 -p /sbin/ldconfig

%pre -n infinoted
%service_add_pre infinoted.service

%post -n infinoted
%{fillup_only -n infinoted}
%service_add_post infinoted.service

%preun -n infinoted
%stop_on_removal infinoted
%service_del_preun infinoted.service

%postun -n infinoted
%service_del_postun infinoted.service

%files -n libinfinity-1_0-0
%license COPYING
%doc AUTHORS ChangeLog NEWS TODO
%{_libdir}/libinf*.so.*
# Only needed for the test applications, it seems
%exclude %{_datadir}/icons/hicolor/*/apps/infinote.*

%files devel
%{_includedir}/libinf*
%{_libdir}/libinf*.so
%{_libdir}/pkgconfig/libinf*.pc
%{_datadir}/gtk-doc/html/*

%files -n infinoted
%{_bindir}/infinoted
%{_mandir}/man1/infinoted.1%{?ext_man}
%{_libdir}/infinoted-%{_version}
# default configuration
%dir %{_sysconfdir}/xdg/infinoted
%config(noreplace) %{_sysconfdir}/xdg/infinoted/infinoted.conf
%{_sbindir}/rcinfinoted
# sysconfig data
%{_fillupdir}/sysconfig.infinoted
%dir /srv/infinoted
%{_unitdir}/infinoted.service

%files lang -f %{name}-%{_version}.lang

%changelog
