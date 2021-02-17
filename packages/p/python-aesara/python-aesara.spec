#
# spec file for package python-aesara
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


# Python 2 unsupported by aesara
%define skip_python2 1
#
# No numpy, scipy for 3.6
%define skip_python36 1
#
%define modname aesara
Name:           python-aesara
Version:        2.0.0
Release:        0
Summary:        Effeciently evaluate expressions involving multi-dimensional arrays
License:        BSD-3-Clause
URL:            https://github.com/pymc-devs/aesara
Source0:        https://files.pythonhosted.org/packages/source/a/aesara/aesara-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module numpy >= 1.9.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.14}
# /SECTION
BuildRequires:  fdupes
Requires:       python-filelock
Requires:       python-numpy >= 1.9.1
Requires:       python-scipy >= 0.14
BuildArch:      noarch
%python_subpackages

%description
Aesara is a Python library that allows you to define, optimize, and efficiently
evaluate mathematical expressions involving multi-dimensional arrays. It can
use GPUs and perform efficient symbolic differentiation.

This is a fork of the original (and no longer maintained) Theano library.

%prep
%setup -q -n aesara-%{version}
# Drop hashbangs from objects not installed to PATH
sed -i -e "1{/\/usr\/bin\/env python/d}" aesara/misc/check_blas.py aesara/misc/check_multi_gpu.py

%build
%python_build

%install
%python_install

# remove binaries and stuff thats not supposed to end up on system
%python_expand rm -r %{buildroot}%{$python_sitelib}/bin

# Move tests into the module sitelib
%{python_expand mkdir %{buildroot}%{$python_sitelib}/aesara/tests
mv %{buildroot}%{$python_sitelib}/tests %{buildroot}%{$python_sitelib}/aesara/tests
}

%python_clone -a %{buildroot}%{_bindir}/aesara-cache
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative aesara-cache

%postun
%python_uninstall_alternative aesara-cache

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/aesara-cache
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
