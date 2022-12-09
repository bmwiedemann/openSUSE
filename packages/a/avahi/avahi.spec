#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define _name avahi
%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "qt5"
%global psuffix -qt5
%global build_qt5 1
%global build_glib2 0
%global build_core 0
%else
%if "%{flavor}" == "glib2"
%global psuffix -glib2
# NOTE: build_glib2 also controls build of gobject, gtk3 and pygobject code.
%global build_qt5 0
%global build_glib2 1
%global build_core 0
%else
%global psuffix %{nil}
%global build_qt5 0
%global build_glib2 0
%global build_core 1
%endif
%endif
%define avahi_client_sover 3
%define avahi_common_sover 3
%define avahi_core_sover 7
%define avahi_libevent_sover 1
%define avahi_libhowl_sover 0
%define avahi_ui_sover 0
%define avahi_glib_sover 1
%define avahi_gobject_sover 0
%define avahi_gtk3_sover 0
%define avahi_qt5_sover 1
%if %{build_glib2}
%define debug_package_requires libavahi-ui%{avahi_ui_sover} = %{version}-%{release}
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define oldpython python
Name:           avahi%{psuffix}
Version:        0.8
Release:        0
Summary:        D-Bus Service for Zeroconf and Bonjour
License:        LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://www.avahi.org/
Source:         https://avahi.org/download/%{_name}-%{version}.tar.gz
# Copy of glib-2.0.m4 from glib2-devel to not depend on glib2-devel.
Source4:        avahi-glib-gettext.m4
Source5:        avahi.sysconfig
Source6:        avahi-autoipd.sysconfig
Source9:        avahi-autoipd.README.SUSE
Source10:       avahi-autoipd.if-up
Source11:       avahi-autoipd.if-down
Source13:       avahi.sysusers
Source14:       avahi-autoipd.sysusers
# File missing from 0.8 tarball
Source12:       https://raw.githubusercontent.com/lathiat/avahi/master/service-type-database/build-db
Source100:      attributes
Source101:      update_spec.pl
Source102:      baselibs.conf
Source103:      avahi-rpmlintrc
# PATCH-FIX-OPENSUSE avahi-gacdir.patch -- Mono libs are in $prefix/lib on suse
Patch0:         avahi-gacdir.patch
# PATCH-FIX-UPSTREAM avahi-desktop.patch bnc254654 Avahi#365 -- sbrabec@suse.cz
Patch1:         avahi-desktop.patch
# PATCH-FIX-OPENSUSE avahi-add-resolv-conf-to-inotify.patch bsc#982317 boo#1194561 mgorse@suse.com -- reconfigure when resolv.conf changes.
Patch19:        avahi-add-resolv-conf-to-inotify.patch
# PATCH-FIX-UPSTREAM add-IT_PROG_INTLTOOL.patch alarrosa@suse.com -- add IT_PROG_INTLTOOL so intltool works
Patch20:        add-IT_PROG_INTLTOOL.patch
# PATCH-FIX-UPSTREAM avahi-CVE-2021-3468.patch boo#1184521 mgorse@suse.com -- avoid infinite loop by handling HUP event in client_work.
Patch21:        avahi-CVE-2021-3468.patch
# PATCH-FIX-UPSTREAM avahi-CVE-2021-3502.patch boo#1184846 mgorse@suse.com -- fix NULL pointer crashes.
Patch22:        avahi-CVE-2021-3502.patch
# PATCH-FIX-UPSTREAM 0001-man-fix-reference-to-avahi-autoipd.action-8-in-avahi.patch mgorse@suse.com -- fix a manpage reference.
Patch23:        0001-man-fix-reference-to-avahi-autoipd.action-8-in-avahi.patch
# PATCH-FIX-UPSTREAM 0005-avahi-dnsconfd.service-Drop-Also-avahi-daemon.socket.patch mgorse@suse.com -- disabling avahi-dnsconfd should not also disable avahi-daemon.socket.
Patch24:        0005-avahi-dnsconfd.service-Drop-Also-avahi-daemon.socket.patch
# PATCH-FIX-UPSTREAM 0006-man-add-missing-bshell.1-symlink.patch mgorse@suse.com -- add manpage symlink.
Patch25:        0006-man-add-missing-bshell.1-symlink.patch
# PATCH-FIX-UPSTREAM 0007-Ship-avahi-discover-1-bssh-1-and-bvnc-1-also-for-GTK.patch mgorse@suse.com -- ship some manpages that were missing when gtk 2 is disabled.
Patch26:        0007-Ship-avahi-discover-1-bssh-1-and-bvnc-1-also-for-GTK.patch
# PATCH-FIX-UPSTREAM 0009-fix-bytestring-decoding-for-proper-display.patch mgorse@suse.com -- fix bytestring decoding for proper display.
Patch27:        0009-fix-bytestring-decoding-for-proper-display.patch
Patch28:        harden_avahi-daemon.service.patch
Patch29:        harden_avahi-dnsconfd.service.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  intltool
BuildRequires:  libdaemon-devel
BuildRequires:  libexpat-devel
BuildRequires:  sysuser-tools
# libtool is needed to build all variants: bootstrap is unconditional in the build section
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  strip-nondeterminism
BuildRequires:  xmltoman
%if %{build_core}
BuildRequires:  dbus-1-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libevent-devel >= 2.1.5
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
Requires:       nss-mdns
Requires:       sudo
%sysusers_requires
#
# mDNSResponder was used for <= 10.2:
Provides:       mDNSResponder = 107.5
Obsoletes:      mDNSResponder < 107.5
# Disable this conflict for now, it breaks staging, and it's pretty much obsolete, but can go back in if needed once a new version of avahi is released.
# File conflict for service-types.db openSUSE <= 12.3 SLE <= 11SP2
#Conflicts:      avahi-utils <= 0.6.31-9.2
%endif
%if %{build_glib2}
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  libavahi-devel = %{version}
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(pygobject-3.0)
%endif
%if %{build_qt5}
BuildRequires:  dbus-1-devel
BuildRequires:  libavahi-devel = %{version}
BuildRequires:  pkgconfig(Qt5Core)
Requires:       libavahi-client%{avahi_client_sover} >= %{version}
%endif
BuildRequires:  python-rpm-macros
%if %{build_core}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module dbus-python}
%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
# Same defaults for all build targets
%define python_sitelib %python3_sitelib
%define python_files() -n python3-%{**}
%endif
%else
# Even if we don't install the python bindings outside of build_core, we need the default python3 to build the service types database:
%define pythons python3
BuildRequires:  python3-dbm
BuildRequires:  python3-dbus-python
# avoid error from unused python_subpackages
%define python_files() -n python3-%{**}
%endif

