#
# spec file for package statserial
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           statserial
Version:        1.1
Release:        0
Summary:        Helps to Debug Serial Lines
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://www.ibiblio.org/pub/Linux/system/serial
Source:         http://www.ibiblio.org/pub/Linux/system/serial/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-device.diff
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Statserial displays a table of the signals on a standard 9-pin or
25-pin serial port and indicates the status of the handshaking lines.
It can be useful for debugging problems with serial ports or modems.

%prep
%setup -q
%patch0

%build
cc %{optflags} -o statserial statserial.c -lncurses -ltinfo

%install
install -d -m 755 %{buildroot}%{_bindir}/
install -d -m 755 %{buildroot}%{_mandir}/man1/
install -m 755 statserial phone_log %{buildroot}%{_bindir}/
install -m 644 statserial.1 %{buildroot}%{_mandir}/man1/

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README
%{_mandir}/man?/*
%{_bindir}/*

%changelog
