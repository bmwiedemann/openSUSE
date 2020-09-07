#
# spec file for package gajim
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gajim
Version:        1.2.2
Release:        0
Summary:        XMPP client written in Python and Gtk3
License:        GPL-3.0-only
Group:          Productivity/Networking/Talk/Clients
URL:            https://gajim.org/
Source:         https://gajim.org/downloads/1.2/gajim-%{version}.tar.gz
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.5.0
BuildRequires:  python3-nbxmpp >= 0.6.10
BuildRequires:  python3-precis-i18n >= 1.0.0
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       ca-certificates-mozilla
Requires:       python3 >= 3.5.0
Requires:       python3-css-parser
Requires:       python3-docutils
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-nbxmpp >= 1.0.2
Requires:       python3-precis-i18n >= 1.0.0
Requires:       python3-pyOpenSSL >= 16.2
Requires:       python3-pycairo >= 1.16.0
Requires:       python3-pycurl
Requires:       python3-xml
Recommends:     %{name}-lang
# OMEMO encryption
Recommends:     gajim-plugin-omemo
Recommends:     python3-axolotl
# End-to-end encryption.
Recommends:     python3-pycrypto
# zeroconf support.
Suggests:       dbus-1-glib
# Idle module.
Suggests:       libXss1
BuildArch:      noarch
%if 0%{?suse_version} >= 1500
Requires:       python3-Pillow
Requires:       python3-dbus-python
Requires:       python3-keyring
# GPG encryption.
Recommends:     python3-python-gnupg
%else
Requires:       dbus-1-python3
# WebP avatars.
Recommends:     python3-Pillow
# GPG encryption.
Recommends:     python3-gnupg
# Password storage.
Recommends:     python3-keyring
%endif

%description
Gajim is a Jabber/XMPP client. It works with MATE and GNOME, but does
require neither to run.

Features:
 * Tabbed chat window and single window modes.
 * Group chat support (with Multi-User Chat protocol), invitation,
   chat to group chat transformation, minimise group chat to roster.
 * Emoticons, avatars, PEP (user activity, mood and tune).
 * Audio / video conferences.
 * File transfer, room bookmarks.
 * Metacontacts support.
 * Trayicon, speller, extended chat history functionalities.
 * TLS, GPG and End-To-End encryption support (with SSL legacy support).
 * Transport registration support.
 * Service discovery including nodes, user search.
 * Wikipedia, dictionary and search engine lookup.
 * Multiple accounts support.
 * DBus capabilities. Read more information.
 * XML console.
 * Link local (bonjour / zeroconf), BOSH.
 * Other features via plugins.

%lang_package

%prep
%setup -q
sed -i '/^Keywords/d' data/org.gajim.Gajim.desktop.in

# FIXME: Some leftover.
rm gajim/data/plugins/plugin_installer/config_dialog.ui~

%build
python3 setup.py build

%install
python3 setup.py install \
  --root=%{buildroot} --prefix=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/
mv %{buildroot}{%{python3_sitelib}/%{name}/data,%{_datadir}/%{name}}/
ln -s %{_datadir}/%{name} %{buildroot}%{python3_sitelib}/%{name}/data

%suse_update_desktop_file -r org.gajim.Gajim Network InstantMessaging
%fdupes %{buildroot}%{_prefix}/
%find_lang %{name}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*
%{_datadir}/applications/*%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/*%{name}*.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*%{name}*.appdata.xml
%{_mandir}/man?/%{name}*%{?ext_man}

%files lang -f %{name}.lang

%changelog
