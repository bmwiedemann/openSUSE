#
# spec file for package python-fann2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-fann2
Version:        1.1.2
Release:        0
License:        LGPL-2.1
Summary:        Fast Artificial Neural Network Library (fann) bindings
Url:            https://github.com/FutureLinkCorporation/fann2
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/f/fann2/fann2-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(fann)
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module nose > 1.3.0}
%endif
# /SECTION
BuildRequires:  unzip
BuildRequires:  fdupes
BuildRequires:  swig

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

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc LICENSE README.rst
%{python_sitearch}/*

%changelog
