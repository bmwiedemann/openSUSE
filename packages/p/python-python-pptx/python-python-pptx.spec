#
# spec file for package python-python-pptx
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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
Name:           python-python-pptx
Version:        1.0.2
Release:        0
Summary:        Generate and manipulate Open XML PowerPoint (pptx) files
License:        MIT
URL:            http://github.com/scanny/python-pptx
Source:         https://files.pythonhosted.org/packages/source/p/python-pptx/python_pptx-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#scanny/python-pptx#1104
Patch0:         support-new-pyparsing.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module lxml >= 3.1.0}
BuildRequires:  %{python_module Pillow >= 3.3.2}
BuildRequires:  %{python_module XlsxWriter >= 0.5.7}
BuildRequires:  %{python_module behave}
BuildRequires:  %{python_module pyparsing >= 2.0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 4.9.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Pillow >= 3.3.2
Requires:       python-XlsxWriter >= 0.5.7
Requires:       python-lxml >= 3.1.0
Requires:       python-typing_extensions >= 4.9.0
BuildArch:      noarch
%python_subpackages

%description
Create, read, and update PowerPoint 2007+ (.pptx) files.

%prep
%autosetup -p1 -n python_pptx-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%{python_sitelib}/pptx
%{python_sitelib}/python_pptx-%{version}.dist-info

%changelog
