#
# spec file for package python-python-louvain
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


%define         skip_python2 1
%define         skip_python36 1
%{?sle15_python_module_pythons}
Name:           python-python-louvain
Version:        0.16
Release:        0
Summary:        Louvain algorithm for community detection
License:        BSD-3-Clause
URL:            https://github.com/taynaud/python-louvain
Source0:        https://files.pythonhosted.org/packages/source/p/python-louvain/python-louvain-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-test-karate.patch gh#taynaud/python-louvain#95
Patch0:         fix-test-karate.patch
# PATCH-FIX-UPSTREAM tests-int-division.patch gh#taynaud/python-louvain#104
Patch1:         tests-int-division.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-networkx
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-community = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module networkx}
# /SECTION
%python_subpackages

%description
This module implements community detection.

It uses the louvain method described in Fast unfolding of
communities in large networks, Vincent D Blondel, Jean-Loup
Guillaume, Renaud Lambiotte, Renaud Lefebvre, Journal of
Statistical Mechanics: Theory and Experiment 2008(10), P10008 (12pp)

%prep
%autosetup -p1 -n python-louvain-%{version}

sed -i -e '/^#!\//, 1d' community/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/community
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v test_*.py

%post
%python_install_alternative community

%postun
%python_uninstall_alternative community

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/community
%{python_sitelib}/community
%{python_sitelib}/python_louvain-%{version}*-info

%changelog
