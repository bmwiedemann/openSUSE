#
# spec file for package ads
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


Name:           ads
Version:        2.0+git.0.bdc680d
Release:        0
Summary:        Swiss army knife for samba
License:        GPL-3.0-only
Group:          Productivity/Networking/Samba
URL:            https://github.com/suse-samba-tools/ads
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       krb5-client
Requires:       ntp
Requires:       python3-dnspython
Requires:       python3-ldb
Requires:       python3-netifaces
Requires:       python3-psutil
Requires:       python3-python-pam
Requires:       samba-client
Requires:       samba-dsdb-modules
Requires:       samba-python3
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  python3
%if 0%{?sle_version} > 150100
BuildRequires:  python3-argparse-manpage
%endif
BuildRequires:  python3-dnspython
BuildRequires:  python3-ldb
BuildRequires:  python3-netifaces
BuildRequires:  python3-psutil
BuildRequires:  python3-python-pam
BuildRequires:  samba-python3
Provides:       vasclnt
Provides:       vastool

%description
Active Directory services tool for samba.
For join, unjoin, provisioning, demotion, user/group and password administration,
ldap attribute modification, posix enablement, kdc timesync, pam and nss configuration,
daemon start/stop, cache flush, etc.
The ads command attempts to maintain compatibility with the proprietary vastool command,
while also adding additional features relevant to samba (such as kdc provisioning).

%prep
%setup -q

%build
autoreconf -if
%configure
%if 0%{?sle_version} <= 150100
pushd src
%endif
make
%if 0%{?sle_version} <= 150100
popd
%endif

%install
%if 0%{?sle_version} <= 150100
pushd src
%endif
%make_install
%if 0%{?sle_version} <= 150100
popd
%endif
%python3_fix_shebang

%files
%defattr(-,root,root)
%{_bindir}/ads
%{_bindir}/vastool
%if 0%{?sle_version} > 150100
%{_mandir}/man1/ads.1*
%endif

%changelog
