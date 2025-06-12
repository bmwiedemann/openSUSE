#
# spec file for package python-setuptools-git
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-setuptools-git
Version:        1.2
Release:        0
Summary:        Setuptools revision control system plugin for Git
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/wichert/setuptools-git
Source:         https://files.pythonhosted.org/packages/source/s/setuptools-git/setuptools-git-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a plugin for setuptools that enables git integration. Once
installed, Setuptools can be told to include in a package distribution
all the files tracked by git. This is an alternative to explicit
inclusion specifications with MANIFEST.in.

This package was formerly known as gitlsfiles. The name change is the
result of an effort by the setuptools plugin developers to provide a
uniform naming convention.

%prep
%setup -q -n setuptools-git-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
export LANG=en_US.UTF-8
# configure git for the test
git config --global user.email "test@test.test"
git config --global user.name "test"
%pyunittest discover -v

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt README.rst TODO.txt
%{python_sitelib}/setuptools[-_]git
%{python_sitelib}/setuptools[-_]git-%{version}*-info

%changelog
