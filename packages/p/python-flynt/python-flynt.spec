#
# spec file for package python-flynt
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
Name:           python-flynt
Version:        0.76
Release:        0
Summary:        CLI tool to convert a python project's %-formatted strings to f-strings
License:        MIT
URL:            https://github.com/ikamensh/flynt
Source:         https://files.pythonhosted.org/packages/source/f/flynt/flynt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
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
%{python_sitelib}/*

%changelog
