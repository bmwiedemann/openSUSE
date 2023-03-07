#
# spec file for package python-fasttext
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname fastText
# Using annotation futures and dataclasses
%define skip_python36 1
Name:           python-fasttext
Version:        0.9.2
Release:        0
Summary:        Library for fast text representation and classification
License:        MIT
URL:            https://github.com/facebookresearch/fastText
Source:         https://github.com/facebookresearch/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
Patch0:         reproducible.patch
Patch1:         gcc13-fix.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pybind11 >= 2.2}
BuildRequires:  %{python_module setuptools >= 0.7.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numpy
Requires:       python-pybind11 >= 2.2
Requires:       python-setuptools >= 0.7.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
fastText is a library for efficient learning of word
representations and sentence classification.

%prep
%autosetup -p1 -n %{modname}-%{version}

sed -Ei "1{/^#!\/usr\/bin\/env python/d}" \
    python/fasttext_module/fasttext/util/util.py

%build
export CXXFLAGS="%{optflags}" CFLAGS="%{optflags}"
%make_build

%pyproject_wheel

%install
%pyproject_install
%{python_expand :
install -Dpm 0755 fasttext %{buildroot}%{_bindir}/fasttext
%python_clone -a %{buildroot}%{_bindir}/fasttext
%fdupes %{buildroot}%{$python_sitearch}
}

%check
# Tests require 300+MB test data

%post
%python_install_alternative fasttext

%postun
%python_uninstall_alternative fasttext

%files %{python_files}
%doc README.md docs/
%license LICENSE
# fasttext.pc.in
%python_alternative %{_bindir}/fasttext
%{python_sitearch}/fasttext
%{python_sitearch}/fasttext-%{version}*-info
%{python_sitearch}/fasttext_pybind.*.so

%changelog
