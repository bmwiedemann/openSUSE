#
# spec file for package deluge
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global __requires_exclude typelib\\(GConf|AyatanaAppIndicator3\\)

%define _version 2.2
Name:           deluge
Version:        2.2.0
Release:        0
Summary:        BitTorrent Client
License:        SUSE-GPL-3.0-with-openssl-exception
Group:          Productivity/Networking/File-Sharing
URL:            https://deluge-torrent.org/
Source:         http://download.deluge-torrent.org/source/%{_version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE deluge-suse-geoip-location.patch -- Point to the right GeoIP.dat location.
Patch0:         %{name}-suse-geoip-location.patch
# PATCH-FIX-UPSTREAM deluge-update_7z_binary.patch
Patch1:         %{name}-update_7z_binary.patch
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
%if 0%{suse_version} >= 1550
BuildRequires:  python3-Twisted-tls >= 17.1
%else
BuildRequires:  python3-Twisted >= 17.1
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-libtorrent-rasterbar >= 1.2
BuildRequires:  python3-rjsmin
BuildRequires:  python3-setuptools
BuildRequires:  python3-slimit
BuildRequires:  python3-wheel
BuildRequires:  strip-nondeterminism
Requires:       python3-Mako
Requires:       python3-Pillow
%if 0%{suse_version} >= 1550
Requires:       python3-Twisted-tls >= 17.1
%else
Requires:       python3-Twisted >= 17.1
%endif
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-libtorrent-rasterbar >= 1.2
Requires:       python3-pyOpenSSL
Requires:       python3-pyxdg
Requires:       python3-rencode
Requires:       python3-setproctitle
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-zope.interface
Requires:       xdg-utils
Recommends:     %{name}-lang
Recommends:     python3-GeoIP
Recommends:     python3-Pillow
Recommends:     python3-chardet
Recommends:     python3-dbus-python
Recommends:     python3-distro
Recommends:     python3-notify
Recommends:     python3-pygame
Recommends:     python3-service_identity
Recommends:     python3-setproctitle
BuildArch:      noarch
%if %{?suse_version} >= 1550
Requires:       python3-pycairo
%else
Requires:       python3-cairo
%endif
%{?systemd_ordering}

%description
Deluge is a Free Software, cross-platform BitTorrent client on
Python and Gtk3 with multiple user interfaces in client/server
model.

%lang_package

%prep
%autosetup -p1
sed -i '/^#!/d' deluge/path_chooser_common.py deluge/ui/gtk3/path_combo_chooser.py

%build
%py3_build

%install
%py3_install
strip-nondeterminism -t zip %{buildroot}%{python3_sitelib}/%{name}/plugins/*.egg
install -D -m 644 packaging/systemd/deluged.service %{buildroot}%{_userunitdir}/deluged.service
install -D -m 644 packaging/systemd/deluge-web.service %{buildroot}%{_userunitdir}/deluge-web.service
%fdupes %{buildroot}%{python3_sitelib}/
%fdupes %{buildroot}%{_datadir}/icons/hicolor/

mv %{buildroot}%{python3_sitelib}/%{name}/i18n %{buildroot}%{_datadir}/locale
%find_lang %{name}

pushd %{buildroot}%{_datadir}/locale/
mkdir %{buildroot}%{python3_sitelib}/%{name}/i18n/
ls | while read -r f; do
    if ( echo "$f" | grep -q '\.py$' ); then
        mv -f "$f" %{buildroot}%{python3_sitelib}/%{name}/i18n/
    else
        ln -s "%{_datadir}/locale/$f" \
          "%{buildroot}%{python3_sitelib}/%{name}/i18n/$f"
    fi
done
popd
%fdupes %{buildroot%}%{_datadir}/icons

%pre
%systemd_user_pre deluged.service deluge-web.service

%post
%systemd_user_post deluged.service deluge-web.service

%preun
%systemd_user_preun deluged.service deluge-web.service

%postun
%systemd_user_postun deluged.service deluge-web.service

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/%{name}*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*
%{_userunitdir}/deluged.service
%{_userunitdir}/deluge-web.service
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/apps/%{name}-panel.*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_mandir}/man1/%{name}*.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
