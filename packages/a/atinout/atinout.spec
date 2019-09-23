#
# spec file for package atinout
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           atinout
Version:        0.9.1
Release:        0
Summary:        Utility to communicate with modems via AT commands
License:        GPL-3.0-or-later
Group:          Hardware/Modem
URL:            http://atinout.sourceforge.net
Source:         http://sourceforge.net/projects/atinout/files/v%{version}/%{name}-%{version}.tar.gz
Patch0:         atinout-fix-build.patch

%description
This program will read a file (or stdin) containing a list of AT
commands. Each command will be send to the modem, and all the response
for the command will be output to file (or stdout).

Example, to hang up an ongoing call:

$ echo ATH | atinout - /dev/ttyACM0 -
ATH
OK
$

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS='%{optflags}'
make %{?_smp_mflags}

%install
%make_install

%files
%license gplv3.txt
%doc Changelog README
%{_bindir}/atinout
%{_mandir}/man1/atinout.1%{?ext_man}

%changelog
