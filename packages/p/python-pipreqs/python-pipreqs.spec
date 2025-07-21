#
# spec file for package python-pipreqs
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
%{?sle15_python_module_pythons}
Name:           python-pipreqs
Version:        0.4.13
Release:        0
Summary:        Pip requirements generator based on imports in project
License:        Apache-2.0
URL:            https://github.com/bndr/pipreqs
Source:         https://files.pythonhosted.org/packages/source/p/pipreqs/pipreqs-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pipreqs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Ignore tests that require network access
%pytest -k 'not (test_get_imports_info or test_ignored_directory or test_init or test_init_overwrite or teset_init_savepath or test_omit_version or test_clean or test_dynamic_version)'

%pre
%python_libalternatives_reset_alternative pipreqs

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/pipreqs
%{python_sitelib}/pipreqs
%{python_sitelib}/pipreqs-%{version}.dist-info

%changelog
