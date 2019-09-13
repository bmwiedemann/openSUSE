#
# spec file for package python-inifile
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-inifile
Version:        0.4
Release:        0
License:        BSD-3-Clause
Summary:        A small INI library for Python
Url:            https://github.com/mitsuhiko/python-inifile
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/i/inifile/inifile-%{version}.zip
Source1:        https://raw.githubusercontent.com/mitsuhiko/python-inifile/master/LICENSE
Source2:        https://raw.githubusercontent.com/mitsuhiko/python-inifile/master/hello.ini
Source3:        https://raw.githubusercontent.com/mitsuhiko/python-inifile/master/test.py
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  unzip
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
A small INI library for Python.

%prep
%setup -q -n inifile-%{version}
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .
python3 -m lib2to3 -w -n --no-diffs test.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
