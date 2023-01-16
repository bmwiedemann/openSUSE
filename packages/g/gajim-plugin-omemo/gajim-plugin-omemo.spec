#
# spec file for package gajim-plugin-omemo
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


# Requires at least python 3.10
%define py3ver 3.10
%define py3pkg python310
%define _name   omemo
Name:           gajim-plugin-omemo
Version:        2.9.0
Release:        0
Summary:        Gajim plugin for OMEMO Multi-End Message and Object Encryption
License:        GPL-3.0-only
Group:          Productivity/Networking/Talk/Clients
URL:            https://dev.gajim.org/gajim/gajim-plugins/wikis/OmemoGajimPlugin
Source:         https://ftp.gajim.org/plugins/master/omemo/omemo_%{version}.zip
BuildRequires:  %{py3pkg}-protobuf
BuildRequires:  gajim >= 1.6.0
BuildRequires:  unzip
Requires:       %{py3pkg}-axolotl
Requires:       %{py3pkg}-base
Requires:       %{py3pkg}-cryptography
Requires:       %{py3pkg}-protobuf
Requires:       gajim
# Verification QR Codes
Recommends:     %{py3pkg}-qrcode
BuildArch:      noarch

%description
This plugin adds support to Gajim for the OMEMO Encryption, an
XMPP Extension Protocol (XEP) for secure multi-client end-to-end
encryption based on Double Ratchet and PEP.

%prep
%setup -q -c

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/gajim/plugins/%{_name}/
cp -aT . %{buildroot}%{_datadir}/gajim/plugins/%{_name}/
rm %{buildroot}%{_datadir}/gajim/plugins/%{_name}/COPYING

%files
%license COPYING
%{_datadir}/gajim/plugins/%{_name}/

%changelog
