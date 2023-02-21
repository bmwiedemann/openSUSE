#
# spec file for package pidgin
#
# Copyright (c) 2023 SUSE LLC
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


%define _name   Pidgin
%define sover   0
Name:           pidgin
Version:        2.14.12
Release:        0
Summary:        Multiprotocol Instant Messaging Client
License:        GPL-2.0-only
URL:            https://pidgin.im/
Source:         https://downloads.sf.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://downloads.sf.net/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        pidgin.keyring
Source3:        pidgin-prefs.xml
# PATCH-FIX-OPENSUSE pidgin-nonblock-common.patch
Patch0:         pidgin-nonblock-common.patch
# PATCH-FIX-OPENSUSE pidgin-nonblock-gwim.patch
Patch1:         pidgin-nonblock-gwim.patch
# PATCH-FIX-OPENSUSE pidgin-fix-perl-build.patch vuntz@opensuse.org -- Revert https://bitbucket.org/pidgin/main/commits/a083625 as it breaks the build.
Patch2:         pidgin-fix-perl-build.patch
# PATCH-FIX-SLE pidgin-use-default-alsa.patch bsc#886670 tiwai@suse.de -- Use ALSA as a default for avoiding broken volume control.
Patch3:         pidgin-use-default-alsa.patch
# PATCH-FIX-OPENSUSE pidgin-always-enable-intltool.patch mgorse@suse.com -- always enable intltool, needed for autoconf 2.71.
Patch4:         pidgin-always-enable-intltool.patch
BuildRequires:  ca-certificates-mozilla
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(farstream-0.2) >= 0.2.7
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnt) >= 2.14.0
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkspell-2.0)
BuildRequires:  pkgconfig(libgadu)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libnotify)
# Can use external libzephyr.
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(meanwhile)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
Requires:       ca-certificates-mozilla
Requires:       libpurple = %{version}
Requires:       perl-base >= %{perl_version}
Recommends:     gstreamer-plugins-good
%if 0%{?suse_version} >= 1500 && !0%{?is_opensuse}
Recommends:     purple-import-empathy
%endif

%description
Pidgin is a messaging application which lets you log in to accounts
on multiple chat networks simultaneously.

Pidgin is compatible with the following chat networks out of the
box: Jabber/XMPP, AIM, ICQ, Bonjour, Gadu-Gadu, IRC, SILC, SIMPLE,
Novell GroupWise Messenger, IBM Sametime, and Zephyr. It can
support many more with plugins.

%package devel
Summary:        Development Headers, Documentation, and Libraries for Pidgin
Requires:       %{name} = %{version}
Requires:       libpurple-devel = %{version}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk+-2.0)

%description devel
The pidgin-devel package contains the header files, developer
documentation, and libraries required for development of Pidgin scripts
and plugins.

%package -n libpurple
Summary:        GLib-based Instant Messenger Library
Requires:       ca-certificates-mozilla
# Not really required, but standard XMPP accounts require it, if compiled with SASL support.
Requires:       cyrus-sasl-digestmd5
Requires:       cyrus-sasl-plain
Requires:       libpurple%{sover} = %{version}
Requires:       libpurple-branding
Requires:       libpurple-client%{sover} = %{version}
Requires:       perl >= %{perl_version}
# Needed for purple-url-handler.
Requires:       python3-dbus-python

%description -n libpurple
libpurple is a library intended to be used by programmers seeking
to write an IM client that connects to many IM networks.

libpurple is compatible with the following chat networks out of the
box: Jabber/XMPP, AIM, ICQ, Bonjour, Gadu-Gadu, IRC, SILC, SIMPLE,
Novell GroupWise Messenger, IBM Sametime, and Zephyr. It can
support many more with plugins.

%lang_package -n libpurple

%package -n libpurple%{sover}
Summary:        GLib-based Instant Messenger Library

%description -n libpurple%{sover}
libpurple is a library intended to be used by programmers seeking
to write an IM client that connects to many IM networks.

This package provides the core libpurple library.

%package -n libpurple-client%{sover}
Summary:        GLib-based Instant Messenger Library

%description -n libpurple-client%{sover}
libpurple is a library intended to be used by programmers seeking
to write an IM client that connects to many IM networks.

This package provides the core libpurple client library.

%package -n libpurple-branding-upstream
Summary:        GLib-based Instant Messenger Library -- Upstream default configuration
Requires:       libpurple = %{version}
Supplements:    (libpurple and branding-upstream)
Conflicts:      libpurple-branding
Provides:       libpurple-branding = %{version}
BuildArch:      noarch
#BRAND: Provides /etc/purple/prefs.xml, the default configuration for
#BRAND: libpurple, and libpurple-based clients.

%description -n libpurple-branding-upstream
libpurple is a library intended to be used by programmers seeking
to write an IM client that connects to many IM networks.

libpurple is compatible with the following chat networks out of the
box: Jabber/XMPP, AIM, ICQ, Bonjour, Gadu-Gadu, IRC, SILC, SIMPLE,
Novell GroupWise Messenger, IBM Sametime, and Zephyr. It can
support many more with plugins.

This package provides the upstream default configuration for Pidgin.

%package -n libpurple-devel
Summary:        Development Headers, Documentation, and Libraries for libpurple
Requires:       libpurple = %{version}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libxml-2.0)

%description -n libpurple-devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple
based instant messaging clients or plugins for any libpurple based
client.

%package -n libpurple-tcl
Summary:        TCL Plugin Support for Pidgin
Requires:       libpurple = %{version}
Supplements:    (libpurple and tcl)

