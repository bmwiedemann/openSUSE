#
# spec file for package python-pytest-spec
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


Name:           python-pytest-spec
Version:        3.2.0
Release:        0
Summary:        Plugin to display pytest execution output like a specification
License:        GPL-2.0-only
URL:            https://github.com/pchomik/pytest-spec
Source:         https://files.pythonhosted.org/packages/source/p/pytest-spec/pytest-spec-%{version}.tar.gz
# https://github.com/pchomik/pytest-spec/compare/3.2.0...master
Patch1:         python-pytest-spec-nopython2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
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
%{python_sitelib}/pytest_spec*

%changelog
