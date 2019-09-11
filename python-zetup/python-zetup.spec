#
# spec file for package python-zetup
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
Name:           python-zetup
Version:        0.2.48
Release:        0
Summary:        Project setups tools
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/zimmermanncode/zetup
Source:         https://files.pythonhosted.org/packages/source/z/zetup/zetup-%{version}.tar.gz
BuildRequires:  %{python_module nbconvert >= 5.4}
BuildRequires:  %{python_module path.py >= 11.5}
BuildRequires:  %{python_module pytest >= 3.8}
BuildRequires:  %{python_module setuptools >= 40.8}
BuildRequires:  %{python_module setuptools_scm >= 3.1}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-jinjatools >= 0.1.8
Recommends:     python-nbconvert >= 5.4
Recommends:     python-path.py >= 11.5
Recommends:     python-pip >= 19.0
Recommends:     python-pytest
BuildArch:      noarch
%python_subpackages

%description
Zimmermann's Extensible Tools for Unified Project setups

%prep
%setup -q -n zetup-%{version}
dos2unix README.rst
dos2unix zetup/script.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/zetup

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest zetup
# test_python - checks if python is set by maintainer to be supported, bogus
# test_class_dir - check dir content and looks weird too
%pytest test -k 'not (test_python or test_class_dir or test_dir)'

%post
%python_install_alternative zetup

%postun
%python_uninstall_alternative zetup

%files %{python_files}
%doc README.ipynb README.md README.rst
%license COPYING COPYING.LESSER
%python_alternative %{_bindir}/zetup
%{python_sitelib}/*

%changelog
