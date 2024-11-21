#
# spec file for package python-RTFDE
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 LISA GmbH, Bingen, Germany
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
Name:           python-RTFDE
Version:        0.1.1
Release:        0
Summary:        A library for extracting HTML content from RTF encapsulated HTML
License:        LGPL-3.0-or-later
URL:            https://github.com/seamustuohy/RTFDE
Source:         https://files.pythonhosted.org/packages/source/R/RTFDE/RTFDE-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module lark >= 1.1.8}
BuildRequires:  %{python_module oletools >= 0.56}
# /SECTION
BuildRequires:  fdupes
Requires:       python-lark >= 1.1.8
Requires:       python-oletools >= 0.56
Suggests:       python-lxml >= 4.6
Suggests:       python-mypy >= 1.1.1
Suggests:       python-pdoc3 >= 0.10.0
Suggests:       python-coverage >= 7.2.2
Suggests:       python-extract_msg >= 0.27
BuildArch:      noarch
%python_subpackages

%description
A library for extracting HTML content from RTF encapsulated HTML as commonly found in the exchange MSG email format.

%prep
%autosetup -p1 -n RTFDE-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# TODO: fetch tests/test_data separately, it is not packaged
#%%check
#%%pyunittest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/RTFDE
%{python_sitelib}/RTFDE-%{version}.dist-info

%changelog
