#
# spec file for package python-aiohappyeyeballs
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


%{?sle15_python_module_pythons}
Name:           python-aiohappyeyeballs
Version:        2.6.1
Release:        0
Summary:        Happy Eyeballs for asyncio
License:        Python-2.0
URL:            https://github.com/aio-libs/aiohappyeyeballs
Source:         https://files.pythonhosted.org/packages/source/a/aiohappyeyeballs/aiohappyeyeballs-%{version}.tar.gz
# PATCH-FIX-OPENSUSE drop the offending helper function to enable tests
# https://github.com/aio-libs/aiohappyeyeballs/pull/177 chore(deps-dev): bump pytest-asyncio from 0.26.0 to 1.0.0
Patch0:         event_loop.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library exists to allow connecting with Happy Eyeballs (RFC 8305) when
you already have a list of addrinfo and not a DNS name.

The stdlib version of `loop.create_connection()`
will only work when you pass in an unresolved name which
is not a good fit when using DNS caching or resolving
names via another method such was `zeroconf`.

%prep
%autosetup -p1 -n aiohappyeyeballs-%{version}

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
%{python_sitelib}/aiohappyeyeballs
%{python_sitelib}/aiohappyeyeballs-%{version}.dist-info

%changelog
