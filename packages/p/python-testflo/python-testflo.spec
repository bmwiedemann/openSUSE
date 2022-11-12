#
# spec file for package python-testflo
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


%define skip_python36 1
Name:           python-testflo
Version:        1.4.9
Release:        0
Summary:        A flow-based testing framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/OpenMDAO/testflo
Source:         https://files.pythonhosted.org/packages/source/t/testflo/testflo-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(preun):update-alternatives
Recommends:     python-coverage
Recommends:     python-mpi4py
Recommends:     python-psutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module mpi4py}
BuildRequires:  %{python_module psutil}
# /SECTION
%python_subpackages

%description
This module provides a flow-based testing framework. testflo supports
testing of the OpenMDAO framework. Some OpenMDAO features require
execution under MPI, while others don't. testflo runs all of the
authors' tests in the same way and allows them to build their tests
using unittest.TestCase objects that they are familiar with.

%prep
%setup -q -n testflo-%{version}

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

%postun
%python_uninstall_alternative testflo

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/testflo
%{python_sitelib}/testflo
%{python_sitelib}/testflo-*.egg-info

%changelog
