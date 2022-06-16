#
# spec file for package intelhex
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


Name:           intelhex
Version:        2.3.0
Release:        0
Summary:        Library for Intel HEX Files Manipulations
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/bialix/intelhex
Source:         https://github.com/bialix/intelhex/archive/%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  python3
BuildRequires:  unzip
BuildArch:      noarch

%description
Python implementation of Intel HEX file format allows you read, modify, write
hex files and convert them to binary form.

The Intel HEX file format widely used in microprocessors and microcontrollers
area as the de-facto standard for representation of code for programming
microelectronic devices.

This work implements an **intelhex** Python library to read, write,
create from scratch and manipulate data from HEX (also known as Intel HEX)
file format. These operations are provided by “IntelHex” class.

The distribution package also includes several convenience Python scripts
to do basic tasks that utilize this library. The “bin2hex.py” script
converts binary data to HEX, and the “hex2bin.py” works the other direction.
“hex2dump.py” converts data from HEX to a hexdump which is useful for
inspecting data, and “hexmerge.py” merges multiple HEX files into one.

%lang_package

%prep
%setup -q

%build
python3 setup.py\
	build

%install
python3 setup.py\
	install\
	--prefix=%{_prefix}\
	--root=%{buildroot}
dos2unix AUTHORS.rst NEWS.rst README.rst LICENSE.txt

%files
%doc AUTHORS.rst NEWS.rst README.rst
%license LICENSE.txt
%{_bindir}/bin2hex.py
%{_bindir}/hex*.py
%{python_sitelib}/*

%changelog
