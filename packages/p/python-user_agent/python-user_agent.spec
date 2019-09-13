#
# spec file for package python-user_agent
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
Name:           python-user_agent
Version:        0.1.9
Release:        0
Summary:        User-Agent generator for Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/lorien/user_agent
Source:         https://pypi.io/packages/source/u/user_agent/user_agent-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
This module generates random, valid web user agents.

%prep
%setup -q -n user_agent-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%python3_only %{_bindir}/ua
%{python_sitelib}/*

%changelog
