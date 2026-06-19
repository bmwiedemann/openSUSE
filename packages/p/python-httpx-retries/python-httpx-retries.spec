#
# spec file for package python-httpx-retries
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


Name:           python-httpx-retries
Version:        0.5.0
Release:        0
Summary:        A retry layer for HTTPX
License:        MIT
URL:            https://github.com/will-ockmore/httpx-retries
Source:         https://files.pythonhosted.org/packages/source/h/httpx-retries/httpx_retries-%{version}.tar.gz
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module httpx >= 0.20.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpx >= 0.20.0
BuildArch:      noarch
%python_subpackages

%description
A retry layer for the HTTPX client: configurable retry behaviour with
exponential backoff for transient HTTP errors.

%prep
%autosetup -p1 -n httpx_retries-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/httpx_retries
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import httpx_retries"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/httpx_retries
%{python_sitelib}/httpx_retries-%{version}.dist-info

%changelog
