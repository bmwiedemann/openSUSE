#
# spec file for package interceptty
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           interceptty
Version:        0.6+git.20190731
Release:        0
Summary:        Serial port sniffer
License:        GPL-2.0-only
Group:          Hardware/Modem
URL:            https://github.com/geoffmeyers/interceptty
Source:         %{name}-%{version}.tar.xz

%description
IntercepTTY is a program that can sit between a real (or fake)
serial port and an application, recording any communications
between the application and the device. It can also be used as a
network serial server or client, to provide an emulated serial port
connected to a program, and for various other tasks.

%prep
%setup -q
chmod -x AUTHORS ChangeLog README.md COPYING

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/interceptty
%{_bindir}/interceptty-nicedump
%{_mandir}/man1/interceptty.1%{?ext_man}

%changelog
