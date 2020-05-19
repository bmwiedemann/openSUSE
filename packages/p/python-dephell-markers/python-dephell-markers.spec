#
# spec file for package python-dephell-markers
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
Name:           python-dephell-markers
Version:        1.0.3
Release:        0
Summary:        Dephell library to use environment markers (PEP-496)
License:        MIT
URL:            https://github.com/dephell/dephell_markers
Source:         https://files.pythonhosted.org/packages/source/d/dephell_markers/dephell_markers-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2
Requires:       python-dephell-specifier
Requires:       python-packaging
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 19.2}
BuildRequires:  %{python_module dephell-specifier}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Dephell library to use environment markers (PEP-496).

%prep
%setup -q -n dephell_markers-%{version}
# https://github.com/dephell/dephell_markers/issues/6
sed -i '/package_dir/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
