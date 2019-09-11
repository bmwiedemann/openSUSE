#
# spec file for package python-dephell-pythons
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-dephell-pythons
Version:        0.1.10
Release:        0
License:        MIT
Summary:        Dephell library to manage python versions
Url:            https://github.com/dephell/dephell_pythons
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/dephell-pythons/dephell_pythons-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module dephell-specifier}
BuildRequires:  %{python_module packaging}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs
Requires:       python-dephell-specifier
Requires:       python-packaging
BuildArch:      noarch

%python_subpackages

%description
Dephell library to manage python versions.

%prep
%setup -q -n dephell_pythons-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
