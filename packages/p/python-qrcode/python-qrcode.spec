#
# spec file for package python-qrcode
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
Name:           python-qrcode
Version:        8.2
Release:        0
Summary:        QR Code image generator
License:        BSD-3-Clause
URL:            https://github.com/lincolnloop/python-qrcode
Source:         %{url}/archive/v%{version}.tar.gz#/qrcode-%{version}.tar.gz
BuildRequires:  %{python_module Pillow >= 9.1.0}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pypng}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-Pillow >= 9.1.0
Recommends:     python-pypng
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This module uses the Python Imaging Library (PIL) to allow for the generation
of QR Codes.

%prep
%setup -q -n python-qrcode-%{version}
# drop shebang from console_scripts
sed -i '1s@^#!.*@@' qrcode/console_scripts.py

%build
%pyproject_wheel

%install
%pyproject_install
install -Dm 644 doc/qr.1 %{buildroot}%{_mandir}/man1/qr.1
%python_clone -a %{buildroot}%{_mandir}/man1/qr.1
%python_clone -a %{buildroot}%{_bindir}/qr
%fdupes %{buildroot}%{_prefix}

%check
%pytest -s qrcode -k "not test_change"

%post
%python_install_alternative qr qr.1

%postun
%python_uninstall_alternative qr qr.1

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/qr
%python_alternative %{_mandir}/man1/qr.1%{?ext_man}
%{python_sitelib}/qrcode
%{python_sitelib}/qrcode-%{version}.dist-info

%changelog
