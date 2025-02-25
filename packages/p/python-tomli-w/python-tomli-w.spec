#
# spec file for package python-tomli-w
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


%{?sle15_python_module_pythons}
Name:           python-tomli-w
Version:        1.2.0
Release:        0
Summary:        A lil' TOML writer
License:        MIT
URL:            https://github.com/hukkin/tomli-w
# prefer github archive over pypi sdist for pacakged tests
Source:         https://github.com/hukkin/tomli-w/archive/refs/tags/%{version}.tar.gz#/tomli-w-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Tomli-W is a Python library for writing TOML. It is a write-only counterpart to Tomli,
which is a read-only TOML parser.

%prep
%setup -q -n tomli-w-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/tomli_w
%{python_sitelib}/tomli_w-%{version}*-info

%check
%pytest

%changelog
