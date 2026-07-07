#
# spec file for package python-anthropic
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


%{?sle15_python_module_pythons}
Name:           python-anthropic
Version:        0.116.0
Release:        0
Summary:        The official Python library for the Anthropic API
License:        MIT
URL:            https://github.com/anthropics/anthropic-sdk-python
Source:         https://files.pythonhosted.org/packages/source/a/anthropic/anthropic-%{version}.tar.gz
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3.5.0
Requires:       python-distro >= 1.7.0
Requires:       python-docstring-parser >= 0.15
Requires:       python-httpx >= 0.25.0
Requires:       python-jiter >= 0.4.0
Requires:       python-pydantic >= 1.9.0
Requires:       python-sniffio
Requires:       python-typing_extensions >= 4.13.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module anyio >= 3.5.0}
BuildRequires:  %{python_module distro >= 1.7.0}
BuildRequires:  %{python_module docstring-parser >= 0.15}
BuildRequires:  %{python_module httpx >= 0.25.0}
BuildRequires:  %{python_module jiter >= 0.4.0}
BuildRequires:  %{python_module pydantic >= 1.9.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sniffio}
BuildRequires:  %{python_module typing_extensions >= 4.13.2}
# /SECTION
%python_subpackages

%description
The Anthropic Python library provides convenient access to the
Anthropic REST API from any Python 3.9+ application. It includes type
definitions for all request params and response fields, and offers both
synchronous and asynchronous clients powered by httpx.

%prep
%autosetup -p1 -n anthropic-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Drop the empty placeholder shipped in the wheel.
%python_expand rm -f %{buildroot}%{$python_sitelib}/anthropic/lib/.keep
# Drop pip's precompiled bytecode and recompile with hash-based invalidation
# so rpmlint does not flag python-bytecode-inconsistent-mtime.
%python_expand find %{buildroot}%{$python_sitelib} -name __pycache__ -type d -exec rm -rf {} +
%python_expand $python -m compileall --invalidation-mode=unchecked-hash %{buildroot}%{$python_sitelib}/anthropic
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The bulk of tests/ (tests/api_resources, test_client, test_response, ...)
# require a registered API key, network access, or snapshot fixtures driven
# by the unpackaged "http_snapshot" helper that tests/conftest.py imports at
# collection time. Run --noconftest on the offline, network-free unit subset
# (serialization, query-string, typing and argument-handling logic).
# Override upstream addopts ("-n auto" needs pytest-xdist; filterwarnings=error
# is too strict for an offline subset build).
%pytest -o addopts="" -W default --noconftest tests/test_models.py tests/test_qs.py tests/test_required_args.py tests/test_extract_files.py tests/test_utils

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/anthropic
%{python_sitelib}/anthropic-%{version}.dist-info

%changelog
