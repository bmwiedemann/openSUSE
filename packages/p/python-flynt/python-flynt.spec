#
# spec file for package python-flynt
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


%{?sle15_python_module_pythons}
Name:           python-flynt
Version:        1.0.1
Release:        0
Summary:        CLI tool to convert a python project's %-formatted strings to f-strings
License:        MIT
URL:            https://github.com/ikamensh/flynt
Source:         https://github.com/ikamensh/flynt/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astor
Requires:       python-tomli >= 1.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astor}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli >= 1.1.0}
# /SECTION
%python_subpackages

%description
CLI tool to convert a python project's %-formatted strings to f-strings.

%prep
%setup -q -n flynt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/flynt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative flynt

%postun
%python_uninstall_alternative flynt

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/flynt
%{python_sitelib}/flynt
%{python_sitelib}/flynt-%{version}*-info

%changelog
