#
# spec file for package python-google-pasta
#
# Copyright (c) 2021 SUSE LLC
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


%define packagename pasta
Name:           python-google-pasta
Version:        0.2.0
Release:        0
Summary:        Enable python source code refactoring through AST modifications
License:        Apache-2.0
URL:            https://github.com/google/pasta/
Source:         https://github.com/google/pasta/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/google/pasta/commit/3451d8b9fb67a2fa3098edd73ea3dba98074d6dd Add test for ast node support
Patch0:         ast.patch
# PATCH-FIX-UPSTREAM https://github.com/google/pasta/commit/6179ebf76faf38430180232d0e86198429afcd33 Bugfix for parsing fstrings in multiple parts
Patch1:         fstrings.patch
# PATCH-FIX-UPSTREAM https://github.com/google/pasta/commit/386d94c04e8d10c945ec330debc3a018ed4e91a4 Add test goldens for python 3.9
Patch2:         golden39.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Enable python source code refactoring through AST modifications.

%prep
%setup -q -n %{packagename}-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*egg-info/
%{python_sitelib}/%{packagename}/

%changelog
