#
# spec file for package python-dbf
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dbf
Version:        0.99.3
Release:        0
Summary:        Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf
License:        BSD-3-Clause
URL:            https://pypi.org/project/dbf/
Source:         https://files.pythonhosted.org/packages/source/d/dbf/dbf-%{version}.tar.gz
BuildRequires:  %{python_module aenum}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aenum
Requires:       python-pytz
BuildArch:      noarch
%python_subpackages

%description
Pure python package for reading/writing dBase, FoxPro, and Visual FoxPro .dbf
files (including memos)

Currently supports dBase III, Clipper, FoxPro, and Visual FoxPro tables. Text is
returned as unicode, and codepage settings in tables are honored. Memos and Null
fields are supported.

%prep
%setup -q -n dbf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python dbf/test.py

%files %{python_files}
%license dbf/LICENSE
%{python_sitelib}/dbf-%{version}-py*.egg-info
%{python_sitelib}/dbf

%changelog
