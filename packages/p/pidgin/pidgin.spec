#
# spec file for package pidgin
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _name   Pidgin
Name:           pidgin
Version:        2.13.0
Release:        0
Summary:        Multiprotocol Instant Messaging Client
License:        GPL-2.0-only
Group:          Productivity/Networking/Instant Messenger
URL:            https://pidgin.im/
Source:         http://downloads.sf.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://downloads.sf.net/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        pidgin.keyring
Source3:        pidgin-prefs.xml
# PATCH-FIX-OPENSUSE pidgin-nonblock-common.patch
Patch0:         pidgin-nonblock-common.patch
# PATCH-FIX-OPENSUSE pidgin-nonblock-gwim.patch
Patch1:         pidgin-nonblock-gwim.patch
# PATCH-FIX-OPENSUSE pidgin-fix-perl-build.patch vuntz@opensuse.org -- Revert https://bitbucket.org/pidgin/main/commits/a083625 as it breaks the build.
Patch2:         pidgin-fix-perl-build.patch
# PATCH-FIX-UPSTREAM pidgin-ncurses-6.0-accessors.patch pidgin.im#16764 dimstar@opensuse.org -- Fix build with NCurses 6.0 with WINDOW_OPAQUE set to 1.
Patch3:         pidgin-ncurses-6.0-accessors.patch
# PATCH-FIX-SLE pidgin-use-default-alsa.patch bsc#886670 tiwai@suse.de -- Use ALSA as a default for avoiding broken volume control.
Patch4:         pidgin-use-default-alsa.patch
# PATCH-FIX-UPSTREAM pidgin-enable-sni-gnutls.patch bsc#1086439 pidgin.im#17300 fezhang@suse.com -- Enable SNI extension in GnuTLS connections.
Patch5:         pidgin-enable-sni-gnutls.patch
# PATCH-FIX-UPSTREAM pidgin-Leaky-deprecation-clean-ups.patch pidgin.im#17415 fezhang@suse.com -- Fix warnings of deprecation of GParameter
Patch6:         pidgin-Leaky-deprecation-clean-ups.patch
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
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
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
Requires:       perl-base >= %{perl_version}
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120200 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse})
BuildRequires:  pkgconfig(farstream-0.2) >= 0.2.7
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
Recommends:     gstreamer-plugins-good
%else
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-interfaces-0.10)
Recommends:     gstreamer-0_10-plugins-good
%endif
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
Group:          Development/Libraries/C and C++
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
Group:          System/Libraries
Requires:       ca-certificates-mozilla
# Not really required, but standard XMPP accounts require it, if compiled with SASL support.
Requires:       cyrus-sasl-digestmd5
Requires:       cyrus-sasl-plain
Requires:       libpurple-branding
Requires:       perl >= %{perl_version}
Recommends:     libpurple-lang
# Needed for purple-url-handler.
%if 0%{?suse_version} >= 1500
Requires:       python3-dbus-python
%else
Requires:       dbus-1-python3
%endif

%description -n libpurple
libpurple is a library intended to be used by programmers seeking
to write an IM client that connects to many IM networks.

libpurple is compatible with the following chat networks out of the
box: Jabber/XMPP, AIM, ICQ, Bonjour, Gadu-Gadu, IRC, SILC, SIMPLE,
Novell GroupWise Messenger, IBM Sametime, and Zephyr. It can
support many more with plugins.

%lang_package -n libpurple

%package -n libpurple-branding-upstream
Summary:        GLib-based Instant Messenger Library -- Upstream default configuration
Group:          System/Libraries
Requires:       libpurple = %{version}
Supplements:    packageand(libpurple:branding-upstream)
Conflicts:      otherproviders(libpurple-branding)
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
Group:          Development/Libraries/C and C++
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
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple = %{version}
Supplements:    packageand(libpurple:tcl)

%description -n libpurple-tcl
TCL plugin loader for Pidgin. This package will allow you to write
or use Pidgin plugins written in the TCL programming language.

%package -n libpurple-plugin-sametime
Summary:        Sametime Plugin for Pidgin using the Meanwhile Library
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple = %{version}
# libpurple-meanwhile was last used in openSUSE Leap 42.2.
Provides:       libpurple-meanwhile = %{version}
Obsoletes:      libpurple-meanwhile < %{version}

%description -n libpurple-plugin-sametime
IBM Sametime plugin for Pidgin using the Meanwhile library.

%package -n finch
Summary:        Text-Based User Interface for Pidgin Instant Messaging Client
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple = %{version}

%description -n finch
A text-based user interface to use with libpurple. This can be run
from a standard text console or from a graphical terminal emulator.
It uses ncurses and our homegrown gnt library for drawing windows
and text.

%package -n finch-devel
Summary:        Headers etc. for finch Stuffs
Group:          Development/Libraries/C and C++
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
translation-update-upstream
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if 0%{?sle_version} >= 120000 && !0%{?is_opensuse}
%patch4 -p1
%endif
%patch5 -p1
%patch6 -p1

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
  --enable-plugins \
  --enable-cyrus-sasl \
  --enable-dbus \
  --enable-gstreamer \
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120200
  --with-gstreamer=1.0 \
  --enable-vv \
%else
  --with-gstreamer=0.10 \
  --disable-vv \
%endif
  --disable-nm \
  --enable-dbus \
  --enable-devhelp \
  --with-tclconfig=%{_libdir} \
  --with-tkconfig=%{_libdir} \
  --with-system-ssl-certs=%{_sysconfdir}/ssl/certs/
make %{?_smp_mflags} V=1

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

%post -n finch -p /sbin/ldconfig

%postun -n finch -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS COPYRIGHT ChangeLog README doc/the_penguin.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/sounds/purple/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/%{name}/
%dir %{_datadir}/appdata/
%{_datadir}/appdata/pidgin.appdata.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

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
%{_libdir}/libpurple.so.*
%{_libdir}/libpurple-client.so.*
%{_libdir}/purple-2/
%exclude %{_libdir}/purple-2/libjabber.so
%exclude %{_libdir}/purple-2/liboscar.so
%exclude %{_libdir}/purple-2/libsametime.so
%exclude %{_libdir}/purple-2/tcl.so

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
%{_libdir}/purple-2/liboscar.so
%{_libdir}/pkgconfig/purple.pc
%{_mandir}/man3/Purple.3pm%{?ext_man}

%files -n finch
%{_bindir}/finch
%{_libdir}/finch/
%{_libdir}/libgnt.so.*
%{_libdir}/gnt/
%dir %{_libdir}/finch/
%{_mandir}/man1/finch.1%{?ext_man}

%files -n finch-devel
%{_includedir}/finch/
%{_includedir}/gnt/
%{_libdir}/libgnt.so
%{_libdir}/pkgconfig/finch.pc
%{_libdir}/pkgconfig/gnt.pc

%changelog
