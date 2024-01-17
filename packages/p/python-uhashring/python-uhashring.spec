#
# spec file for package python-uhashring
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-uhashring
Version:        2.3
Release:        0
Summary:        Full featured consistent hashing python library compatible with ketama
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ultrabug/uhashring
Source:         https://github.com/ultrabug/uhashring/archive/refs/tags/%{version}.tar.gz#/uhashring-%{version}-gh.tar.gz
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-memcached}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Full featured consistent hashing python library compatible with ketama.

%prep
%setup -q -n uhashring-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
