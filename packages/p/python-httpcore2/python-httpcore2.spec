#
# spec file for package python-httpcore2
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


Name:           python-httpcore2
Version:        2.4.0
Release:        0
Summary:        A minimal low-level HTTP client
License:        BSD-3-Clause
URL:            https://github.com/pydantic/httpx2
Source:         https://files.pythonhosted.org/packages/source/h/httpcore2/httpcore2-%{version}.tar.gz
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-dynamic-versioning >= 0.8.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module h11 >= 0.16}
BuildRequires:  %{python_module truststore >= 0.10}
# /SECTION
BuildRequires:  fdupes
Requires:       python-h11 >= 0.16
Requires:       python-truststore >= 0.10
Suggests:       python-h2 >= 3
Suggests:       python-socksio >= 1.0
Suggests:       python-trio >= 0.22.0
Suggests:       python-anyio >= 4.5
BuildArch:      noarch
%python_subpackages

%description
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only. Sending HTTP requests.

%prep
%autosetup -p1 -n httpcore2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests are run inside the python-httpx2 package instead

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{python_sitelib}/httpcore2
%{python_sitelib}/httpcore2-%{version}.dist-info

%changelog
