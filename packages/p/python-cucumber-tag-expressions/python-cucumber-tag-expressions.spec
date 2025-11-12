#
# spec file for package python-cucumber-tag-expressions
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


Name:           python-cucumber-tag-expressions
Version:        8.0.0
Release:        0
Summary:        Provides a tag-expression parser and evaluation logic for cucumber/behave
License:        MIT
URL:            https://github.com/cucumber/tag-expressions
Source:         https://files.pythonhosted.org/packages/source/c/cucumber-tag-expressions/cucumber_tag_expressions-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 6.0.1}
BuildRequires:  %{python_module PyYAML >= 6.0.3}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Provides tag-expression parser for cucumber/behave.

%prep
%autosetup -p1 -n cucumber_tag_expressions-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest "--doctest-glob=README.md"

%files %{python_files}
%doc README.md
%license LICENSE LICENSE
%{python_sitelib}/cucumber_tag_expressions
%{python_sitelib}/cucumber_tag_expressions-%{version}.dist-info

%changelog