%description
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing. It uses D-Bus for
communication between user applications and a system daemon. The daemon
is used to coordinate application efforts in caching replies, necessary
to minimize the traffic imposed on networks.

The Avahi mDNS responder is now complete with features, implementing
all MUSTs and the majority of the SHOULDs of the mDNS and DNS-SD RFCs.
It passes all tests in the Apple Bonjour conformance test suite. In
addition, it supports some nifty things, like correct mDNS reflection
across LAN segments.

%package -n libavahi-client%{avahi_client_sover}
Summary:        D-Bus Service for Zeroconf and Bonjour
Group:          System/Libraries

%description -n libavahi-client%{avahi_client_sover}
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%package -n libavahi-common%{avahi_common_sover}
Summary:        D-Bus Service for Zeroconf and Bonjour
Group:          System/Libraries

%description -n libavahi-common%{avahi_common_sover}
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%package -n libavahi-core%{avahi_core_sover}
Summary:        D-Bus Service for Zeroconf and Bonjour
Group:          System/Libraries

%description -n libavahi-core%{avahi_core_sover}
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%package -n libavahi-libevent%{avahi_libevent_sover}
Summary:        D-Bus Service for Zeroconf and Bonjour
Group:          System/Libraries

%description -n libavahi-libevent%{avahi_libevent_sover}
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%package -n libdns_sd
Summary:        mDNSResponder Compatibility Package for the Zeroconf/Bonjour D-Bus service
# mDNSResponder-lib used unversioned soname.
# Provide full compatibility with mDNSResponder (FIXME: should be fixed in the package):
#
# mDNSResponder-lib was used for <= 10.2:
Group:          System/Libraries
Provides:       mDNSResponder-lib = 107.5
Obsoletes:      mDNSResponder-lib < 107.5
# Old name used for <= 10.3:
Provides:       avahi-compat-mDNSResponder = %{version}
Obsoletes:      avahi-compat-mDNSResponder < %{version}
%ifarch ia64 x86_64 ppc64 s390x
Provides:       libdns_sd.so()(64bit)
%else
Provides:       libdns_sd.so
%endif

%description -n libdns_sd
Apple mDNSResponder compatibility layer for Avahi.

Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.

%package -n libhowl%{avahi_libhowl_sover}
Summary:        Howl Compatibility Package for the Zeroconf/Bonjour D-Bus service
# Old name used for <= 10.3:
Group:          System/Libraries
Provides:       avahi-compat-howl = %{version}
Obsoletes:      avahi-compat-howl < %{version}

%description -n libhowl%{avahi_libhowl_sover}
Howl compatibility layer for Avahi.

Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.

