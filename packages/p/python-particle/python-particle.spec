#
# spec file for package python-particle
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


%global modname particle
%define skip_python2 1
Name:           python-particle
Version:        0.13.0
Release:        0
Summary:        PDG particle data and identification codes
License:        BSD-3-Clause
URL:            https://github.com/scikit-hep/particle
Source:         https://files.pythonhosted.org/packages/source/p/particle/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2
Requires:       python-hepunits >= 2.0.0
Recommends:     python-pandas
Recommends:     python-tabulate
BuildArch:      noarch
%python_subpackages

%description
Particle provides a pythonic interface to the Particle Data Group (PDG)
particle data tables and particle identification codes.

%prep
%setup -q -n particle-%{version}
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" src/particle/__main__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# NO TESTS DEFINED
#%%check

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