%description -n libpurple-tcl
TCL plugin loader for Pidgin. This package will allow you to write
or use Pidgin plugins written in the TCL programming language.

%package -n libpurple-plugin-sametime
Summary:        Sametime Plugin for Pidgin using the Meanwhile Library
Requires:       libpurple = %{version}
# libpurple-meanwhile was last used in openSUSE Leap 42.2.
Provides:       libpurple-meanwhile = %{version}
Obsoletes:      libpurple-meanwhile < %{version}

%description -n libpurple-plugin-sametime
IBM Sametime plugin for Pidgin using the Meanwhile library.

%package -n finch
Summary:        Text-Based User Interface for Pidgin Instant Messaging Client
Requires:       libpurple = %{version}

%description -n finch
A text-based user interface to use with libpurple. This can be run
from a standard text console or from a graphical terminal emulator.
It uses ncurses and our homegrown gnt library for drawing windows
and text.

%package -n finch-devel
Summary:        Headers etc. for finch Stuffs
Requires:       finch = %{version}
Requires:       glibc-devel
Requires:       libpurple-devel = %{version}
Requires:       ncurses-devel
Requires:       pkgconfig(glib-2.0)

%description -n finch-devel
The finch-devel package contains the header files, developer
documentation, and libraries required for development of Finch
scripts and plugins.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if 0%{?sle_version} >= 120000 && !0%{?is_opensuse}
%patch3 -p1
%endif
%patch4 -p1

cp -f %{SOURCE3} %{name}-prefs.xml

# Change Myanmar/Myanmar to Myanmar.
mv po/my_MM.po po/my.po
sed -i "/ALL_LINGUAS/s/ my_MM / my /" configure.ac

# Do not use env for python sripts.
sed -i '/^#!/s|env python$|python3|' libpurple/purple-*

%build
export CFLAGS="%{optflags} -fstack-protector -fPIC"
export CXXFLAGS="%{optflags} -fstack-protector -fPIC"
export FFLAGS="%{optflags} -fstack-protector -fPIC"
export LDFLAGS="-pie"
export PYTHON=python3
autoreconf -fi
%configure \
  --disable-static \
  --disable-gevolution \
  --enable-plugins \
  --enable-cyrus-sasl \
  --enable-dbus \
  --enable-gstreamer \
  --with-gstreamer=1.0 \
  --enable-vv \
  --disable-nm \
  --enable-dbus \
  --enable-devhelp \
  --with-tclconfig=%{_libdir} \
  --with-tkconfig=%{_libdir} \
  --with-system-ssl-certs=%{_sysconfdir}/ssl/certs/
%make_build

%install
%make_install

install -Dpm 0644 %{name}-prefs.xml %{buildroot}%{_sysconfdir}/purple/prefs.xml
%perl_process_packlist

find %{buildroot} -type f -name "perllocal.pod" -delete -print
find %{buildroot} -type f -name ".packlist" -delete -print
find %{buildroot} -type f -name "*.bs" -empty -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}
%suse_update_desktop_file -N %{_name} -G "Instant Messenger" %{name}
%find_lang %{name} %{?no_lang_C}

%post -n libpurple -p /sbin/ldconfig
%postun -n libpurple -p /sbin/ldconfig
%post -n libpurple%{sover} -p /sbin/ldconfig
%postun -n libpurple%{sover} -p /sbin/ldconfig
%post -n libpurple-client%{sover} -p /sbin/ldconfig
%postun -n libpurple-client%{sover} -p /sbin/ldconfig
%post -n finch -p /sbin/ldconfig
%postun -n finch -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS COPYRIGHT ChangeLog README doc/the_penguin.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/sounds/purple/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/%{name}/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/metainfo/pidgin.appdata.xml

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{_name}.3*%{?ext_man}

%files -n libpurple
%dir %{_sysconfdir}/purple/
%{_bindir}/purple-client-example
%{_bindir}/purple-remote
%{_bindir}/purple-send
%{_bindir}/purple-send-async
%{_bindir}/purple-url-handler
%{_libdir}/purple-2/
%exclude %{_libdir}/purple-2/libjabber.so
%exclude %{_libdir}/purple-2/libsametime.so
%exclude %{_libdir}/purple-2/tcl.so

%files -n libpurple0
%{_libdir}/libpurple.so.*

%files -n libpurple-client0
%{_libdir}/libpurple-client.so.*

%files -n libpurple-lang -f %{name}.lang

%files -n libpurple-branding-upstream
%config %{_sysconfdir}/purple/prefs.xml

%files -n libpurple-tcl
%{_libdir}/purple-2/tcl.so

%files -n libpurple-plugin-sametime
%{_libdir}/purple-2/libsametime.so

%files -n libpurple-devel
%doc ChangeLog.API HACKING PLUGIN_HOWTO
%doc libpurple/purple-notifications-example
%{_includedir}/libpurple/
%{_datadir}/aclocal/purple.m4
%{_libdir}/libpurple.so
%{_libdir}/libpurple-client.so
%{_libdir}/purple-2/libjabber.so
%{_libdir}/pkgconfig/purple.pc
%{_mandir}/man3/Purple.3pm%{?ext_man}

%files -n finch
%{_bindir}/finch
%{_libdir}/finch/
%dir %{_libdir}/finch/
%{_mandir}/man1/finch.1%{?ext_man}

%files -n finch-devel
%{_includedir}/finch/
%{_libdir}/pkgconfig/finch.pc

%changelog