%if 0%{?python_subpackage_only}
%package -n python-avahi
Summary:        A set of Avahi utilities written in Python
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-Twisted
Requires:       python-dbm
Requires:       python-dbus-python
# Old name used for <= 10.3:
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       avahi-python = %{version}
Obsoletes:      %{oldpython}-avahi < %{version}
Obsoletes:      avahi-python < %{version}
%endif

%description -n python-avahi
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%else

%package -n python3-avahi
Summary:        A set of Avahi utilities written in Python
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python3-Twisted
Requires:       python3-dbm
Requires:       python3-dbus-python
# Old name used for <= 10.3:
Provides:       avahi-python = %{version}
Obsoletes:      avahi-python < %{version}
Obsoletes:      python-avahi < %{version}

%description -n python3-avahi
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.
%endif

%package autoipd
Summary:        IPv4LL Service for Zeroconf and Bonjour
# Split provides for upgrade from openSUSE <= 12.3 and SLE <= 11.
# Disable this conflict for now, it breaks staging, and it's pretty much obsolete, but can go back in if needed once a new version of avahi is released.
# File conflict for avahi-autoipd openSUSE <= 12.3 SLE <= 11
#Conflicts:      avahi <= 0.6.31-9.2
# coreutils contains /usr/bin/chown
Group:          Productivity/Networking/Other
Requires(post): coreutils
%sysusers_requires
Provides:       avahi:%{_sbindir}/avahi-autoipd

%description autoipd
avahi-autoipd is an implementation of Dynamic Configuration of IPv4
Link-Local Addresses.

avahi-autoipd doesn't depend on any other Avahi library, hence it makes
sense to install it even if Avahi itself is not installed.

%package utils
Summary:        Command Line Utilities for the Zeroconf/Bonjour D-Bus service
Group:          Productivity/Networking/Other
Requires:       %{_name} >= %{version}

%description utils
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%package -n libavahi-devel
Summary:        Header files for the Zeroconf/Bonjour D-Bus service
Group:          Development/Libraries/C and C++
Requires:       dbus-1-devel
Requires:       glibc-devel
Requires:       libavahi-client%{avahi_client_sover} = %{version}
Requires:       libavahi-common%{avahi_common_sover} = %{version}
Requires:       libavahi-core%{avahi_core_sover} = %{version}
Requires:       libavahi-libevent%{avahi_libevent_sover} = %{version}
# Last appeared in OpenSUSE 10.3:
Provides:       avahi-devel = %{version}
Obsoletes:      avahi-devel < %{version}

%description -n libavahi-devel
Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.

%package compat-mDNSResponder-devel
Summary:        mDNSResponder Compatibility Package for the Zeroconf/Bonjour D-Bus service
Group:          Development/Libraries/C and C++
Requires:       libavahi-devel = %{version}
Requires:       libdns_sd = %{version}
Provides:       mDNSResponder-devel = 107.5
Obsoletes:      mDNSResponder-devel < 107.5

%description compat-mDNSResponder-devel
Apple mDNSResponder compatibility layer for Avahi.

Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.

%package compat-howl-devel
Summary:        Howl Compatibility Package for the Zeroconf/Bonjour D-Bus service
Group:          Development/Libraries/C and C++
Requires:       libavahi-devel = %{version}
Requires:       libhowl%{avahi_libhowl_sover} = %{version}

%description compat-howl-devel
Howl compatibility layer for Avahi.

Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.

%package -n libavahi-ui-gtk3-%{avahi_gtk3_sover}
Summary:        D-Bus Service for Zeroconf and Bonjour
Group:          System/Libraries

%description -n libavahi-ui-gtk3-%{avahi_gtk3_sover}
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%package -n libavahi-glib%{avahi_glib_sover}
Summary:        Glib Bindings for avahi, the D-Bus Service for Zeroconf and Bonjour
# Old name used for <= 10.3:
Group:          System/Libraries
Provides:       avahi-glib = %{version}
Obsoletes:      avahi-glib < %{version}

%description -n libavahi-glib%{avahi_glib_sover}
GLib support for Avahi.

Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.

%package -n libavahi-gobject%{avahi_gobject_sover}
Summary:        D-Bus Service for Zeroconf and Bonjour
Group:          System/Libraries

%description -n libavahi-gobject%{avahi_gobject_sover}
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%package -n typelib-1_0-Avahi-0_6
Summary:        Introspection bindings for the Zeroconf/Bonjour D-Bus service
Group:          System/Libraries

%description -n typelib-1_0-Avahi-0_6
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

This package provides the GObject Introspection bindings for Avahi.

