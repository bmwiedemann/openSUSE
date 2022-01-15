#
# spec file for package python-fann2
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-fann2
Version:        1.2.0
Release:        0
Summary:        Fast Artificial Neural Network Library (fann) bindings
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://github.com/FutureLinkCorporation/fann2
Source:         https://github.com/FutureLinkCorporation/fann2/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(fann)

%python_subpackages

%description
Python bindings for Fast Artificial Neural Networks 2.2.0 (FANN >= 2.2.0)
that implements multilayer artificial neural networks with support for both
fully-connected and sparsely-connected networks. It includes a framework
for easy handling of training data sets.

These are the original python bindings included with FANN 2.1.0beta and
updated to include support for python 2.x/3.x .

%prep
%setup -q -n fann2-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/fann2/fann2_wrap.cxx
%python_expand rm %{buildroot}%{$python_sitearch}/fann2/fann_cpp_subclass.h

#%%check - no tests exist upstream
# https://github.com/FutureLinkCorporation/fann2/issues/30

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
