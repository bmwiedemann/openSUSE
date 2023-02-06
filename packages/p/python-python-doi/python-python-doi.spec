#
# spec file for package python-python-doi
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


Name:           python-python-doi
Version:        0.2.0
Release:        0
Summary:        Python package to work with Document Object Identifier (doi)
License:        GPL-3.0-only
URL:            https://github.com/papis/python-doi
Source:         https://files.pythonhosted.org/packages/source/p/python-doi/python-doi-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mark-network-tests.patch gh#alejandrogallo/python-doi#1 mcepl@suse.com
# mark tests requiring network access for their exclusion
Patch0:         mark-network-tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-sphinx
Suggests:       python-sphinx-autobuild
Suggests:       python-sphinx-autodoc-typehints
Suggests:       python-sphinx_rtd_theme
BuildArch:      noarch
%python_subpackages

%description
Python package to work with Document Object Identifier (doi)

%prep
%autosetup -p1 -n python-doi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not net'

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/doi
%{python_sitelib}/python_doi-%{version}*-info

%changelog