%package -n avahi-utils-gtk
Summary:        GTK+ Utilities for the Zeroconf/Bonjour D-Bus service
Group:          Productivity/Networking/Other
Requires:       %{_name} >= %{version}
# Due to a mistake in the spec file build staging, this package had
# name avahi-glib2-utils-gtk in 11.1 and SLE11 and avahi-utils-gtk in
# all other products.
Provides:       avahi-glib2-utils-gtk = %{version}
Obsoletes:      avahi-glib2-utils-gtk < %{version}

%description -n avahi-utils-gtk
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.








# This is the avahi-discover command, only provided for the primary python3 flavor
%package -n python3-avahi-gtk
Summary:        A set of Avahi utilities written in Python Using python-gtk
Group:          Development/Languages/Python
Requires:       python3-avahi = %{version}
Requires:       python3-gobject
Requires(post): coreutils
Requires(postun):coreutils
Provides:       %{oldpython}-avahi-gtk = %{version}
Obsoletes:      %{oldpython}-avahi-gtk < %{version}
# Provide split-provides for update from <= 11.0:
Provides:       %{oldpython}-avahi:%{_bindir}/avahi-discover

%description -n python3-avahi-gtk
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%package -n libavahi-glib-devel
Summary:        Header files for Avahi's Glib bindings
Group:          Development/Libraries/C and C++
Requires:       libavahi-devel = %{version}
Requires:       libavahi-glib%{avahi_glib_sover} = %{version}
Requires:       libavahi-ui-gtk3-%{avahi_gtk3_sover} = %{version}
Requires:       typelib-1_0-Avahi-0_6 = %{version}
# Last appeared in OpenSUSE 10.3:
Provides:       avahi-devel:%{_libdir}/libavahi-glib.so

%description -n libavahi-glib-devel
GLib support for Avahi.

Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.

%package -n libavahi-gobject-devel
Summary:        Header files for Avahi's GObject bindings
Group:          System/Daemons
Requires:       glib2-devel
Requires:       libavahi-devel = %{version}
Requires:       libavahi-glib-devel
Requires:       libavahi-gobject%{avahi_gobject_sover} = %{version}

%description -n libavahi-gobject-devel
Avahi is an implementation of the DNS Service Discovery and Multicast
DNS specifications for Zeroconf Computing.

%if %{build_core}
%lang_package
%endif

%if %{build_qt5}
%package -n libavahi-qt5-%{avahi_qt5_sover}
Summary:        Qt5 Bindings for avahi, the D-Bus Service for Zeroconf and Bonjour
Group:          System/Libraries

%description -n libavahi-qt5-%{avahi_qt5_sover}
Qt5 support for Avahi.

Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.

%package -n libavahi-qt5-devel
Summary:        Header files for Avahi's Qt5 bindings
Group:          Development/Libraries/C and C++
Requires:       libavahi-devel = %{version}
Requires:       libavahi-qt5-%{avahi_qt5_sover} = %{version}

%description -n libavahi-qt5-devel
Development files for the Qt5 support for Avahi.

Avahi is an implementation of the DNS Service Discovery and Multicast DNS
specifications for Zeroconf Computing.
%endif

%prep
%setup -q -n %{_name}-%{version}
cp -a %{SOURCE5} sysconfig.avahi
sed "s:@docdir@:%{_docdir}:g" <%{SOURCE6} >sysconfig.avahi-autoipd
cp -a %{SOURCE9} avahi-autoipd/README.SUSE
sed "s:@sbindir@:%{_sbindir}:g" <%{SOURCE10} >avahi-autoipd/avahi-autoipd.if-up
sed "s:@sbindir@:%{_sbindir}:g" <%{SOURCE11} >avahi-autoipd/avahi-autoipd.if-down
sed -ie "s/libevent-[0-9\.]*/libevent/" avahi-libevent.pc.in
cp -a %{SOURCE12} service-type-database/build-db
%patch0
%patch1 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1

%if !%{build_core}
# Replace all .la references from local .la files to installed versions
# with exception of libavahi-glib.la.
# It allows to build only the binding subpackage.
sed -i 's:libavahi-glib\.la:@@SKIP LIBAVAHI GLIB@@:g
s:\(\.\.\|\$(top_builddir)\)/[^/]*/\(lib[^ ]*\.la\):%{_libdir}/\2:g
s:@@SKIP LIBAVAHI GLIB@@:libavahi-glib.la:g
' */Makefile.am
%endif
if ! test -f %{_datadir}/aclocal/glib-gettext.m4 ; then
    cat %{SOURCE4} >>acinclude.m4
fi

