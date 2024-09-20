#
# spec file for package python-executing
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-executing
Version:        2.1.0
Release:        0
Summary:        Get the currently executing AST node of a frame, and other information
License:        MIT
URL:            https://github.com/alexmojaki/executing
Source:         https://files.pythonhosted.org/packages/source/e/executing/executing-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/alexmojaki/executing/pull/86 fix: backward compatibility fix for changed source positions in 3.12.6
Patch0:         new-python-312.patch
BuildRequires:  %{python_module asttokens}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module littleutils}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm >= 4.0.0}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Get the currently executing AST node of a frame, and other information

%prep
%autosetup -p1 -n executing-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/executing
%{python_sitelib}/executing-%{version}.dist-info

%changelog
