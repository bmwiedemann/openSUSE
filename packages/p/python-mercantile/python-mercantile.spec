#
# spec file for package python-mercantile
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


Name:           python-mercantile
Version:        1.2.1
Release:        0
Summary:        Spherical mercator tile and coordinate utilities
License:        BSD-3-Clause
URL:            https://github.com/mapbox/mercantile
Source:         https://files.pythonhosted.org/packages/source/m/mercantile/mercantile-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 3.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 3.0}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
The mercantile module provides ul(xtile, ytile, zoom) and bounds(xtile, ytile, zoom)
functions that respectively return the upper left corner and bounding longitudes and
latitudes for XYZ tiles, a xy(lng, lat) function that returns spherical mercator
x and y coordinates, a tile(lng, lat, zoom) function that returns the tile containing
a given point, and quadkey conversion functions quadkey(xtile, ytile, zoom) and
quadkey_to_tile(quadkey) for translating between quadkey and tile coordinates.

%prep
%setup -q -n mercantile-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mercantile
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative mercantile

%postun
%python_uninstall_alternative mercantile

%files %{python_files}
%doc AUTHORS.txt CHANGES.txt README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/mercantile
%{python_sitelib}/mercantile
%{python_sitelib}/mercantile-%{version}*-info

%changelog
