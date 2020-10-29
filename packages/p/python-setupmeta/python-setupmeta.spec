#
# spec file for package python-setupmeta
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
Name:           python-setupmeta
Version:        2.7.16
Release:        0
Summary:        Simplify your setup.py
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/zsimic/setupmeta
Source:         https://github.com/zsimic/setupmeta/archive/v%{version}.tar.gz#/setupmeta-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Recommends:     git-core
Recommends:     python-pip
Recommends:     python-setuptools_scm
Recommends:     python-twine
Recommends:     python-wheel
BuildArch:      noarch
%python_subpackages

%description
Simplify your setup.py.

%prep
%setup -q -n setupmeta-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git init
export LANG=en_US.UTF-8
# test_check_dependencies needs to be run in a venv
# test_wheel is https://github.com/zsimic/setupmeta/issues/61
%pytest -k 'not (test_check_dependencies or test_wheel)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
