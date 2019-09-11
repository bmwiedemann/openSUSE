#
# spec file for package python-flake8-future-import
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
Name:           python-flake8-future-import
Version:        0.4.5
Release:        0
Summary:        __future__ import checker, plugin for flake8
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/xZise/flake8-future-import
Source:         https://files.pythonhosted.org/packages/source/f/flake8-future-import/flake8-future-import-%{version}.tar.gz
Patch0:         python37.patch
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8
BuildArch:      noarch
%python_subpackages

%description
A script to check for the imported ``__future__`` modules to make it easier to
have a consistent code base.

By default it requires and forbids all imports but it's possible to have
certain imports optional by ignoring both their requiring and forbidding error
code. In the future it's planned to have a “consistency” mode and that the
default is having the import optional or required (not sure on that yet).

This module provides a plugin for ``flake8``, the Python code checker.

%prep
%setup -q -n flake8-future-import-%{version}
%patch0 -p1
mv test_flake8_future_import.py test_flake8_future_import.py.in

%build
%python_build

%check
%{python_expand # Deal with generated Python code
sed -e "s|#!%{_bindir}/python\\\\n|#!%{_bindir}/$python\\\\n|g" \
    -e "s|command = \\['flake8'|command = \\['flake8-%{$python_bin_suffix}'|g" \
    test_flake8_future_import.py.in > test_flake8_future_import.py
$python setup.py test
}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
