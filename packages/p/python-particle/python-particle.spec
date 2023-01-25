#
# spec file for package python-particle
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


%global modname particle
%define skip_python2 1
%define skip_python36 1
Name:           python-particle
Version:        0.21.1
Release:        0
Summary:        PDG particle data and identification codes
License:        BSD-3-Clause
URL:            https://github.com/scikit-hep/particle
Source0:        https://files.pythonhosted.org/packages/source/p/particle/%{modname}-%{version}.tar.gz
# Downloaded separately from github using _service file
Source1:        tests.tar.xz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2
Requires:       python-hepunits >= 2.0.0
Recommends:     python-pandas
Recommends:     python-tabulate
BuildArch:      noarch
# SECTION For tests
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module hepunits}
BuildRequires:  %{python_module importlib_resources}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Particle provides a pythonic interface to the Particle Data Group (PDG)
particle data tables and particle identification codes.

%prep
%setup -q -n %{modname}-%{version}
%setup -q -D -n %{modname}-%{version} -a 1
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" src/particle/__main__.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand # Copy missed files
cp -R src/particle/data %{buildroot}%{$python_sitelib}/%{modname}/
cp -R src/particle/lhcb %{buildroot}%{$python_sitelib}/%{modname}/
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info/

%changelog
