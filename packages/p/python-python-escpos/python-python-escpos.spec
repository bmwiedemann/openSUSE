#
# spec file for package python-python-escpos
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without libalternatives
Name:           python-python-escpos
Version:        3.1
Release:        0
Summary:        Python library to manipulate ESC/POS Printers
License:        MIT
URL:            https://github.com/python-escpos/python-escpos
Source:         https://files.pythonhosted.org/packages/source/p/python-escpos/python-escpos-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove-six-and-mock.patch gh#python-escpos/python-escpos/pull/738
Patch0:         remove-six-and-mock.patch
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module importlib-resources}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module pycups}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-barcode}
BuildRequires:  %{python_module pyusb}
BuildRequires:  %{python_module qrcode}
BuildRequires:  %{python_module scripttest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-Pillow
Requires:       python-appdirs
Requires:       python-argcomplete
Requires:       python-importlib-resources
Requires:       python-pyaml
Requires:       python-pycups
Requires:       python-pyserial
Requires:       python-python-barcode
Requires:       python-pyusb
Requires:       python-qrcode
Requires:       python-setuptools
Provides:       %{python_flavor}-escpos = %{version}
BuildArch:      noarch
%if "%{python_provides}" == "python3"
Provides:       python-escpos = %{version}
Provides:       python3-escpos = %{version}
%endif
%python_subpackages

%description
Library which lets the user have access to all those printers handled
by ESC/POS commands, as defined by Epson, from a Python application.

The library tries to implement the functions provided by the
ESC/POS-command-set and supports sending text, images,
barcodes and qr-codes to the printer.

%prep
%autosetup -p1 -n python-escpos-%{version}
sed -i -e "s/setup(/setup(version='%{version}',/" setup.py
sed -i -e '/addopts/d' pyproject.toml
find src -name '*.py' | xargs sed -i -e '/^#!/d'

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/python-escpos
%{python3_fix_shebang}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/escpos
%{python_sitelib}/python_escpos-%{version}.dist-info
%python_alternative %{_bindir}/python-escpos

%changelog
