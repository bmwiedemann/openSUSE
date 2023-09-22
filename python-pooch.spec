#
# spec file for package python-pooch
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
Name:           python-pooch
Version:        1.7.0
Release:        0
Summary:        Manager for Python libraries' sample data files
License:        BSD-3-Clause
URL:            https://github.com/fatiando/pooch
Source:         https://files.pythonhosted.org/packages/source/p/pooch/pooch-%{version}.tar.gz
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
Requires:       python-platformdirs
Requires:       python-requests
Suggests:       python-paramiko
Suggests:       python-tqdm
BuildArch:      noarch
%python_subpackages

%description
Pooch manages sample data files for Python libraries. It automatically
downloads and stores them in a local directory, with support for versioning
and checks for corruption.

%prep
%autosetup -p1 -n pooch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# These test the online functionality
donttest+=" or (test_core and test_load_registry_from_doi)"
donttest+=" or (test_core and test_check_availability)"
donttest+=" or (test_downloaders and test_doi)"
donttest+=" or (test_downloaders and test_figshare)"
donttest+=" or (test_downloaders and test_invalid_doi_repository)"
%pytest -k "not (${donttest:4})" -m 'not network'

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE.txt
%{python_sitelib}/pooch
%{python_sitelib}/pooch-%{version}.dist-info

%changelog
