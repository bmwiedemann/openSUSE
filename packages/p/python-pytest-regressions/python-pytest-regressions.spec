#
# spec file for package python-pytest-regressions
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python36 1
Name:           python-pytest-regressions
Version:        2.2.0
Release:        0
License:        MIT
Summary:        Python fixtures to write regression tests
Url:            https://github.com/ESSS/pytest-regressions
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pytest-regressions/pytest-regressions-%{version}.tar.gz
# PATCH-FIX-UPSTREAM np_num-deprecated.patch gh#ESSS/pytest-regressions#63 mcepl@suse.com
# don't use deprecated np.* types
Patch0:         np_num-deprecated.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.5.0}
BuildRequires:  %{python_module pytest-datadir >= 1.2.0}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module Pillow}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 3.5.0
Requires:       python-pytest-datadir >= 1.2.0
Requires:       python-PyYAML
Suggests:       python-matplotlib
Suggests:       python-numpy
Suggests:       python-pandas
Suggests:       python-Pillow
BuildArch:      noarch

%python_subpackages

%description
Python fixtures to write regression tests.

%prep
%autosetup -p1 -n pytest-regressions-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pytest_regressions*

%changelog
