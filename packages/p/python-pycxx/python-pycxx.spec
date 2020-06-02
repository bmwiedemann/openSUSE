#
# spec file for package python-pycxx
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


%global modname pycxx
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
Name:           python-%{modname}
Version:        7.0.3
Release:        0
Summary:        Python extensions in C++
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://CXX.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cxx/%{modname}-%{version}.tar.gz
Patch0:         python-pycxx-7.0.3-python37.patch
Patch1:         python-pycxx-7.0.3-change-include-paths.patch
Patch2:         python-pycxx-7.0.3-setup.py.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Obsoletes:      python-cxx < %{version}
Provides:       python-cxx = %{version}
Obsoletes:      python-CXX < %{version}
Provides:       python-CXX = %{version}
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-cxx < %{version}
Provides:       %{oldpython}-cxx = %{version}
%endif
%python_subpackages

%description
PyCXX is a set of classes to help create extensions of Python in the
C++ language. The first part encapsulates the Python C API taking care
of exceptions and ref counting. The second part supports the building
of Python extension modules in C++.

%package devel
Summary:        Development files for %{modname} applications
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Obsoletes:      python-cxx-devel < %{version}
Provides:       python-cxx-devel = %{version}
Obsoletes:      python-CXX-devel < %{version}
Provides:       python-CXX-devel = %{version}
%ifpython2
Obsoletes:      %{oldpython}-cxx-devel < %{version}
Provides:       %{oldpython}-cxx-devel = %{version}
%endif

%description devel
PyCXX is a set of classes to help create extensions of Python in the
C++ language. The first part encapsulates the Python C API taking care
of exceptions and ref counting. The second part supports the building
of Python extension modules in C++.

%prep
%setup -q -n %{modname}-%{version}
%autopatch -p1

%build
%python_build
%ifpython3
rm -r Doc/Python2 && mv Doc/Python3 Doc/Python
%else
rm -r Doc/Python3 && mv Doc/Python2 Doc/Python
%endif

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYRIGHT
%doc README.html
%{python_sitelib}/CXX*

%files %{python_files devel}
%doc Doc/Python/
%ifpython3
%{_datadir}/python%{python3_bin_suffix}
%else
%{_datadir}/python%{python2_bin_suffix}
%endif
%{python_sysconfig_path include}

%changelog
