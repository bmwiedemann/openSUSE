#
# spec file for package python-shutilwhich
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


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-shutilwhich
Version:        1.1.0
Release:        0
License:        Python-2.0
Summary:        Backport of Python 3.3 shutil.which function
Url:            http://github.com/mbr/shutilwhich
Group:          Development/Languages/Python
Source:         https://github.com/mbr/shutilwhich/archive/%{version}.tar.gz#/shutilwhich-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/mbr/shutilwhich/master/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools >= 18.0.1}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Backport of Python 3.3 shutil.which function.

This library monkey patches the standard library
shutil.which on versions prior to Python 3.3.

Use backports.shutil_which if monkey patching of
the standard library function is not desirable.

%prep
%setup -q -n shutilwhich-%{version}
sed -i '1 { /^#!/ d }' shutilwhich/__init__.py

cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
