#
# spec file for package python-tinyrecord
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
Name:           python-tinyrecord
Version:        0.1.5
Release:        0
License:        MIT
Summary:        Atomic transactions for TinyDB
Url:            https://github.com/eugene-eeo/tinyrecord
Group:          Development/Languages/Python
Source:         https://github.com/eugene-eeo/tinyrecord/archive/%{version}.tar.gz#/tinyrecord-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/eugene-eeo/tinyrecord/master/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tinydb}
BuildRequires:  fdupes
Requires:       python-tinydb
BuildArch:      noarch

%python_subpackages

%description
Atomic transactions for TinyDB.

%prep
%setup -q -n tinyrecord-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python setup.py pytest --addopts="tests.py"
$python ./test.py
}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
