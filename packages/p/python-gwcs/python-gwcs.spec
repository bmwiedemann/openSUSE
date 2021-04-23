#
# spec file for package python-gwcs
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
# Astropy dropped Python 3.6 
# But gwcs still supports it, so keep the -base, requirement below for potential Leap backports
%define skip_python36 1
Name:           python-gwcs
Version:        0.16.1
Release:        0
Summary:        Generalized World Coordinate System
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://gwcs.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/source/g/gwcs/gwcs-%{version}.tar.gz
BuildRequires:  %{python_module asdf}
BuildRequires:  %{python_module astropy >= 4.1}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asdf
Requires:       python-astropy >= 4.1
Requires:       python-numpy
Requires:       python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
An Astropy affiliated package providing tools for managing the
World Coordinate System of astronomical data.

%prep
%setup -q -n gwcs-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the schema tests do not tolerate numpy 1.20 deprecation warnings. Already fixed upstream, but patch is too unspecific
# gh#spacetelescope/gwcs#353
%pytest -ra -k "not (schemas and (label_mapper or regions_selector))"

%files %{python_files}
%doc README.rst
%license licenses/LICENSE.rst licenses/README.rst
%{python_sitelib}/gwcs
%{python_sitelib}/gwcs-%{version}-py*.egg-info

%changelog
