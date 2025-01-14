#
# spec file for package python-pycountry
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


%{?sle15_python_module_pythons}
Name:           python-pycountry
Version:        23.12.11
Release:        0
Summary:        Databases for ISO standards 639 3166 3166-2 4217 15924
License:        LGPL-2.1-only
URL:            https://pypi.python.org/pypi/pycountry/
Source:         https://pypi.io/packages/source/p/pycountry/pycountry-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module importlib-metadata}
# /SECTION
%python_subpackages

%description
pycountry provides the ISO databases for the standards 639 (Languages),
3166 (Countries), 3166-2 (Subdivisions of countries), 4217 (Currencies),
15924 (Scripts). The databases are imported from Debian's pkg-isocodes,
packaged into pycountry and made accessible through a Python API.
Translation files for the various strings are included as well.

%prep
%setup -q -n pycountry-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/pycountry
%{python_sitelib}/pycountry-%{version}.dist-info

%changelog
