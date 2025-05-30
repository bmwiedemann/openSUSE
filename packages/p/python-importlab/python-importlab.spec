#
# spec file for package python-importlab
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


%define         skip_python2 1
# python36-networkx no longer exists in Tumbleweed (due to SciPy following NEP 29)
%define         skip_python36 1
Name:           python-importlab
Version:        0.8.1
Release:        0
Summary:        A library to calculate python dependency graphs
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/google/importlab
Source:         https://files.pythonhosted.org/packages/source/i/importlab/importlab-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-networkx
Requires(post): alts
Requires(postun): alts
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module networkx}
# /SECTION
%python_subpackages

%description
A library to calculate python dependency graphs.

%prep
%setup -q -n importlab-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/importlab
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative importlab

%postun
%python_uninstall_alternative importlab

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%python_alternative %{_bindir}/importlab
%{python_sitelib}/importlab
%{python_sitelib}/importlab-%{version}*-info

%changelog
