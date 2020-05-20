#
# spec file for package python-python-louvain
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-python-louvain
Version:        0.13
Release:        0
Summary:        Louvain algorithm for community detection
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/taynaud/python-louvain
Source0:        https://files.pythonhosted.org/packages/source/p/python-louvain/python-louvain-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-networkx
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%setup -q -n python-louvain-%{version}
sed -i -e '/^#!\//, 1d' community/__init__.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/community
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_community.py

%post
%python_install_alternative community

%postun
%python_uninstall_alternative community

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/community
%{python_sitelib}/*

%changelog
