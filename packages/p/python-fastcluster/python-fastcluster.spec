#
# spec file for package python-fastcluster
#
# Copyright (c) 2021 SUSE LLC
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


%define         skip_python36 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-fastcluster
Version:        1.1.28
Release:        0
Summary:        Hierarchical clustering routines for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/dmuellner/fastcluster
Source:         https://files.pythonhosted.org/packages/source/f/fastcluster/fastcluster-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip_error_test.patch gh#dmuellner/fastcluster#21 mcepl@suse.com
# Skip over erroring test
Patch0:         skip_error_test.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.9}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-scipy
%python_subpackages

%description
This library provides Python functions for hierarchical clustering.
It generates hierarchical clusters from distance matrices or from
vector data.

Part of this module is intended to replace the functions
linkage, single, complete, average, weighted, centroid, median, ward
in the module scipy.cluster.hierarchy with the same functionality but
much faster algorithms. Moreover, the function 'linkage_vector'
provides memory-efficient clustering for vector data.

The interface is very similar to MATLAB's Statistics Toolbox API to
make code easier to port from MATLAB to Python/Numpy. The core
implementation of this library is in C++ for efficiency.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module fastcluster-doc = %{version}}

%description -n %{name}-doc
Documentation and help files for %{name}.

%prep
%autosetup -p1 -n fastcluster-%{version}

sed -i 's/\r$//' CITATION.txt
sed -i 's/\r$//' NEWS.txt
sed -i 's/\r$//' README.txt

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG=en_US.UTF-8
%pyunittest_arch -v tests

%files %{python_files}
%license COPYING.txt
%doc CITATION.txt NEWS.txt README.txt
%{python_sitearch}/*

%files -n %{name}-doc
%doc docs/fastcluster.pdf

%changelog
