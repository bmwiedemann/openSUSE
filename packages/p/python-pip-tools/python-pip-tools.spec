#
# spec file for package python-pip-tools
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
%define skip_python2 1
Name:           python-pip-tools
Version:        5.4.0
Release:        0
Summary:        Tool to keep pinned dependencies up to date
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/pip-tools/
Source:         https://files.pythonhosted.org/packages/source/p/pip-tools/pip-tools-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 7
Requires:       python-pip >= 20.0
Requires:       python-setuptools
Requires:       python-six
Requires:       python-wheel
Recommends:     git-core
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 7}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip >= 20.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
pip-tools keeps pinned dependencies inside a project up to date.

%prep
%setup -q -n pip-tools-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pip-compile
%python_clone -a %{buildroot}%{_bindir}/pip-sync
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pip-compile pip-sync

%postun
%python_uninstall_alternative pip-compile pip-sync

%check
export LANG=en_US.UTF-8
%pytest -k 'not network'

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%python_alternative %{_bindir}/pip-compile
%python_alternative %{_bindir}/pip-sync
%{python_sitelib}/*

%changelog
