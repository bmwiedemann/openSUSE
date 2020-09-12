#
# spec file for package gajim-plugin-omemo
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


%define _name   omemo
Name:           gajim-plugin-omemo
Version:        2.6.80
Release:        0
Summary:        Gajim plugin for OMEMO Multi-End Message and Object Encryption
License:        GPL-3.0-only
Group:          Productivity/Networking/Talk/Clients
URL:            https://dev.gajim.org/gajim/gajim-plugins/wikis/OmemoGajimPlugin
Source:         https://ftp.gajim.org/plugins_releases/omemo_%{version}.zip
BuildRequires:  gajim >= 1.1
BuildRequires:  python3-protobuf
BuildRequires:  unzip
Requires:       gajim
Requires:       python3-axolotl
Requires:       python3-cryptography
Requires:       python3-protobuf
Requires:       python3-qrcode
BuildArch:      noarch

%description
This plugin adds support to Gajim for the OMEMO Encryption, an
XMPP Extension Protocol (XEP) for secure multi-client end-to-end
encryption based on Double Ratchet and PEP.

%prep
%setup -q -n %{_name}

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/gajim/plugins/%{_name}/
cp -aT . %{buildroot}%{_datadir}/gajim/plugins/%{_name}/
for f in CHANGELOG COPYING; do
    rm "%{buildroot}%{_datadir}/gajim/plugins/%{_name}/$f"
done

%files
%license COPYING
%doc CHANGELOG
%{_datadir}/gajim/plugins/%{_name}/

%changelog
