#
# spec file for package python-zc.buildout
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-zc.buildout
Version:        4.1.11
Release:        0
Summary:        System for managing development buildouts
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zc.buildout
Source:         https://github.com/buildout/buildout/archive/refs/tags/%{version}.tar.gz#/zc_buildout-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-packaging >= 23.2
Requires:       python-pip
Requires:       python-setuptools >= 49
Requires:       python-wheel
Provides:       python-zc_buildout = %{version}
Obsoletes:      python-zc_buildout < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module zope.testing}
# /SECTION
%python_subpackages

%description
System for managing development buildouts.

Buildout is a project designed to solve 2 problems:
 * Application-centric assembly and deployment
 * Repeatable assembly of programs from Python software distributions

%prep
%setup -q -n buildout-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/buildout
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python src/zc/buildout/tests/test_all.py

%pre
%python_libalternatives_reset_alternative buildout

%files %{python_files}
%doc README.rst CHANGES.rst COPYRIGHT.txt
%license LICENSE.txt
%dir %{python_sitelib}/zc
%{python_sitelib}/zc/buildout
%{python_sitelib}/zc.buildout-%{version}-py*-nspkg.pth
%{python_sitelib}/zc[._]buildout-%{version}.dist-info
%python_alternative %{_bindir}/buildout

%changelog
