#
# spec file for package python-uproot
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

# No numpy for py3.6
%define skip_python36 1
%global modname uproot
Name:           python-uproot
Version:        4.0.0
Release:        0
Summary:        ROOT I/O in pure Python and Numpy
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scikit-hep/uproot4
Source0:        https://files.pythonhosted.org/packages/source/u/uproot/uproot-%{version}.tar.gz
Source1:        tests.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.13.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module importlib-resources}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy >= 1.13.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-hep-testdata}
BuildRequires:  %{python_module xxhash}
# /SECTION
%python_subpackages

%description
Uproot is a reader and a writer of the ROOT file format using only Python and
Numpy. Unlike the standard C++ ROOT implementation, Uproot is only an I/O
library, primarily intended to stream data into machine learning libraries in
Python. It uses Numpy to cast blocks of data from the ROOT file as Numpy
arrays.

%prep
%autosetup -p1 -n %{modname}-%{version}
%setup -q -D -T -a 1 -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip tests requiring network
%pytest -k 'not (test_http or test_fallback or test_no_multipart or test_0066 or test_0088 or test_0220)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
