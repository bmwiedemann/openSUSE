#
# spec file for package python-libusb1
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
Name:           python-libusb1
Version:        1.7.1
Release:        0
Summary:        Python wrapper for libusb-1.0
# Relicensed from GPL to LGPLv2.1+ in May 2015
# https://github.com/vpelletier/python-libusb1/commit/238eaefa0759622afc554884b4b333d9bf946c65
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/vpelletier/%{name}
Source:         https://files.pythonhosted.org/packages/source/l/libusb1/libusb1-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libusb-1_0-0
BuildRequires:  python-rpm-macros
Requires:       libusb-1_0-0
BuildArch:      noarch
%python_subpackages

%description
This is a pure python wrapper for libusb-1.0.

%prep
%setup -q -n libusb1-%{version}
sed -i '1{/^#!/d}' examples/*.py
chmod a-x examples/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m usb1.testUSB1

%files %{python_files}
%doc README.rst examples/
%license COPYING.LESSER
%{python_sitelib}/*

%changelog
