#
# spec file for package python-perky
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-perky
Version:        0.10
Release:        0
Summary:        A parser for the perky text file format
License:        MIT
URL:            https://github.com/larryhastings/perky/
Source:         https://files.pythonhosted.org/packages/source/p/perky/perky-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Use PEP 621 metadata and flit-core
Patch0:         switch-to-flit-core.patch
BuildRequires:  %{python_module big >= 0.14}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-big >= 0.14
BuildArch:      noarch
%python_subpackages

%description
An "rcfile" text file format for Python programs solving the same
problem as "INI" files, "TOML" files, and "JSON" files.

%prep
%autosetup -p1 -n perky-%{version}
sed -i '1{/\/usr\/bin\/env python*/d;}' perky/utility.py perky/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests need to be executed directly, otherwise (pytest, unittest discover) they fail
%python_exec tests/test_perky.py -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/perky/
%{python_sitelib}/perky-%{version}.dist-info

%changelog
