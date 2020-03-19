#
# spec file for package python-shellingham
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-shellingham
Version:        1.3.2
Release:        0
Summary:        Library to detect surrounding shell
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/shellingham
Source:         https://github.com/sarugaku/shellingham/archive/%{version}.tar.gz#//shellingham-%{version}.tar.gz
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python library to detect surrounding shell.

%prep
%setup -q -n shellingham-%{version}

%build
if [ -f setup.py ]; then
  echo 'remove setup.py creation in %%build'
  exit 1
fi
# https://github.com/sarugaku/shellingham/blob/master/setup.py
cat << EOF > setup.py
from setuptools import setup
setup()
EOF
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
