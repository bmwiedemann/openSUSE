#
# spec file for package python-big
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-big
Version:        0.14
Release:        0
Summary:        A grab-bag of cool code
License:        MIT
URL:            https://github.com/larryhastings/big/
Source:         https://files.pythonhosted.org/packages/source/b/big/big-%{version}.tar.gz
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module inflect}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module regex}
# /SECTION
BuildRequires:  fdupes
Suggests:       python-packaging
Suggests:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
big is a Python package of small functions and classes
that aren't big enough to get a package of their own.
It's zillions of useful little bits of
Python code I always want to have handy.

%prep
%autosetup -p1 -n big-%{version}
sed -i '/^#!\/usr\/bin\/env python3$/d' big/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Fiddles with sys.path, which play badly with our macros
%python_exec tests/test_all.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/big
%{python_sitelib}/big-%{version}.dist-info

%changelog
