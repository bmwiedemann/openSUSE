#
# spec file for package python-conway-polynomials
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-conway-polynomials
Version:        0.10
Release:        0
Summary:        Python interface to Frank Lübeck's Conway polynomial database
License:        GPL-3.0-or-later
URL:            https://github.com/sagemath/conway-polynomials
Source:         https://files.pythonhosted.org/packages/source/c/conway-polynomials/conway_polynomials-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Python interface to Frank Lübeck's Conway polynomial database

%prep
%autosetup -p1 -n conway_polynomials-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/conway_polynomials
%{python_sitelib}/conway_polynomials-%{version}.dist-info

%changelog
