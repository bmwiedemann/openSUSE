#
# spec file for package python-o2sclpy
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


%define modname o2sclpy
%{?sle15_python_module_pythons}
Name:           python-o2sclpy
Version:        0.930
Release:        0
Summary:        Python extensions for O2scl
License:        GPL-3.0-only
URL:            https://neutronstars.utk.edu/code/o2sclpy
Source0:        https://files.pythonhosted.org/packages/source/o/o2sclpy/%{modname}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module matplotlib >= 3.1}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module yt}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION Tests
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module normflows}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module torch}
BuildRequires:  o2scl-devel >= %{version}
# /SECTION
Requires:       o2scl-devel >= %{version}
Requires:       python-matplotlib >= 3.1
Requires:       python-numpy
Requires:       python-yt
Requires:       texlive-latex
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-normflows
Recommends:     python-torch
BuildArch:      noarch
%python_subpackages

%description
A high-level plotting script, o2graph, for quick matplotlib or yt plots for use
with the O2scl C++ library and a set of python classes for convenient plotting.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/o2graph
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# TMPDIR with write permissions
export TMPDIR=`mktemp -d -p ./`
# test_interpm requires tensorflow, unavailable as package for oS
# test_classify fails on aarch64 https://github.com/awsteiner/o2sclpy/issues/3
%pytest -k "not (test_interpm or test_classify)"

%post
%python_install_alternative o2graph

%postun
%python_uninstall_alternative o2graph

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/o2graph
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}*.*-info/

%changelog