%build
%sysusers_generate_pre %{SOURCE13} avahi avahi.conf
%sysusers_generate_pre %{SOURCE14} autoipd avahi-autoipd.conf
autoreconf -f -i
intltoolize -f
%{python_expand # configure for every python flavor
export PYTHON=%{_bindir}/$python
%configure\
	--disable-static\
        --with-distro=suse\
        --enable-xmltoman\
        --with-dbus-sys=%{_datadir}/dbus-1/system.d \
%if %{build_core}
	--enable-compat-libdns_sd\
	--enable-compat-howl\
	--enable-libevent\
%else
	--disable-compat-libdns_sd\
	--disable-compat-howl\
	--disable-libevent\
%endif
%if %{build_glib2}
	--enable-glib\
	--enable-gobject\
	--disable-gtk\
	--enable-gtk3\
	--enable-pygobject\
%else
	--disable-glib\
	--disable-gobject\
	--disable-pygobject\
	--disable-gtk\
	--disable-gtk3\
%endif
	--disable-qt3\
	--disable-qt4\
	--disable-mono\
%if %{build_qt5}
	--enable-qt5\
%else
	--disable-qt5\
%endif
%ifarch ppc64 ppc64le s390x
    --disable-monodoc\
%endif
	--with-avahi-priv-access-group=avahi\
	--with-autoipd-user=avahi-autoipd\
	--with-autoipd-group=avahi-autoipd

cp -r avahi-python avahi-python-%{$python_bin_suffix}
}

%if %{build_glib2} && !%{build_core}
for DIR in avahi-glib avahi-gobject avahi-ui avahi-discover-standalone avahi-python man ; do
cd $DIR
%make_build
cd ..
done
%endif
%if %{build_core}
%{python_expand # build for every python flavor
cd avahi-python-%{$python_bin_suffix}
%make_build
cd ..
}
%endif
%make_build

%install
%if %{build_glib2} && !%{build_core}
for DIR in avahi-glib avahi-gobject avahi-ui avahi-discover-standalone avahi-python man ; do
cd $DIR
%make_install
cd ..
done
cd -
%endif
%if %{build_qt5} && !%{build_core}
cd avahi-qt
%endif
%make_install
# do not install sysv init scripts
rm -rf %{buildroot}%{_sysconfdir}/init.d/
# Do not install ssh and sftp services
rm -rf %{buildroot}%{_sysconfdir}/avahi/services/ssh.service
rm -rf %{buildroot}%{_sysconfdir}/avahi/services/sftp-ssh.service

%if !%{build_core}
cd ..
%make_build install-pkgconfigDATA DESTDIR=%{buildroot}
%endif
%if %{build_core}
%{python_expand # install for every python flavor
cd avahi-python-%{$python_bin_suffix}
%make_install
cd ..
}
%python_clone -a %{buildroot}%{_bindir}/avahi-bookmarks
%python_clone -a %{buildroot}%{_mandir}/man1/avahi-bookmarks.1
# do not remove this unless you plan to fix _all_ the references to
# it. all (multiple) previous attempts have failed already
#rm "%{buildroot}/%{_libdir}/libavahi-common.la"
install -d %{buildroot}/%{_localstatedir}/run/avahi-daemon
ln -s avahi-compat-libdns_sd/dns_sd.h %{buildroot}/%{_includedir}/
ln -s avahi-compat-howl.pc %{buildroot}/%{_libdir}/pkgconfig/howl.pc
install -d %{buildroot}/%{_prefix}/lib/avahi
install -d %{buildroot}%{_sysconfdir}/sysconfig/network/if-{up,down}.d
install avahi-autoipd/avahi-autoipd.if-up %{buildroot}%{_sysconfdir}/sysconfig/network/if-up.d/avahi-autoipd
install avahi-autoipd/avahi-autoipd.if-down %{buildroot}%{_sysconfdir}/sysconfig/network/if-down.d/avahi-autoipd
install -d %{buildroot}/%{_localstatedir}/lib/avahi-autoipd
mkdir -p %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcavahi-daemon
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcavahi-dnsconfd
install -d %{buildroot}/%{_datadir}/pixmaps
install -d %{buildroot}%{_fillupdir}
install -m 644 sysconfig.avahi* %{buildroot}%{_fillupdir}/
install -Dm0644 %{SOURCE13} %{buildroot}%{_sysusersdir}/avahi.conf
install -Dm0644 %{SOURCE14} %{buildroot}%{_sysusersdir}/avahi-autoipd.conf
%if ! %{build_glib2}
# Note: This file is intentionally installed here. It is needed for avahi-utils-gtk and python3-avahi-gtk:
install -d %{buildroot}/%{_datadir}/avahi/interfaces
install -m 644 avahi-discover-standalone/avahi-discover.ui %{buildroot}/%{_datadir}/avahi/interfaces
%endif
%find_lang %{name} %{?no_lang_C}
%else
# There is no simple way to not install core files. Remove them here.
# The rest is enabled/disabled in configure as needed.
rm %{buildroot}/%{_libdir}/pkgconfig/avahi-client.pc
rm %{buildroot}/%{_libdir}/pkgconfig/avahi-core.pc
%if %{build_glib2}
rm %{buildroot}/%{_bindir}/avahi-bookmarks
rm -r %{buildroot}/%{python3_sitelib}/avahi
rm %{buildroot}/%{_mandir}/man1/avahi-bookmarks.1*
rm %{buildroot}/%{_mandir}/man1/avahi-browse-domains.1*
rm %{buildroot}/%{_mandir}/man1/avahi-browse.1*
rm %{buildroot}/%{_mandir}/man1/avahi-publish-address.1*
rm %{buildroot}/%{_mandir}/man1/avahi-publish-service.1*
rm %{buildroot}/%{_mandir}/man1/avahi-publish.1*
rm %{buildroot}/%{_mandir}/man1/avahi-resolve-address.1*
rm %{buildroot}/%{_mandir}/man1/avahi-resolve-host-name.1*
rm %{buildroot}/%{_mandir}/man1/avahi-resolve.1*
rm %{buildroot}/%{_mandir}/man1/avahi-set-host-name.1*
rm %{buildroot}/%{_mandir}/man5/avahi-daemon.conf.5*
rm %{buildroot}/%{_mandir}/man5/avahi.hosts.5*
rm %{buildroot}/%{_mandir}/man5/avahi.service.5*
rm %{buildroot}/%{_mandir}/man8/avahi-autoipd.8*
rm %{buildroot}/%{_mandir}/man8/avahi-autoipd.action.8*
rm %{buildroot}/%{_mandir}/man8/avahi-daemon.8*
rm %{buildroot}/%{_mandir}/man8/avahi-dnsconfd.8*
rm %{buildroot}/%{_mandir}/man8/avahi-dnsconfd.action.8*
# Note: This file was intentionally moved to avahi. It is needed for avahi-utils-gtk and python3-avahi-gtk:
rm %{buildroot}/%{_datadir}/avahi/interfaces/avahi-discover.ui
rmdir %{buildroot}/%{_datadir}/avahi/interfaces
rmdir %{buildroot}/%{_datadir}/avahi
%endif
%endif
%if %{build_glib2}
%suse_update_desktop_file avahi-discover
%suse_update_desktop_file bvnc
%suse_update_desktop_file bssh
%endif
%fdupes %{buildroot}/%{_libdir}

