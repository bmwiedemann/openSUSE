#
# spec file for package python-cpplint
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-cpplint
Version:        2.0.2
Release:        0
Summary:        An automated checker to make sure a C++ file follows Google's C++ style guide
License:        BSD-3-Clause
URL:            https://github.com/cpplint/cpplint
Source:         https://files.pythonhosted.org/packages/source/c/cpplint/cpplint-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#cpplint/cpplint#405
Patch0:         do-not-use-codecs-open.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
This project continues the work of cpplint, a C++ style checker
following Google's C++ style guide. It provides cpplint as a PyPI
package and adds a few features and fixes. It is maintained as a
fork of google/styleguide (https://github.com/google/styleguide)
in hopes that it can be merged in the future.

%prep
%autosetup -p1 -n cpplint-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cpplint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative cpplint

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/cpplint
%{python_sitelib}/cpplint.py
%pycache_only %{python_sitelib}/__pycache__/cpplint.*.pyc
%{python_sitelib}/cpplint-%{version}.dist-info

%changelog
