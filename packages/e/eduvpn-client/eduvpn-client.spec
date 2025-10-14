#
# spec file for package eduvpn-client
#
# Copyright (c) 2025 SUSE LLC
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


%define skip_python2 1
%define vname linux-app
Name:           eduvpn-client
Version:        4.6.0
Release:        0
Summary:        The eduVPN desktop client (CLI and GUI front-end)
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.eduvpn.org/
Source0:        https://codeberg.org/eduVPN/linux-app/releases/download/%{version}/%{vname}-%{version}.tar.xz
Source1:        https://codeberg.org/eduVPN/linux-app/releases/download/%{version}/%{vname}-%{version}.tar.xz.asc
                # https://app.eduvpn.org/linux/v4/deb/app+linux@eduvpn.org.asc and inside package dir 'keys'
Source2:        %{name}.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module eduvpn-common >= 4.0.0 with %python-eduvpn-common < 5}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gtk3
BuildRequires:  libnotify
BuildRequires:  python-rpm-macros
BuildRequires:  rsync
BuildRequires:  update-desktop-files
Requires:       NetworkManager-openvpn
Requires:       gtk3
Requires:       python3-%{name}
BuildArch:      noarch
%define python_subpackage_only 1
%python_subpackages

%description
The eduVPN desktop client is a specialized virtual private network (VPN)
solution designed primarily for the education and research community. It offers
preconfigured secure and private network connections for students, faculty, and
researchers at educational institutions, providing several key advantages over
traditional VPN clients.

%package -n python-%{name}
Summary:        Python3 API for eduVPN
Requires:       NetworkManager-openvpn
Requires:       (python-eduvpn-common >= 4.0.0 with python-eduvpn-common < 5)
Requires:       python-gobject

%description -n python-%{name}
eduVPN client API for Python3

%package -n letsconnect-client
Summary:        Let's Connect! desktop client
Requires:       gtk3
Requires:       python3-%{name}

%description -n letsconnect-client
The 'Let's Connect!' desktop client is an open source VPN solution that enables
ISPs, hosters and companies to easily set up a secure VPN service. The project
is known under two names: 'Let’s Connect!' and eduVPN. The brand eduVPN is used
to promote this VPN solution to international educational and research
organizations.

%prep
%autosetup -n %{vname}-%{version}

# Dir 'data' conflicts otherwise with Python subpackages
mv eduvpn/data data

%build
%pyproject_wheel

%install
%pyproject_install

# Manual copy of extra files. Previously they were specified in setup.py.
rsync -a data/share/ \
  --exclude '*.po' \
  --exclude '*.pot' \
  --exclude 'Makefile' %{buildroot}%{_datadir}/

%find_lang eduVPN
%suse_update_desktop_file org.eduvpn.client Network Dialup
%suse_update_desktop_file org.letsconnect-vpn.client Network Dialup
%fdupes %{buildroot}%{_datadir}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files -n %{name} -f eduVPN.lang
%license LICENSE
%doc CHANGES.md README.md
%dir %{_datadir}/eduvpn
%{_datadir}/eduvpn/
%{_bindir}/eduvpn-cli
%{_bindir}/eduvpn-gui
%{_datadir}/applications/org.eduvpn.client.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.eduvpn.client.png
%{_datadir}/icons/hicolor/256x256/apps/org.eduvpn.client.png
%{_datadir}/icons/hicolor/48x48/apps/org.eduvpn.client.png
%{_datadir}/icons/hicolor/512x512/apps/org.eduvpn.client.png

%files %{python_files %{name}}
%license LICENSE
%doc CHANGES.md README.md
%{python_sitelib}/eduvpn*

%files -n letsconnect-client
%license LICENSE
%doc CHANGES.md README.md
%dir %{_datadir}/letsconnect
%{_datadir}/letsconnect/
%{_bindir}/letsconnect-cli
%{_bindir}/letsconnect-gui
%{_datadir}/applications/org.letsconnect-vpn.client.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.letsconnect-vpn.client.png
%{_datadir}/icons/hicolor/256x256/apps/org.letsconnect-vpn.client.png
%{_datadir}/icons/hicolor/48x48/apps/org.letsconnect-vpn.client.png
%{_datadir}/icons/hicolor/512x512/apps/org.letsconnect-vpn.client.png

%changelog
