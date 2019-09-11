#
# spec file for package python-cpplint
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
Name:           python-cpplint
Version:        1.4.4
Release:        0
Summary:        An automated checker to make sure a C++ file follows Google's C++ style guide
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/cpplint/cpplint
Source:         https://files.pythonhosted.org/packages/source/c/cpplint/cpplint-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This project continues the work of cpplint, a C++ style checker
following Google's C++ style guide. It provides cpplint as a PyPI
package and adds a few features and fixes. It is maintained as a
fork of google/styleguide (https://github.com/google/styleguide)
in hopes that it can be merged in the future.

%prep
%setup -q -n cpplint-%{version}
sed -i -e '/^#!\//, 1d' cpplint.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/cpplint
%{python_sitelib}/*

%changelog
