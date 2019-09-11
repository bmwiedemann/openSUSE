#
# spec file for package python-setuptools_scm_git_archive
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
Name:           python-setuptools_scm_git_archive
Version:        1.1
Release:        0
Summary:        Git archive plugin setuptools_scm
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/Changaco/setuptools_scm_git_archive/
Source:         https://files.pythonhosted.org/packages/source/s/setuptools_scm_git_archive/setuptools_scm_git_archive-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools_scm
BuildArch:      noarch

%python_subpackages

%description
This is a setuptools_scm plugin that adds support for git archives
(for example the ones GitHub automatically generates).

Note that it only works for archives of tagged commits (because git currently
lacks a format option equivalent to git describe --tags).

%prep
%setup -q -n setuptools_scm_git_archive-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#There are no tests for this package.
#%%check
#%%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
