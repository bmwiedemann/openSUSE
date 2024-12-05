#
# spec file for package python-segno
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


%{?sle15_python_module_pythons}
Name:           python-segno
Version:        1.6.1
Release:        0
Summary:        QR Code and Micro QR Code generator for Python
License:        BSD-3-Clause
URL:            https://github.com/heuer/segno/
Source0:        https://github.com/heuer/segno/archive/refs/tags/%{version}.tar.gz#/segno-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pypng}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
QR Code encoder and Micro QR Code encoder

Pure Python QR Code generator with no dependencies.

The project provides more than 1500 test cases (coverage >= 98%) to verify a
standard conform QR Code and Micro QR Code generation acc. to ISO/IEC
18004:2015(E).

%prep
%autosetup -p1 -n segno-%{version}

%build
%pyproject_wheel
sed -i 's/env python/python/' ./segno/cli.py
chmod 755 ./segno/cli.py

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/segno
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
IGNORED_CHECKS="test_plugin"
%pytest -k "not (${IGNORED_CHECKS})"

%post
%python_install_alternative segno

%postun
%python_uninstall_alternative segno

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/segno
%{python_sitelib}/segno
%{python_sitelib}/segno-%{version}.dist-info

%changelog
