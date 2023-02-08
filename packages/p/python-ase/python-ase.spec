#
# spec file for package python-ase
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-ase
Version:        3.22.1
Release:        0
Summary:        Atomic Simulation Environment
License:        LGPL-2.1+
URL:            https://wiki.fysik.dtu.dk/ase
Source:         https://files.pythonhosted.org/packages/source/a/ase/ase-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://gitlab.com/ase/ase/-/merge_requests/2826
Patch0:         support-matplotlib-36.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 3.1.0}
BuildRequires:  %{python_module numpy >= 1.15.0}
BuildRequires:  %{python_module scipy >= 1.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module tk}
# /SECTION
BuildRequires:  fdupes
Requires:       python-matplotlib >= 3.1.0
Requires:       python-numpy >= 1.15.0
Requires:       python-scipy >= 1.1.0
BuildArch:      noarch
%python_subpackages

%description
Atomic Simulation Environment

%prep
%autosetup -p1 -n ase-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ase
%python_clone -a %{buildroot}%{_bindir}/ase-db
%python_clone -a %{buildroot}%{_bindir}/ase-gui
%python_clone -a %{buildroot}%{_bindir}/ase-run
%python_clone -a %{buildroot}%{_bindir}/ase-info
%python_clone -a %{buildroot}%{_bindir}/ase-build
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No scipy CODATA
%pytest -k 'not test_units'

%post
%python_install_alternative ase ase-db ase-gui ase-run ase-info ase-build

%postun
%python_uninstall_alternative ase

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license COPYING COPYING.LESSER LICENSE
%python_alternative %{_bindir}/ase
%python_alternative %{_bindir}/ase-db
%python_alternative %{_bindir}/ase-gui
%python_alternative %{_bindir}/ase-run
%python_alternative %{_bindir}/ase-info
%python_alternative %{_bindir}/ase-build
%{python_sitelib}/ase
%{python_sitelib}/ase*info

%changelog
