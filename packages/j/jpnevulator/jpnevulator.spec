#
# spec file for package jpnevulator
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           jpnevulator
Version:        2.3.4
Release:        0
Summary:        Serial Sniffer
License:        GPL-2.0-only
Group:          Hardware/Modem
URL:            http://jpnevulator.snarl.nl/
#Git-Clone:     https://github.com/snarlistic/jpnevulator
Source:         https://github.com/snarlistic/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         jpnevulator-obey-cflags.patch

%description
jpnevulator is a serial sniffer. It can be used to send data on a
serial device, too. It can read or write from/to one or more serial
devices at the same time.

In write mode, data to be sent on the serial device(s) is read from a
file or stdin in hexadecimal notation. Data is sent on the serial
device(s) line by line.

In read mode, data to be read from the serial device(s) is written to a
file or stdout in hexadecimal notation. It is possible to pass the
data in between the serial device(s). Several options enhance the
way the data is displayed.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS Changelog BUGS FAQ README TODO
%{_bindir}/jpnevulator
%{_mandir}/man1/jpnevulator.1%{?ext_man}

%changelog
