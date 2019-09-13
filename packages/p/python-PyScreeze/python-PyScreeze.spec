#
# spec file for package python-PyScreeze
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-PyScreeze
Version:        0.1.21
Release:        0
Summary:        A screenshot Python module
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/asweigart/pyscreeze
Source:         https://files.pythonhosted.org/packages/source/P/PyScreeze/PyScreeze-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-xlib}
BuildRequires:  scrot
BuildRequires:  xvfb-run
# /SECTION
%python_subpackages

%description
PyScreeze is a screenshot module for Python 2 and 3.

%prep
%setup -q -n PyScreeze-%{version}
dos2unix README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests lack fixtures https://github.com/asweigart/pyscreeze/issues/44
#pushd tests/
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run py.test-%{$python_bin_suffix} -v
#popd

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
