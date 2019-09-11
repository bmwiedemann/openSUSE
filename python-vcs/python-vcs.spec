#
# spec file for package python-vcs
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


#
%define skip_python3 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-vcs
Version:        0.4.0
Release:        0
Summary:        Various Version Control System management abstraction layer for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/codeinn/vcs
Source:         https://files.pythonhosted.org/packages/source/v/vcs/vcs-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/codeinn/vcs/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements:
#BuildRequires:  python-mock
#BuildRequires:  python-Pygments
#BuildRequires:  python-nose
#BuildRequires:  python-unittest2
#BuildRequires:  python-dulwich
#BuildRequires:  git-core
Requires:       git-core
Requires:       python-dulwich
BuildArch:      noarch
%python_subpackages

%description
Vcs is an abstraction layer over various version control systems. It is
designed as feature-rich Python library with clean API.

%prep
%setup -q -n vcs-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/vcs/.ropeproject
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests require network access, thus disabled:
#%%check
#nosetests

%files %{python_files}
%license LICENSE
%doc README.rst
%{_bindir}/vcs
%{python_sitelib}/*

%changelog
