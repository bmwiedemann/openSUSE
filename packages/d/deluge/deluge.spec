#
# spec file for package deluge
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


%define _version 2.0
Name:           deluge
Version:        2.0.3
Release:        0
Summary:        BitTorrent Client
License:        SUSE-GPL-3.0-with-openssl-exception
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
BuildRequires:  python3-Twisted >= 17.1
BuildRequires:  python3-devel
%if 0%{?suse_version} > 1500
BuildRequires:  python3-libtorrent-rasterbar-1 >= 1.1.1
%else
BuildRequires:  python3-libtorrent-rasterbar >= 1.1.1
%endif
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  update-desktop-files
Requires:       python3-Mako
Requires:       python3-Pillow
Requires:       python3-Twisted >= 17.1
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
%if 0%{?suse_version} > 1500
Requires:       python3-libtorrent-rasterbar-1 >= 1.1.1
%else
Requires:       python3-libtorrent-rasterbar >= 1.1.1
%endif
Requires:       python3-pyOpenSSL
Requires:       python3-rencode
Requires:       python3-setproctitle
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-xdg
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
%if %{?suse_version} > 1510
BuildRequires:  python3-slimit
%endif
%if %{?suse_version} >= 1550
Requires:       python3-pycairo
%else
Requires:       python3-cairo
%endif

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
%fdupes %{buildroot}%{python3_sitelib}/

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

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/%{name}*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/apps/%{name}-panel.*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/%{name}*.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
