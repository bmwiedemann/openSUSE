#
# spec file for package bump2version
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           bump2version
Version:        1.0.0
Release:        0
License:        MIT
Summary:        Version-bump your software with a single command!
Url:            https://github.com/c4urself/bump2version
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/b/bump2version/bump2version-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testfixtures}
Obsoletes:      bumpversion <= 0.6.0
BuildArch:      noarch

%python_subpackages

%description
Version-bump your software with a single command!

%prep
%setup -q -n bump2version-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_usage_string_fork: bumpversion is not in PATH
%pytest -k 'not test_usage_string_fork'

%files %{python_files}
%doc README.md
%license LICENSE.rst
%python3_only %{_bindir}/bumpversion
%python3_only %{_bindir}/bump2version
%{python_sitelib}/*

%changelog
