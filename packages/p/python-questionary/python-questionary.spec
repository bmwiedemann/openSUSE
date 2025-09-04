#
# spec file for package python-questionary
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


%{?sle15_python_module_pythons}
Name:           python-questionary
Version:        2.1.1
Release:        0
Summary:        Library for effortlessly building pretty command line interfaces
License:        MIT
URL:            https://github.com/tmbo/questionary
Source:         https://files.pythonhosted.org/packages/source/q/questionary/questionary-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-prompt-toolkit
BuildArch:      noarch
%python_subpackages

%description
A Python library for effortlessly building pretty command line interfaces.

%prep
%setup -q -n questionary-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# PyPi tarball doesn't contain any tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/questionary
%{python_sitelib}/questionary-%{version}.dist-info

%changelog

