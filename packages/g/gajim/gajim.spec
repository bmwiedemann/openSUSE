#
# spec file for package gajim
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


#
# Gajim uses libsoup2 while GUPnP, libsoup3. And that makes the app unlunchable.
# This is a temporary fix until upstream addresses it.
#
# FIXME: Once the issue https://dev.gajim.org/gajim/gajim/-/issues/11183
#        is properly addressed, exclude only AppIndicator3.
#
%define __requires_exclude ^typelib\\((GUPnPIgd|AppIndicator3)\\).*$
#
# It was: __requires_exclude ^typelib\\(AppIndicator3\\)

%if 0%{?suse_version} > 1500
%define py3ver 3
%define py3pkg python3
%define py3pkg_sitelib %{python3_sitelib}
%else
# Requires at least python 3.9
%define py3ver 3.10
%define py3pkg python310
%define py3pkg_sitelib %{_prefix}/lib/python%{py3ver}/site-packages
%endif
Name:           gajim
Version:        1.5.4
Release:        0
Summary:        XMPP client written in Python and Gtk
License:        GPL-3.0-only
Group:          Productivity/Networking/Talk/Clients
URL:            https://gajim.org/
Source:         https://gajim.org/downloads/1.5/gajim-%{version}.tar.gz
BuildRequires:  %{py3pkg}-nbxmpp >= 3.2.4
BuildRequires:  %{py3pkg}-precis-i18n >= 1.0.0
BuildRequires:  %{py3pkg}-setuptools
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpcre1
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Requires:       %{py3pkg}-Pillow
Requires:       %{py3pkg}-base
Requires:       %{py3pkg}-cryptography >= 3.4.8
Requires:       %{py3pkg}-css-parser
Requires:       %{py3pkg}-gobject-Gdk
Requires:       %{py3pkg}-gobject-cairo
Requires:       %{py3pkg}-gssapi
Requires:       %{py3pkg}-keyring
Requires:       %{py3pkg}-nbxmpp >= 3.2.5
Requires:       %{py3pkg}-precis-i18n >= 1.0.0
Requires:       %{py3pkg}-pycairo >= 1.16.0
Requires:       ca-certificates-mozilla
Requires:       typelib(GtkSource) = 4
Requires:       typelib(Soup) = 2.4
# gajim-remote
Recommends:     %{py3pkg}-dbus-python
# OMEMO encryption
Recommends:     gajim-plugin-omemo
Recommends:     %{py3pkg}-axolotl
BuildArch:      noarch

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
sed -i '1{/\/usr\/bin\/*/d;}' gajim/gajim_remote.py

%build
python%{py3ver} setup.py build

%install
python%{py3ver} setup.py install \
  --root=%{buildroot} --prefix=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/
mv %{buildroot}{%{py3pkg_sitelib}/%{name}/data,%{_datadir}/%{name}}/
ln -s %{_datadir}/%{name} %{buildroot}%{py3pkg_sitelib}/%{name}/data

# The plugins subdirectory must be owned by the package.
mkdir %{buildroot}%{_datadir}/%{name}/plugins/

%suse_update_desktop_file -r org.gajim.Gajim Network InstantMessaging
%fdupes %{buildroot}%{_prefix}/
%find_lang %{name}

%files
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{py3pkg_sitelib}/%{name}/
%{py3pkg_sitelib}/%{name}-*
%{_datadir}/applications/*%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/*%{name}*.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*%{name}*.appdata.xml
%{_mandir}/man?/%{name}*%{?ext_man}

%files lang -f %{name}.lang

%changelog
