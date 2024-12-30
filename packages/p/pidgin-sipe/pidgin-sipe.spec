#
# spec file for package pidgin-sipe
#
# Copyright (c) 2024 SUSE LLC
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


Name:           pidgin-sipe
Version:        1.25.0
Release:        0
Summary:        Pidgin protocol plugin to connect to MS Skype for Business
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://sipe.sourceforge.io/
Source:         http://downloads.sf.net/sipe/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE 0001-Fix-test-failures-with-appstream-1.0.patch christophe@krop.fr -- Fix test failures with appstream 1.0.
Patch0:         0001-Fix-test-failures-with-appstream-1.0.patch
# PATCH-FIX-OPENSUSE pidgin-sipe-fix-pointer-types.patch -- Fix pointer types.
Patch1:         pidgin-sipe-fix-pointer-types.patch
BuildRequires:  AppStream
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pidgin
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(freerdp-shadow2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-rtp-1.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(nice) >= 0.1.13
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(purple) >= 2.0.12
BuildRequires:  pkgconfig(telepathy-glib) >= 0.24.0
Recommends:     freerdp
Recommends:     remmina

%description
A third-party plugin for the Pidgin multi-protocol instant
messenger. It implements the extended version of SIP/SIMPLE used by
various products:
 * Skype for Business.
 * Microsoft Office 365.
 * Microsoft Business Productivity Online Suite (BPOS).
 * Microsoft Lync Server.
 * Microsoft Office Communications Server (OCS 2007/2007 R2).
 * Microsoft Live Communications Server (LCS 2003/2005).
 * Reuters Messaging.

With this plugin you should be able to replace your
Skype for Business client with Pidgin.

%package -n pidgin-plugin-sipe
Summary:        Pidgin protocol plugin to connect to MS Skype for Business
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-sipe = %{version}
%requires_ge    pidgin
Supplements:    (libpurple-plugin-sipe and pidgin)
# pidgin-sipe was last used in openSUSE Leap 42.2.
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
BuildArch:      noarch

%description -n pidgin-plugin-sipe
A third-party plugin for the Pidgin multi-protocol instant
messenger. It implements the extended version of SIP/SIMPLE used by
various products:
 * Skype for Business.
 * Microsoft Office 365.
 * Microsoft Business Productivity Online Suite (BPOS).
 * Microsoft Lync Server.
 * Microsoft Office Communications Server (OCS 2007/2007 R2).
 * Microsoft Live Communications Server (LCS 2003/2005).
 * Reuters Messaging.

With this plugin you should be able to replace your
Skype for Business client with Pidgin.

This package provides the icon set for Pidgin.

%package -n libpurple-plugin-sipe
Summary:        Libpurple third-party plugin for MS Skype for Business
Group:          Productivity/Networking/Instant Messenger
Recommends:     libpurple-plugin-sipe-lang
Enhances:       libpurple

%description -n libpurple-plugin-sipe
A third-party plugin for the libpurple multi-protocol instant
messaging library. It implements the extended version of SIP/SIMPLE
used by various products:
 * Skype for Business.
 * Microsoft Office 365.
 * Microsoft Business Productivity Online Suite (BPOS).
 * Microsoft Lync Server.
 * Microsoft Office Communications Server (OCS 2007/2007 R2).
 * Microsoft Live Communications Server (LCS 2003/2005).
 * Reuters Messaging.

%lang_package -n libpurple-plugin-sipe

%package -n telepathy-sipe
Summary:        MS Skype for Business connection manager for Telepathy
Group:          Productivity/Networking/Instant Messenger
# telepathy-plugin-sipe was last used in openSUSE Leap 42.2.
Provides:       telepathy-plugin-sipe = %{version}
Obsoletes:      telepathy-plugin-sipe < %{version}

%description -n telepathy-sipe
A third-party connection manager for the telepathy multi-protocol
instant messaging core. It implements the extended version of
SIP/SIMPLE used by various products:
 * Skype for Business.
 * Microsoft Office 365.
 * Microsoft Business Productivity Online Suite (BPOS).
 * Microsoft Lync Server.
 * Microsoft Office Communications Server (OCS 2007/2007 R2).
 * Microsoft Live Communications Server (LCS 2003/2005).
 * Reuters Messaging.

%prep
%autosetup -p1

%build
%configure \
  --disable-quality-check \
  --with-krb5             \
  --with-vv               \
  --with-appstream        \
  --enable-purple         \
  --enable-telepathy
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%check
%make_build check

%files -n pidgin-plugin-sipe
%license COPYING
%doc AUTHORS ChangeLog README TODO
%dir %{_datadir}/pixmaps/pidgin/
%dir %{_datadir}/pixmaps/pidgin/protocols/
%dir %{_datadir}/pixmaps/pidgin/protocols/*/
%{_datadir}/pixmaps/pidgin/protocols/*/sipe.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/pidgin-sipe.metainfo.xml

%files -n libpurple-plugin-sipe
%{_libdir}/purple-2/libsipe.so

%files -n libpurple-plugin-sipe-lang -f %{name}.lang

%files -n telepathy-sipe
%{_libexecdir}/telepathy-sipe
%{_datadir}/telepathy/
%{_datadir}/empathy/
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.sipe.service

%changelog
