#
# spec file for package python-xyzservices
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-xyzservices
Version:        2022.9.0
Release:        0
Summary:        Source of XYZ tiles providers
License:        BSD-3-Clause
URL:            https://xyzservices.readthedocs.io/
#Repo-URL:      https://github.com/geopandas/xyzservices
Source:         https://files.pythonhosted.org/packages/source/x/xyzservices/xyzservices-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       xyzservices-data = %{version}
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module mercantile}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
xyzservices is a lightweight library providing a repository
of available XYZ services offering raster basemap tiles.
The repository is provided via Python API and as a compressed
JSON file.

XYZ tiles can be used as background for your maps to provide
necessary spatial context. xyzservices offer specifications
of many tile services and provide an easy-to-use tools to
plug them into your work, no matter if interactive or static.

%package -n xyzservices-data
Summary:        Source of XYZ tiles providers - common data package

%description -n xyzservices-data
xyzservices is a lightweight library providing a repository
of available XYZ services offering raster basemap tiles.
The repository is provided via Python API and as a compressed
JSON file.

XYZ tiles can be used as background for your maps to provide
necessary spatial context. xyzservices offer specifications
of many tile services and provide an easy-to-use tools to
plug them into your work, no matter if interactive or static.

This package provides the common compressed JSON file for the
pythonXY-xyzservices packages.

%prep
%setup -q -n xyzservices-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -m "not request"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/xyzservices
%{python_sitelib}/xyzservices-%{version}*-info

%files -n xyzservices-data
%license LICENSE
%{_datadir}/xyzservices

%changelog
