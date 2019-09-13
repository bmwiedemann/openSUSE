#
# spec file for package python-MulticoreTSNE
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-MulticoreTSNE
Version:        0.1
Release:        0
Summary:        Multicore version of t-SNE algorithm
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/DmitryUlyanov/Multicore-TSNE
Source:         https://files.pythonhosted.org/packages/source/M/MulticoreTSNE/MulticoreTSNE-%{version}.tar.gz
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
%setup -q -n MulticoreTSNE-%{version}
# fix optflags
sed -i \
    -e 's:-O3 -fPIC -ffast-math -funroll-loops:%optflags:' \
    multicore_tsne/CMakeLists.txt

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd MulticoreTSNE/tests
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -m unittest discover -v
}
popd

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitearch}/*

%changelog
