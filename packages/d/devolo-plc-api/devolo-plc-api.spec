#
# spec file for package devolo-plc-api
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           devolo-plc-api
Version:        1.6.0
Release:        0
Summary:        devolo PLC devices in Python
License:        GPL-3.0-or-later
URL:            https://github.com/2Fake/devolo_plc_api
Source:         https://files.pythonhosted.org/packages/source/d/devolo_plc_api/devolo_plc_api-%{version}.tar.gz
# Single-flavor app-style package (no python subpackages): the module is
# shipped for the default python3 only.
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-httpx >= 0.21.0
BuildRequires:  python3-ifaddr >= 0.1.7
BuildRequires:  python3-pip
BuildRequires:  python3-protobuf >= 4.22.0
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-httpx >= 0.18.0
BuildRequires:  python3-segno >= 1.5.2
BuildRequires:  python3-setuptools >= 77
BuildRequires:  python3-setuptools_scm >= 6.2
BuildRequires:  python3-syrupy
BuildRequires:  python3-tenacity >= 8.3.0
BuildRequires:  python3-typing_extensions
BuildRequires:  python3-wheel
BuildRequires:  python3-zeroconf >= 0.70.0
Requires:       python3-httpx >= 0.21.0
Requires:       python3-ifaddr >= 0.1.7
Requires:       python3-protobuf >= 4.22.0
Requires:       python3-segno >= 1.5.2
Requires:       python3-tenacity >= 8.3.0
Requires:       python3-zeroconf >= 0.70.0
BuildArch:      noarch

%description
Python API for devolo PLC powerline devices. Communication to the
devices is formatted in protobuf.

%prep
%autosetup -p1 -n devolo_plc_api-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%{python3_pyproject_wheel}

%install
%{python3_pyproject_install}
python3 -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{python3_sitelib}/devolo_plc_api
%fdupes %{buildroot}%{python3_sitelib}

%check
%{python3_pytest}

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/devolo_plc_api
%{python3_sitelib}/devolo_plc_api-%{version}.dist-info

%changelog
