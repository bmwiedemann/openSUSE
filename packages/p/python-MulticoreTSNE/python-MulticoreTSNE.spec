#
# spec file for package python-MulticoreTSNE
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
# TW does not have python36-scipy (SciPy 1.6.0 does not support it)
%define skip_python36 1
Name:           python-MulticoreTSNE
Version:        0.1
Release:        0
Summary:        Multicore version of t-SNE algorithm
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/DmitryUlyanov/Multicore-TSNE
Source:         https://files.pythonhosted.org/packages/source/M/MulticoreTSNE/MulticoreTSNE-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_sklearn.patch gh#DmitryUlyanov/Multicore-TSNE#90 mcepl@suse.com
# signature of sklearn.datasets.make_blogs changed
Patch0:         fix_sklearn.patch
Patch1:         test-tsne.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cffi
Requires:       python-numpy
Recommends:     python-scikit-learn
Recommends:     python-scipy
# SECTION test requirements
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
This is a multicore modification of Barnes-Hut t-distributed
Stochastic Neighbor Embedding (t-SNE). It is implemented using Python
and Torch CFFI-based wrappers.

%prep
%autosetup -p1 -n MulticoreTSNE-%{version}

# fix optflags
sed -i \
    -e 's:-O3 -fPIC -ffast-math -funroll-loops:%optflags:' \
    multicore_tsne/CMakeLists.txt
# fix cmake flags
sed -i 's/self.cmake_args or "--"/self.cmake_args or ""/' setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd MulticoreTSNE/tests
%pyunittest_arch discover -v
popd

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/MulticoreTSNE
%{python_sitearch}/MulticoreTSNE-%{version}*-info

%changelog
