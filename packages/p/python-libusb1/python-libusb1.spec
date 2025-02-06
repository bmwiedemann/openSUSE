#
# spec file for package python-libusb1
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


Name:           python-libusb1
Version:        3.2.0
Release:        0
Summary:        Python wrapper for libusb-1.0
# Relicensed from GPL to LGPLv2.1+ in May 2015
# https://github.com/vpelletier/python-libusb1/commit/238eaefa0759622afc554884b4b333d9bf946c65
License:        LGPL-2.1-or-later
URL:            https://github.com/vpelletier/%{name}
Source:         https://files.pythonhosted.org/packages/source/l/libusb1/libusb1-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libusb-1_0-0 >= 1.0.21
BuildRequires:  python-rpm-macros
Requires:       libusb-1_0-0 >= 1.0.21
BuildArch:      noarch
%python_subpackages

%description
This is a pure python wrapper for libusb-1.0.

%prep
%autosetup -p1 -n libusb1-%{version}
sed -i '/wheel/d' setup.py

sed -i '1{/^#!/d}' examples/*.py
chmod a-x examples/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m usb1.testUSB1 -v

%files %{python_files}
%doc README.rst examples/
%license COPYING.LESSER
%{python_sitelib}/libusb1.py
%{python_sitelib}/usb1
%pycache_only %{python_sitelib}/__pycache__/libusb1*
%{python_sitelib}/libusb1-%{version}*info

%changelog
