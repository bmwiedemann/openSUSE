#
# spec file for package python-extratools
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


%bcond_without libalternatives
Name:           python-extratools
Version:        0.8.2.1
Release:        0
Summary:        145+ extra higher-level functional tools
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/chuanconggao/extratools
Source:         https://files.pythonhosted.org/packages/source/e/extratools/extratools-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-RegexOrder >= 0.2
Requires:       python-TagStats >= 0.1.2
Requires:       python-sh >= 1.12.13
Requires:       python-sortedcontainers >= 1.5.10
Requires:       python-toolz >= 0.9.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module RegexOrder >= 0.2}
BuildRequires:  %{python_module TagStats >= 0.1.2}
BuildRequires:  %{python_module sh >= 1.12.13}
BuildRequires:  %{python_module sortedcontainers >= 1.5.10}
BuildRequires:  %{python_module toolz >= 0.9.0}
# /SECTION
%python_subpackages

%description
145+ extra higher-level functional tools that go beyond standard
library's itertools, functools, etc. and popular third-party
libraries like toolz, funcy, and more-itertools.

%prep
%setup -q -n extratools-%{version}
sed -i -e '/^#!\s*\//, 1d' extratools/*.py
sed -i -e '/^#!\s*\//, 1d' extratools/*/*.js
chmod a-x extratools/*/*.js

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/extratools-teststats
%python_clone -a %{buildroot}%{_bindir}/extratools-remap
%python_clone -a %{buildroot}%{_bindir}/extratools-flatten
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative extratools-teststats
%python_libalternatives_reset_alternative extratools-remap
%python_libalternatives_reset_alternative extratools-flatten

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/extratools-flatten
%python_alternative %{_bindir}/extratools-remap
%python_alternative %{_bindir}/extratools-teststats
%{python_sitelib}/extratools
%{python_sitelib}/extratools-%{version}*-info

%changelog