%pre -f avahi.pre
%service_add_pre avahi-dnsconfd.service avahi-daemon.service
# bnc#853845,bnc#851953: do not start by default under
# sysconfig as this breaks vlan,bridge,bonding setups
# in pre to revert old default setting from template.
if test -f %{_fillupdir}/sysconfig.avahi-autoipd -a \
	-f etc/sysconfig/avahi ; then
	.  %{_fillupdir}/sysconfig.avahi-autoipd
	if test "X$AVAHI_AUTOIPD_ENABLE" = "Xyes" ; then
		sed -i etc/sysconfig/avahi \
		    -e 's/^\(AVAHI_AUTOIPD_ENABLE\)=.*/\1="no"/'
	fi
fi

%post
%{fillup_only -n avahi}
%{fillup_only -ns security checksig}
%service_add_post avahi-dnsconfd.service avahi-daemon.service

%preun
%service_del_preun avahi-dnsconfd.service avahi-daemon.service

%postun
%service_del_postun avahi-dnsconfd.service avahi-daemon.service

%pre autoipd -f autoipd.pre

%post autoipd
%{fillup_only -ns avahi autoipd}
# Change ownership of /var/lib/avahi-autoipd after upgrade from openSUSE <= 12.3 and SLE <= 11.
find %{_localstatedir}/lib/avahi-autoipd -user avahi -exec chown avahi-autoipd:avahi-autoipd {} +

%post -n libavahi-client%{avahi_client_sover} -p /sbin/ldconfig
%postun -n libavahi-client%{avahi_client_sover} -p /sbin/ldconfig
%post -n libavahi-common%{avahi_common_sover} -p /sbin/ldconfig
%postun -n libavahi-common%{avahi_common_sover} -p /sbin/ldconfig
%post -n libavahi-core%{avahi_core_sover} -p /sbin/ldconfig
%postun -n libavahi-core%{avahi_core_sover} -p /sbin/ldconfig
%post -n libavahi-libevent%{avahi_libevent_sover} -p /sbin/ldconfig
%postun -n libavahi-libevent%{avahi_libevent_sover} -p /sbin/ldconfig
%post -n libdns_sd -p /sbin/ldconfig
%postun -n libdns_sd -p /sbin/ldconfig
%post -n libhowl%{avahi_libhowl_sover} -p /sbin/ldconfig
%postun -n libhowl%{avahi_libhowl_sover} -p /sbin/ldconfig
%post -n libavahi-ui-gtk3-%{avahi_gtk3_sover} -p /sbin/ldconfig
%postun -n libavahi-ui-gtk3-%{avahi_gtk3_sover} -p /sbin/ldconfig
%post -n libavahi-gobject%{avahi_gobject_sover} -p /sbin/ldconfig
%postun -n libavahi-gobject%{avahi_gobject_sover} -p /sbin/ldconfig
%post -n libavahi-glib%{avahi_glib_sover} -p /sbin/ldconfig
%postun -n libavahi-glib%{avahi_glib_sover} -p /sbin/ldconfig
%if %{build_qt5}
%post -n libavahi-qt5-%{avahi_qt5_sover} -p /sbin/ldconfig
%postun -n libavahi-qt5-%{avahi_qt5_sover} -p /sbin/ldconfig
%endif

