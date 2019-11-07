#
# spec file for package python-PyGithub
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
Name:           python-PyGithub
Version:        1.44.1
Release:        0
Summary:        Python library to use the GitHub API v3
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/PyGithub/PyGithub
Source:         https://github.com/PyGithub/PyGithub/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module httpretty >= 0.9.6}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module parameterized == 0.7.0}
BuildRequires:  %{python_module requests >= 2.14.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Deprecated
Requires:       python-PyJWT
Requires:       python-requests >= 2.14.0
Recommends:     python-cryptography
BuildArch:      noarch
%python_subpackages

%description
PyGithub is a Python (2 and 3) library to use the Github API v3.
Github resources (repositories, user profiles, organizations,
etc.) can be managed with this.

%prep
%setup -q -n PyGithub-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python setup.py test

%files %{python_files}
%license COPYING COPYING.LESSER
%doc README.md
%{python_sitelib}/*

%changelog
