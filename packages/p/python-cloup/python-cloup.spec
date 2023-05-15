#
# spec file for package python-cloup
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


Name:           python-cloup
Version:        2.1.0
Release:        0
Summary:        Option groups, constraints, subcommand sections and help themes for Click
License:        BSD-3-Clause
URL:            https://github.com/janLuke/cloup
Source:         https://files.pythonhosted.org/packages/source/c/cloup/cloup-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 8.0
Suggests:       python-typing_extensions
BuildArch:      noarch
%python_subpackages

%description
This module adds features to python-click: option groups,
constraints, subcommand sections and help themes.

%prep
%autosetup -n cloup-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%dir %{python_sitelib}/cloup
%{python_sitelib}/cloup
%{python_sitelib}/cloup-%{version}*-info

%changelog
