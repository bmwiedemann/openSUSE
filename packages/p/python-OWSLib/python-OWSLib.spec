#
# spec file for package python-OWSLib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Angelos Tzotsos <tzotsos@opensuse.org>
# Copyright (c) 2018 Ioda-Net Sàrl, Bruno Friedmann, Charmoille, Switzerland.
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
%define         oldpython python
Name:           python-OWSLib 
Version:        0.17.1
Release:        0
Summary:        Python interface to OGC Web Services
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            http://geopython.github.com/OWSLib/
Source:         https://files.pythonhosted.org/packages/source/O/OWSLib/OWSLib-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 1.5
Requires:       python-pyproj
Requires:       python-pytz
Requires:       python-requests >= 1.0
Provides:       python-owslib = %{version}
Obsoletes:      python-owslib < %{version}
%ifpython2
Provides:       %{oldpython}-pymodis = %{version}
Obsoletes:      %{oldpython}-pymodis < %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
OWSLib is a Python package for client programming with Open Geospatial
Consortium (OGC) web service (hence OWS) interface standards, and their
related content models.

%prep
%setup -q -n OWSLib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%files %python_files
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
