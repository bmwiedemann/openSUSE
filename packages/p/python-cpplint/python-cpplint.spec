#
# spec file for package python-cpplint
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


Name:           python-cpplint
Version:        1.6.1
Release:        0
Summary:        An automated checker to make sure a C++ file follows Google's C++ style guide
License:        BSD-3-Clause
URL:            https://github.com/cpplint/cpplint
Source:         https://files.pythonhosted.org/packages/source/c/cpplint/cpplint-%{version}.tar.gz
# PATCH-FIX-UPSTREAM drop-sre-compile.patch gh#cpplint/cpplint#214
Patch0:         drop-sre-compile.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
sed -i -e '/^#!\//, 1d' cpplint.py
sed -i 's/pytest-runner==5.2//' setup.py
sed -i 's/pytest-cov//' test-requirements
sed -i 's/--cov-fail-under=75 --cov=cpplint//' setup.cfg

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/cpplint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative cpplint

%postun
%python_uninstall_alternative cpplint

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/cpplint
%{python_sitelib}/cpplint*
%pycache_only %{python_sitelib}/__pycache__

%changelog
