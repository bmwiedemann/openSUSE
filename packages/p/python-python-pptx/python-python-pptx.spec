#
# spec file for package python-python-pptx
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-python-pptx
Version:        0.6.23
Release:        0
Summary:        Generate and manipulate Open XML PowerPoint (pptx) files
License:        MIT
URL:            http://github.com/scanny/python-pptx
Source:         https://files.pythonhosted.org/packages/source/p/python-pptx/python-pptx-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/scanny/python-pptx/pull/957 Use UTC-aware datetime objects
Patch:          utc.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module lxml >= 3.1.0}
BuildRequires:  %{python_module Pillow >= 3.3.2}
BuildRequires:  %{python_module XlsxWriter >= 0.5.7}
BuildRequires:  %{python_module behave}
BuildRequires:  %{python_module pyparsing >= 2.0.1}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Pillow >= 3.3.2
Requires:       python-XlsxWriter >= 0.5.7
Requires:       python-lxml >= 3.1.0
BuildArch:      noarch
%python_subpackages

%description
Generate and manipulate Open XML PowerPoint (.pptx) files.

%prep
%autosetup -p1 -n python-pptx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%{python_sitelib}/*pptx*

%changelog
