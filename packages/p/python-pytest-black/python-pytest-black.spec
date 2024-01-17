#
# spec file for package python-pytest-black
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-pytest-black
Version:        0.3.12
Release:        0
Summary:        Black format checking plugin for pytest
License:        MIT
URL:            https://github.com/shopkeep/pytest-black
Source:         https://files.pythonhosted.org/packages/source/p/pytest-black/pytest-black-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-pytest-makefile.patch -- gh#shopkeep/pytest-black#53
Patch0:         https://github.com/shopkeep/pytest-black/pull/53.patch#/fix-pytest-makefile.patch
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-black
Requires:       python-pytest >= 3.5.0
Requires:       python-toml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module pytest >= 3.5.0}
BuildRequires:  %{python_module toml}
# /SECTION
%python_subpackages

%description
A pytest plugin to enable format checking with black.

%prep
%autosetup -p1 -n pytest-black-%{version}

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
%{python_sitelib}/*

%changelog
