#
# spec file for package python-pylink-square
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pylink-square
Version:        1.4.0
Release:        0
Summary:        Python interface for SEGGER J-Link
License:        Apache-2.0
URL:            http://www.github.com/Square/pylink
Source:         https://files.pythonhosted.org/packages/source/p/pylink-square/pylink-square-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module psutil >= 5.2.2}
BuildRequires:  %{python_module six}
# Requires for mock == 2.0.0 replaced by using unittest.mock
# /SECTION
BuildRequires:  fdupes
Requires:       python-psutil >= 5.2.2
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python interface for SEGGER J-Link.

%prep
%setup -q -n pylink-square-%{version}
sed -i 's/assertEquals/assertEqual/g' tests/unit/test_library.py
sed -i 's/\.called_once_with/.assert_called_once_with/g' tests/unit/test_jlink.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pylink-rtt
%python_clone -a %{buildroot}%{_bindir}/pylink-swv
%python_clone -a %{buildroot}%{_bindir}/pylink
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# replace mock with unittest.mock
find tests -type f -exec sed -i 's/from mock/from unittest.mock/g' {} +
find tests -type f -exec sed -i 's/import mock/import unittest.mock as mock/g' {} +
# ignore checks that fail on some architectures
# see https://github.com/square/pylink/issues/175
IGNORED_CHECKS="test_initialize_windows"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_unlock_kinetis_read_fail"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_unlock_kinetis_success"
# Fails because parameter order in assert_called_once_with
IGNORED_CHECKS="${IGNORED_CHECKS} or test_cp15_register_write_success or test_set_log_file_success"
%pytest -k "not (${IGNORED_CHECKS})"

%post
%python_install_alternative pylink-rtt pylink-swv pylink

%postun
%python_uninstall_alternative pylink-rtt

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%python_alternative %{_bindir}/pylink-rtt
%python_alternative %{_bindir}/pylink-swv
%python_alternative %{_bindir}/pylink
%{python_sitelib}/pylink/
%{python_sitelib}/pylink_square-%{version}.dist-info

%changelog
