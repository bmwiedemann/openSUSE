#
# spec file for package gajim
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


%define __requires_exclude ^typelib\\(AppIndicator3\\).*$
%if 0%{?suse_version} > 1500
# Build only one time
%define pythons %{primary_python}
%else
# Build only with python 3.11
%{?sle15_python_module_pythons}
%endif
Name:           gajim
Version:        1.9.0
Release:        0
Summary:        XMPP client written in Python and GTK
License:        GPL-3.0-only
Group:          Productivity/Networking/Talk/Clients
URL:            https://gajim.org/
Source:         https://gajim.org/downloads/1.9/gajim-%{version}.tar.gz
BuildRequires:  %{python_module nbxmpp >= 5.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module precis-i18n >= 1.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpcre1
BuildRequires:  p11-kit-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-generators >= 20220912
BuildRequires:  python-rpm-macros >= 20220912
BuildRequires:  sqlite3 >= 3.35.0
BuildRequires:  update-desktop-files
Requires:       %{python_flavor}-gobject-Gdk
Requires:       %{python_flavor}-gobject-cairo
Requires:       %{python_flavor}-gssapi
Requires:       %{python_flavor}-omemo-dr
Requires:       %{python_flavor}-qrcode
Requires:       ca-certificates-mozilla
Requires:       sqlite3 >= 3.35.0
Requires:       typelib(GtkSource) = 4
Requires:       typelib(Soup) = 3.0
Obsoletes:      gajim-plugin-omemo <= 2.9.0
BuildArch:      noarch
%{?python_enable_dependency_generator}

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
%autosetup
sed -i '/^Keywords/d' data/org.gajim.Gajim.desktop.in

%build
%pyproject_wheel
python%{python_bin_suffix} ./pep517build/build_metadata.py -o dist/metadata

%install
%pyproject_install
python%{python_bin_suffix} ./pep517build/install_metadata.py dist/metadata --prefix=%{buildroot}%{_prefix}

mkdir -p %{buildroot}%{_datadir}/
mv %{buildroot}{%{python_sitelib}/%{name}/data,%{_datadir}/%{name}}/
ln -s %{_datadir}/%{name} %{buildroot}%{python_sitelib}/%{name}/data

# Move locales to the system path.
mv %{buildroot}%{_datadir}/{%{name}/locale,locale}/
ln -s %{_datadir}/locale %{buildroot}%{_datadir}/%{name}/locale

# The plugins subdirectory must be owned by the package.
mkdir %{buildroot}%{_datadir}/%{name}/plugins/

%suse_update_desktop_file -r org.gajim.Gajim Network InstantMessaging
%fdupes %{buildroot}%{_prefix}/
%find_lang %{name}

%files
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}/
# Symlink to /usr/share/locale
%exclude %{_datadir}/%{name}/locale
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-*
%{_datadir}/applications/*%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/*%{name}*.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*%{name}*.metainfo.xml
%{_mandir}/man?/%{name}*%{?ext_man}

%files lang -f %{name}.lang
%{_datadir}/%{name}/locale

%changelog
