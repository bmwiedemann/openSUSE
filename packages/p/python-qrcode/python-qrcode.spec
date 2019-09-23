#
# spec file for package python-qrcode
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
Name:           python-qrcode
Version:        6.1
Release:        0
Summary:        QR Code image generator
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/lincolnloop/python-qrcode
Source:         https://files.pythonhosted.org/packages/source/q/qrcode/qrcode-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Recommends:     python-Pillow
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
This module uses the Python Imaging Library (PIL) to allow for the generation
of QR Codes.

%prep
%setup -q -n qrcode-%{version}
# drop shebang from console_scripts
sed -i '1s@^#!.*@@' qrcode/console_scripts.py

%build
%python_build

%install
%python_install
%fdupes %{buildroot}%{_prefix}

%check
%python_exec -m pytest -s qrcode

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGES.rst LICENSE README.rst
%python3_only %{_bindir}/qr
%python3_only %{_mandir}/man1/qr.1%{?ext_man}
%{python_sitelib}/*

%changelog
