#
# spec file for package python-aiostream
#
# Copyright (c) 2023 SUSE LLC
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


%global modname aiostream
%{?sle15_python_module_pythons}
Name:           python-aiostream
Version:        0.6.4
Release:        0
Summary:        Generator-based operators for asynchronous iteration
License:        Apache-2.0
URL:            https://github.com/vxgmichel/%{modname}
Source:         https://github.com/vxgmichel/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-siosocks >= 0.2.0
Requires:       python-typing-extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
%python_subpackages

%description
aiostream provides a collection of stream operators that can be
combined to create asynchronous pipelines of operations.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{modname}-%{version}*-info
%{python_sitelib}/%{modname}

%changelog
