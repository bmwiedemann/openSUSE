#
# spec file for package python-testflo
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
Name:           python-testflo
Version:        1.3.4
Release:        0
Summary:        A flow-based testing framework
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/OpenMDAO/testflo
Source:         https://files.pythonhosted.org/packages/source/t/testflo/testflo-%{version}.tar.gz
# PATCH-FIX-OPENSUSE use_setuptools.patch -- some of the optional features we want need setuptools
Patch0:         use_setuptools.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module mpi4py}
BuildRequires:  %{python_module psutil}
# /SECTION
Requires:       python-six
Recommends:     python-coverage
Recommends:     python-mpi4py
Recommends:     python-psutil
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(preun):  update-alternatives

%python_subpackages

%description
This module provides a flow-based testing framework. testflo supports
testing of the OpenMDAO framework. Some OpenMDAO features require
execution under MPI, while others don't. testflo runs all of the
authors' tests in the same way and allows them to build their tests
using unittest.TestCase objects that they are familiar with.

%prep
%setup -q -n testflo-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/testflo

# Tests not included in sdists
# %%check
# %%python_expand $python -B -m unittest testflo.test

%post
%python_install_alternative testflo

%preun
%python_uninstall_alternative testflo

%files %{python_files}
%license LICENSE.txt
%doc README.md RELEASE_NOTES.txt
%python_alternative %{_bindir}/testflo
%{python_sitelib}/*

%changelog
