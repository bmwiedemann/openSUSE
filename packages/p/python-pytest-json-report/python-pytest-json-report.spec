#
# spec file for package python-pytest-json-report
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
%define skip_python2 1
Name:           python-pytest-json-report
Version:        1.2.4
Release:        0
Summary:        A pytest plugin to report test results as JSON files
License:        MIT
URL:            https://github.com/numirias/pytest-json-report
Source:         https://files.pythonhosted.org/packages/source/p/pytest-json-report/pytest-json-report-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest-metadata}
BuildRequires:  %{python_module flaky}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest
Requires:       python-pytest-metadata
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin to report test results as JSON files

%prep
%setup -q -n pytest-json-report-%{version}

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
