#
# spec file for package python-pytest-pretty
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


Name:           python-pytest-pretty
Version:        1.2.0
Release:        0
Summary:        Pytest plugin for printing summary data as I want it
License:        MIT
URL:            https://github.com/samuelcolvin/pytest-pretty
Source:         https://github.com/samuelcolvin/pytest-pretty/archive/refs/tags/v%{version}.tar.gz#/pytest-pretty-%{version}-gh.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 7
Requires:       python-rich >= 12
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module rich >= 12}
# /SECTION
%python_subpackages

%description
Opinionated pytest plugin to make output slightly easier to read
and errors easy to find and fix.

%prep
%autosetup -p1 -n pytest-pretty-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_pretty
%{python_sitelib}/pytest_pretty-%{version}.dist-info

%changelog
