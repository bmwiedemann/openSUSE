#
# spec file for package python-cloudflare
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


# tests take forever and most of them (apparently) need internet access
%bcond_with test
%define  repo  cloudflare-python
%{?sle15_python_module_pythons}
Name:           python-cloudflare
Version:        4.3.1
Release:        0
Summary:        Python wrapper for the Cloudflare v4 API
License:        MIT
URL:            https://github.com/cloudflare/cloudflare-python
Source:         https://github.com/cloudflare/cloudflare-python/archive/v%{version}/%{repo}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/cloudflare/cloudflare-python/commit/813dd685ebe2158929bd275c58ad2979ef89b879 feat: improve future compat with pydantic v3
Patch0:         pydantic3.patch
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
%if %{with test}
BuildRequires:  %{python_module anyio >= 3.5.0}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module distro >= 1.7.0}
BuildRequires:  %{python_module httpx >= 0.23}
BuildRequires:  %{python_module pydantic >= 1.0.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module respx}
BuildRequires:  %{python_module sniffio}
BuildRequires:  %{python_module typing-extensions >= 4.10}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-anyio >= 3.5.0
Requires:       python-distro >= 1.7.0
Requires:       python-httpx >= 0.23
Requires:       python-pydantic >= 1.0.0
Requires:       python-sniffio
Requires:       python-typing-extensions >= 4.10
BuildArch:      noarch
%python_subpackages

%description
Python wrapper for the Cloudflare Client API v4.

The Cloudflare Python library provides convenient access to the Cloudflare REST
API from any Python 3.9+ application. The library includes type definitions for
all request params and response fields, and offers both synchronous and
asynchronous clients powered by httpx.

%prep
%autosetup -p1 -n %{repo}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# remove examples from sitelib
%python_expand rm -rf %{buildroot}%{$python_sitelib}/examples
# Note: rpmlint may report files-duplicate for some __init__.py files
# that have the same name but different content in different namespaces.
# Those warnings are false positives and can be safely ignored.
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with test}
# radar tests are improperly configured
rm -r tests/api_resources/radar
%pytest
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cloudflare
%{python_sitelib}/cloudflare-%{version}.dist-info

%changelog
