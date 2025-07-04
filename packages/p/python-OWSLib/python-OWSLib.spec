#
# spec file for package python-OWSLib
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2015 Angelos Tzotsos <tzotsos@opensuse.org>
# Copyright (c) 2021 Ioda-Net Sàrl, Bruno Friedmann, Charmoille, Switzerland.
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
Name:           python-OWSLib
Version:        0.31.0
Release:        0
Summary:        Python interface to OGC Web Services
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://owslib.readthedocs.io/
# get the test suite form Github
Source:         https://github.com/geopython/OWSLib/archive/refs/tags/%{version}.tar.gz#/OWSLib-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-lxml
Requires:       python-python-dateutil >= 1.5
Requires:       python-pytz
Requires:       python-requests >= 1.0
Provides:       python-owslib = %{version}
Obsoletes:      python-owslib < %{version}
# SECTION test
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 1.5}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 1.0}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
OWSLib is a Python package for client programming with Open Geospatial
Consortium (OGC) web service (hence OWS) interface standards, and their
related content models.

%prep
%setup -q -n OWSLib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# override tox.ini: no doctest no cov, register own mark
echo '[pytest]
markers =
    online
' > pytest.ini
donttest="     (TestOffline and test_wfs_110_remotemd_parse_all)"
donttest+=" or (TestOffline and test_wfs_110_remotemd_parse_single)"
donttest+=" or (TestOffline and test_wfs_200_remotemd_parse_all)"
donttest+=" or (TestOffline and test_wfs_200_remotemd_parse_single)"
donttest+=" or (TestOffline and test_wms_130_remotemd_parse_all)"
donttest+=" or (TestOffline and test_wms_130_remotemd_parse_single)"
# online but not marked
donttest+=" or test_wmts_example_informatievlaanderen"
%pytest -s -m "not online" -k "not ($donttest)"

%files %python_files
%doc AUTHORS.rst README.md SECURITY.md
%license LICENSE
%{python_sitelib}/owslib
%{python_sitelib}/[Oo][Ww][Ss][Ll]ib-%{version}*-info

%changelog
