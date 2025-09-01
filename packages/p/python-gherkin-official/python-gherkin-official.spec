#
# spec file for package python-gherkin-official
#
# Copyright (c) 2025 SUSE LLC
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


# PyPi name
Name:           python-gherkin-official
Version:        33.0.0
Release:        0
Summary:        Gherkin parser (official, by Cucumber team)
License:        MIT
URL:            https://github.com/cucumber/gherkin
Source:         https://github.com/cucumber/gherkin/archive/refs/tags/v%{version}.tar.gz#/gherkin-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module typing_extensions >= 4}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing_extensions >= 4
# Module name
Provides:       python-gherkin = %{version}
BuildArch:      noarch
%python_subpackages

%description
Parser and compiler for the Gherkin language.

%prep
%autosetup -p1 -n gherkin-%{version}

%build
pushd python
%pyproject_wheel
popd

%install
pushd python
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd python
%pytest
popd

%files %{python_files}
%doc python/README.md
%license LICENSE
%{python_sitelib}/gherkin
%{python_sitelib}/gherkin_official-%{version}.dist-info

%changelog
