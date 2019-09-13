#
# spec file for package intelhex
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           intelhex
Version:        2.2.1
Release:        0
Summary:        Library for Intel HEX Files Manipulations
License:        BSD-3-Clause
Group:          Development/Tools/Other
Url:            https://github.com/bialix/intelhex
Source:         https://github.com/bialix/intelhex/archive/%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  python
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
python setup.py\
	build

%install
python setup.py\
	install\
	--prefix=%{_prefix}\
	--root=$RPM_BUILD_ROOT
dos2unix AUTHORS.rst NEWS.rst Readme.rst LICENSE.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS.rst NEWS.rst Readme.rst
%license LICENSE.txt
%{_bindir}/*
%{python_sitelib}/*

%changelog
