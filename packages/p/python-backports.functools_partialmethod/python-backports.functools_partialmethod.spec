#
# spec file for package python-backports.functools_partialmethod
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if %{python3_version_nodots} > 35
%define skip_python3 1
%endif
Name:           python-backports.functools_partialmethod
Version:        3.5.1.0
Release:        0
Summary:        Backport of functools.partialmethod
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/PythonBackports/backports.functools_partialmethod
Source:         https://files.pythonhosted.org/packages/source/b/backports.functools_partialmethod/backports.functools_partialmethod-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
BuildArch:      noarch
%python_subpackages

%description
Backport of `functools.partialmethod` from Python 3.5.1.

%prep
%setup -q -n backports.functools_partialmethod-%{version}
rm -rf *.egg-info

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
