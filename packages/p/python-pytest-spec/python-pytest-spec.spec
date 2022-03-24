#
# spec file for package python-pytest-spec
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-pytest-spec
Version:        3.2.0
Release:        0
Summary:        Plugin to display pytest execution output like a specification
License:        GPL-2.0-only
URL:            https://github.com/pchomik/pytest-spec
Source:         https://files.pythonhosted.org/packages/source/p/pytest-spec/pytest-spec-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#pchomik/pytest-spec#51
Patch0:         remove-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
pytest plugin to display test execution output like a specification.

%prep
%autosetup -p1 -n pytest-spec-%{version}

%build
%python_build

%install
%python_install
# Do not install tests
%python_expand rm -r %{buildroot}%{$python_sitelib}/test
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
