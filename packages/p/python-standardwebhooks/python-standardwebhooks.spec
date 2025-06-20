#
# spec file for package python-standardwebhooks
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


Name:           python-standardwebhooks
Version:        1.0.0
Release:        0
Summary:        Standard Webhooks
License:        MIT
URL:            https://github.com/standard-webhooks/standard-webhooks/tree/main/libraries/python
Source:         https://files.pythonhosted.org/packages/source/s/standardwebhooks/standardwebhooks-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/standard-webhooks/standard-webhooks/refs/heads/main/libraries/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 21.3.0}
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module httpx >= 0.23.0}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 21.3.0
Requires:       python-Deprecated
Requires:       python-httpx >= 0.23.0
Requires:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
Standard Webhooks

%prep
%autosetup -p1 -n standardwebhooks-%{version}
cp %SOURCE1 .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/standardwebhooks
%{python_sitelib}/standardwebhooks-%{version}.dist-info

%changelog
