#
# spec file for package python-aiostream
#
# Copyright (c) 2022 SUSE LLC
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


%define         skip_python2 1
%define modname aiostream
Name:           python-aiostream
Version:        0.4.5
Release:        0
Summary:        Generator-based operators for asynchronous iteration
License:        Apache-2.0
URL:            https://github.com/vxgmichel/aiostream
Source:         https://github.com/vxgmichel/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-siosocks >= 0.2.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
aiostream provides a collection of stream operators that can be
combined to create asynchronous pipelines of operations.

%prep
%autosetup -p1 -n %{modname}-%{version}

# Remove coverage parameters for pytest
sed -i -e '/addopts/s/=.*$/= tests --strict-markers/' setup.cfg

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