%post -n python3-avahi-gtk
%desktop_database_post

%postun -n python3-avahi-gtk
%desktop_database_post

%post -n avahi-utils-gtk
%desktop_database_post

%postun -n avahi-utils-gtk
%desktop_database_post

%if %{build_core}
%if 0%{?python_subpackage_only}
# this is rewritten by python_subpackages into the appropriate flavor
%post -n python-avahi
%python_install_alternative avahi-bookmarks avahi-bookmarks.1

%postun -n python-avahi
%python_uninstall_alternative avahi-bookmarks
%else

%post -n python3-avahi
%python_install_alternative avahi-bookmarks avahi-bookmarks.1

%postun -n python3-avahi
%python_uninstall_alternative avahi-bookmarks
%endif

%files
%license LICENSE
%doc docs/* avahi-daemon/sftp-ssh.service avahi-daemon/ssh.service
%dir %{_libdir}/avahi/
# Note: This file is intentionally packaged here. It is needed for python3-avahi and avahi-utils:
%{_libdir}/avahi/service-types.db
# avahi creates the directory itself, we do not package it
# since it might be on tmpfs
%attr(-,avahi,avahi) %ghost /run/avahi-daemon
%{_mandir}/man5/*.5%{ext_man}
%{_mandir}/man8/*.8%{ext_man}
%exclude %{_mandir}/man8/avahi-autoipd.8.*
%{_sbindir}/avahi-*
%exclude %{_sbindir}/avahi-autoipd
%{_sbindir}/rcavahi-daemon
%{_sbindir}/rcavahi-dnsconfd
%dir %{_sysconfdir}/avahi
%config %{_sysconfdir}/avahi/avahi-daemon.conf
%{_sysconfdir}/avahi/avahi-dnsconfd.action
%dir %{_sysconfdir}/avahi/services
%config(noreplace) %{_sysconfdir}/avahi/hosts
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.Avahi.*.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.Avahi.service
%dir %{_prefix}/lib/avahi
%{_unitdir}/avahi-daemon.service
%{_unitdir}/avahi-daemon.socket
%{_unitdir}/avahi-dnsconfd.service
%{_sysusersdir}/avahi.conf
# Common file for avahi-utils-gtk and python3-avahi-gtk:
%dir %{_datadir}/avahi/
%{_datadir}/avahi/interfaces
%{_fillupdir}/sysconfig.avahi

%files lang -f %{name}.lang

%files -n libavahi-client%{avahi_client_sover}
%{_libdir}/libavahi-client*.so.*

%files -n libavahi-common%{avahi_common_sover}
%{_libdir}/libavahi-common*.so.*

%files -n libavahi-core%{avahi_core_sover}
%{_libdir}/libavahi-core*.so.*

%files -n libavahi-libevent%{avahi_libevent_sover}
%{_libdir}/libavahi-libevent*.so.*

%files -n libdns_sd
# libdns_sd.so must be in non-devel package to provide mDNSResponder-lib compatibility:
%{_libdir}/libdns_sd.so
%{_libdir}/libdns_sd.so.*

%files -n libhowl%{avahi_libhowl_sover}
%{_libdir}/libhowl.so.*

%files %{python_files avahi}
%python_alternative %{_bindir}/avahi-bookmarks
%python_alternative %{_mandir}/man1/avahi-bookmarks.1%{ext_man}
%{python_sitelib}/avahi

%files autoipd
%doc avahi-autoipd/README.SUSE
%{_mandir}/man8/avahi-autoipd.8%{ext_man}
%attr(-,avahi-autoipd,avahi-autoipd)%{_localstatedir}/lib/avahi-autoipd
%{_sbindir}/avahi-autoipd
%{_sysconfdir}/avahi/avahi-autoipd.action
%dir %{_sysconfdir}/sysconfig/network
%dir %{_sysconfdir}/sysconfig/network/if-{down,up}.d
%{_sysconfdir}/sysconfig/network/*/avahi-autoipd
%{_fillupdir}/sysconfig.avahi-autoipd
%{_sysusersdir}/avahi-autoipd.conf

