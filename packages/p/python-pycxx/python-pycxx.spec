#
# spec file for package python-pycxx
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# Note PyPI 'pycxx' is a different package,
# and this package is not 'cxx' or 'CXX' on PyPI
%global modname pycxx
%define oldpython python
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        7.1.8
Release:        0
Summary:        Python extensions in C++
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://CXX.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cxx/%{modname}-%{version}.tar.gz
Patch1:         python-pycxx-7.0.3-change-include-paths.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel
%ifpython2
rm -r Doc/Python3 && mv Doc/Python2 Doc/Python
%else
rm -r Doc/Python2 && mv Doc/Python3 Doc/Python
%endif

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{python_expand mkdir -p %{buildroot}%{_datadir}/python%{$python_bin_suffix}
cp -r %{buildroot}/usr/CXX %{buildroot}%{_datadir}/python%{$python_bin_suffix}
}
rm -r %{buildroot}/usr/CXX

%files %{python_files}
%license COPYRIGHT
%doc README.html
%{python_sitelib}/CXX*
%{python_sitelib}/[Cc][Xx][Xx]-%{version}*-info

%files %{python_files devel}
%doc Doc/Python/
%{_datadir}/python%{python_bin_suffix}
%{python_sysconfig_path include}

%changelog
