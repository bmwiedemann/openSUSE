#
# spec file for package python-parver
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


Name:           python-parver
Version:        0.4
Release:        0
Summary:        Module to parse and manipulate version numbers
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/RazerM/parver
Source:         https://files.pythonhosted.org/packages/source/p/parver/parver-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Arpeggio >= 1.7
Requires:       python-attrs >= 19.2
Requires:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Arpeggio >= 1.7}
BuildRequires:  %{python_module attrs >= 19.2}
BuildRequires:  %{python_module hypothesis >= 3.56}
BuildRequires:  %{python_module pretend >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%python_subpackages

%description
parver allows parsing and manipulation of `PEP 440`_ version numbers.

%prep
%autosetup -p1 -n parver-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -q

%files %{python_files}
%license LICENSE
%doc README*
%{python_sitelib}/parver*

%changelog
