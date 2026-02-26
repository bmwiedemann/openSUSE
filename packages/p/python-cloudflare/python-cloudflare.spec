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


%define  repo  cloudflare-python
%{?sle15_python_module_pythons}
Name:           python-cloudflare
Version:        4.3.1
Release:        0
Summary:        Python wrapper for the Cloudflare v4 API
License:        MIT
URL:            https://github.com/cloudflare/cloudflare-python
Source:         https://github.com/cloudflare/cloudflare-python/archive/v%{version}/%{repo}-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module jsonlines}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.4.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-beautifulsoup4
Requires:       python-jsonlines
Requires:       python-requests >= 2.4.2
BuildArch:      noarch
%python_subpackages

%description
Python wrapper for the Cloudflare Client API v4.

The Cloudflare Python library provides convenient access to the Cloudflare REST
API from any Python 3.9+ application. The library includes type definitions for
all request params and response fields, and offers both synchronous and
asynchronous clients powered by httpx.

%prep
%setup -q -n %{repo}-%{version}

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

#%%check
# there is one test, but even upstream does not launch it

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cloudflare
%{python_sitelib}/cloudflare-%{version}.dist-info

%changelog
