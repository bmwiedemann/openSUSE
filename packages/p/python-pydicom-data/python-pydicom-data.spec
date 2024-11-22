#
# spec file for package python-pydicom-data
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


%{?sle15allpythons}
Name:           python-pydicom-data
Version:        1.0.0
Release:        0
Summary:        Test files for pydicom
License:        MIT
URL:            https://github.com/pydicom/pydicom-data/
Source:         https://files.pythonhosted.org/packages/source/p/pydicom-data/pydicom-data-%{version}.tar.gz
Patch1:         pytest8.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Test files used by pydicom and other packages by the same organisation.

%prep
%autosetup -p1 -n pydicom-data-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/data_store
%{python_sitelib}/pydicom_data-%{version}.dist-info

%changelog
