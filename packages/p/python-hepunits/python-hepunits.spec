#
# spec file for package python-hepunits
#
# Copyright (c) 2020 SUSE LLC
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


%global modname hepunits

Name:           python-hepunits
Version:        2.0.1
Release:        0
Summary:        Units and constants in the HEP system of units
License:        BSD-3-Clause
URL:            https://github.com/scikit-hep/hepunits
Source:         https://files.pythonhosted.org/packages/source/h/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools > 42.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION For tests
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
hepunits collects the most commonly used units and constants in the HEP System
of Units, as derived from the basic units originally defined by the CLHEP
project.

%prep
%setup -q -n hepunits-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
