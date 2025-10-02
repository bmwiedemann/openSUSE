#
# spec file for package python-maison
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


%bcond_without libalternatives
Name:           python-maison
Version:        2.0.0
Release:        0
Summary:        Read settings from config files
License:        MIT
URL:            https://github.com/dbatten5/maison
Source:         https://files.pythonhosted.org/packages/source/m/maison/maison-%{version}.tar.gz
BuildRequires:  alts
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.0.1}
BuildRequires:  %{python_module toml >= 0.10.2}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       alts
Requires:       python-click >= 8.0.1
Requires:       python-toml >= 0.10.2
BuildArch:      noarch
%python_subpackages

%description
`maison` aims to provide a simple and flexible way to read and validate those
configuration options so that they may be used in the package.

%prep
%autosetup -p1 -n maison-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/maison
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/maison
%{python_sitelib}/maison
%{python_sitelib}/maison-%{version}.dist-info

%changelog
