#
# spec file for package python-cucumber-expressions
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-cucumber-expressions
Version:        18.0.1
Release:        0
Summary:        Cucumber Expressions - a simpler alternative to Regular Expressions
License:        MIT
URL:            https://github.com/cucumber/cucumber-expressions
Source:         https://github.com/cucumber/cucumber-expressions/archive/refs/tags/v%{version}.tar.gz#/cucumber-expressions-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Cucumber Expressions for Python, a simpler alternative to Regular
Expressions.

The main docs are here:
https://github.com/cucumber/cucumber-expressions#readme

%prep
%autosetup -p1 -n cucumber-expressions-%{version}
cp -r testdata/ python/

%build
cd python
%pyproject_wheel

%install
cd python
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd python
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cucumber_expressions
%{python_sitelib}/cucumber_expressions-%{version}.dist-info

%changelog
