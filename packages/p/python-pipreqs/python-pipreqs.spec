#
# spec file for package python-pipreqs
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pipreqs
Version:        0.4.9
Release:        0
Summary:        Pip requirements generator based on imports in project
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/bndr/pipreqs
Source:         https://files.pythonhosted.org/packages/source/p/pipreqs/pipreqs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module nose}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docopt
Requires:       python-yarg
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module yarg}
# /SECTION
%python_subpackages

%description
Pip requirements.txt generator based on imports in project.

%prep
%setup -q -n pipreqs-%{version}
chmod a-x pipreqs/pipreqs.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Ignore four tests that require network access
%python_exec -m nose -e 'test_(get_imports_info|ignored_directory|init_)'

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%python3_only %{_bindir}/pipreqs
%{python_sitelib}/*

%changelog
