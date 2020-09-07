#
# spec file for package benji
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


Name:           benji
Version:        0.10.0
Release:        0
Summary:        Deduplicating block based backup software
License:        LGPL-3.0-only
URL:            https://benji-backup.me/
Source0:        https://github.com/elemental-lf/benji/archive/v%{version}.tar.gz
BuildRequires:  python3-devel >= 3.6.5
BuildRequires:  python3-setuptools
Requires:       python3-Cerberus >= 1.2
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-alembic >= 1.0.5
Requires:       python3-argcomplete >= 1.9.4
Requires:       python3-colorama >= 0.4.1
Requires:       python3-dateutil >= 2.6.0
Requires:       python3-diskcache >= 3.0.6
Requires:       python3-psutil
Requires:       python3-pycryptodome >= 3.6.1
Requires:       python3-pyparsing >= 2.3.0
Requires:       python3-ruamel.yaml >= 0.15
Requires:       python3-semantic_version >= 2.6.0
Requires:       python3-setproctitle >= 1.1.8
Requires:       python3-shortuuid
Requires:       python3-sparse >= 0.2.2
Requires:       python3-sqlalchemy >= 1.2.6
Requires:       python3-structlog >= 19.1.0
Recommends:     python3-boto3
Recommends:     python3-psycopg2 >= 2.7.4
BuildArch:      noarch

%description
Deduplicating block based backup software for ceph/rbd,
image files and devices.

%prep
%setup -q

%build
%python3_build

%install
mkdir -p %{buildroot}%{_localstatedir}/lib/benji
%python3_install --single-version-externally-managed
# install config
mkdir -p %{buildroot}%{_sysconfdir}/
cp etc/benji.yaml %{buildroot}%{_sysconfdir}/benji.yaml

%files
%doc README.rst
%license LICENSE.txt
%{_bindir}/benji
%{python3_sitelib}/benji*
%config %{_sysconfdir}/benji.yaml

%changelog
