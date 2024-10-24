#
# spec file for package python-ase
#
# Copyright (c) 2024 SUSE LLC
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
Version:        3.23.0
Release:        0
Summary:        Atomic Simulation Environment
License:        LGPL-2.1-or-later
URL:            https://wiki.fysik.dtu.dk/ase
Source:         https://files.pythonhosted.org/packages/source/a/ase/ase-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ase-mr3400-numpy2.patch https://gitlab.com/ase/ase/-/merge_requests/3400
Patch0:         ase-mr3400-numpy2.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 3.1.0}
BuildRequires:  %{python_module numpy >= 1.15.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.1.0}
BuildRequires:  %{python_module tk}
# /SECTION
BuildRequires:  fdupes
Requires:       python-matplotlib >= 3.1.0
Requires:       python-numpy >= 1.15.0
Requires:       python-scipy >= 1.1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Atomic Simulation Environment

%prep
%autosetup -p1 -n ase-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ase
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No scipy CODATA
donttest="test_units"
# Broken with current release, remove on upgrade
donttest+=" or test_pw_input_write_nested_flat or test_fix_scaled"
%pytest -k "not ($donttest)"

%post
%python_install_alternative ase

%postun
%python_uninstall_alternative ase

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license COPYING COPYING.LESSER LICENSE
%python_alternative %{_bindir}/ase
%{python_sitelib}/ase
%{python_sitelib}/ase-%{version}.dist-info

%changelog
