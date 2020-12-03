#
# spec file for package python-three-merge
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
Name:           python-three-merge
Version:        0.1.1
Release:        0
Summary:        Simple library for merging two strings with respect to a base one
License:        MIT
URL:            https://github.com/spyder-ide/three-merge
# Use GitHub archive instead of PyPI sdist because of test files
Source:         %{url}/archive/v%{version}.tar.gz#/three-merge-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-diff-match-patch
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module diff-match-patch}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Simple Python library to perform a 3-way merge between strings, based on
diff-match-patch. This library performs merges at a character level, as
opposed to most VCS systems, which opt for a line-based approach.

%prep
%setup -q -n three-merge-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/three_merge
%{python_sitelib}/three_merge-%{version}*-info

%changelog