%files utils
%{_bindir}/avahi-browse*
%{_bindir}/avahi-publish*
%{_bindir}/avahi-resolve*
%{_bindir}/avahi-set-host-name
%dir %{_datadir}/avahi/
%{_datadir}/avahi/avahi-service.dtd
%{_mandir}/man1/avahi-browse*.1*
%{_mandir}/man1/avahi-publish*.1*
%{_mandir}/man1/avahi-resolve*.1*
%{_mandir}/man1/avahi-set-host-name.1*

%files -n libavahi-devel
# FIXME: Maybe split to particular subpackages.
#%doc doc/api/html
#%doc doc/*.html doc/*.txt doc/file-boilerplate.c doc/TODO
%{_includedir}/avahi-client
%{_includedir}/avahi-common
%{_includedir}/avahi-core
%{_includedir}/avahi-libevent
# avahi devel files
%{_libdir}/libavahi-client.*a
%{_libdir}/libavahi-client*.so
%{_libdir}/libavahi-core.*a
%{_libdir}/libavahi-core*.so
%{_libdir}/libavahi-common*.so
# do not remove unless you fix the resulting problems
# reference is in libavahi-client.la
%{_libdir}/libavahi-common*.*a
%{_libdir}/libavahi-libevent.*a
%{_libdir}/libavahi-libevent*.so
%{_libdir}/pkgconfig/avahi-client.pc
%{_libdir}/pkgconfig/avahi-core.pc
%{_libdir}/pkgconfig/avahi-libevent.pc

%files compat-mDNSResponder-devel
%{_includedir}/avahi-compat-libdns_sd
%{_includedir}/dns_sd.h
%{_libdir}/libdns_sd.*a
%{_libdir}/pkgconfig/avahi-compat-libdns_sd.pc

%files compat-howl-devel
%{_includedir}/avahi-compat-howl
%{_libdir}/libhowl.so
%{_libdir}/libhowl.*a
%{_libdir}/pkgconfig/avahi-compat-howl.pc
%{_libdir}/pkgconfig/howl.pc
%endif

%if %{build_glib2}
%files -n libavahi-ui-gtk3-%{avahi_gtk3_sover}
%{_libdir}/libavahi-ui-gtk3.so.%{avahi_gtk3_sover}*

%files -n libavahi-glib%{avahi_glib_sover}
%{_libdir}/libavahi-glib*.so.*

%files -n libavahi-gobject%{avahi_gobject_sover}
%{_libdir}/libavahi-gobject*.so.*

%files -n typelib-1_0-Avahi-0_6
%{_libdir}/girepository-1.0/Avahi-0.6.typelib
%{_libdir}/girepository-1.0/AvahiCore-0.6.typelib

%files -n python3-avahi-gtk
%{_bindir}/avahi-discover
%{_datadir}/applications/avahi-discover.desktop
%{_mandir}/man1/avahi-discover.1*

%files -n avahi-utils-gtk
%{_bindir}/bshell
%{_bindir}/bssh
%{_bindir}/bvnc
%{_bindir}/avahi-discover-standalone
%{_datadir}/applications/bssh.desktop
%{_datadir}/applications/bvnc.desktop
%{_mandir}/man1/bshell.1*
%{_mandir}/man1/bssh.1*
%{_mandir}/man1/bvnc.1*

%files -n libavahi-glib-devel
%{_includedir}/avahi-glib
%{_includedir}/avahi-ui
%{_libdir}/libavahi-glib*.*a
%{_libdir}/libavahi-glib*.so
%{_libdir}/libavahi-ui*.*a
%{_libdir}/libavahi-ui*.*so
%{_libdir}/pkgconfig/avahi-glib.pc
%{_libdir}/pkgconfig/avahi-ui-gtk3.pc

%files -n libavahi-gobject-devel
%{_includedir}/avahi-gobject
%{_libdir}/libavahi-gobject*.*a
%{_libdir}/libavahi-gobject*.so
%{_libdir}/pkgconfig/avahi-gobject.pc
%{_datadir}/gir-1.0/*.gir
%endif

%if %{build_qt5}
%files -n libavahi-qt5-%{avahi_qt5_sover}
%{_libdir}/libavahi-qt5.so.*

%files -n libavahi-qt5-devel
%{_includedir}/avahi-qt5
%{_libdir}/libavahi-qt5.*a
%{_libdir}/libavahi-qt5.so
%{_libdir}/pkgconfig/avahi-qt5.pc
%endif

%changelog
