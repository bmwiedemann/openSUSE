#
# spec file for package sethdlc
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           sethdlc
Version:        1.18
Release:        0
Summary:        Utility for the Generic HDLC layer
# GPL-2.0-only as stated in the header of sethdlc.c
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            https://www.kernel.org/doc/Documentation/networking/generic-hdlc.txt
Source:         https://kernel.org/pub/linux/utils/net/hdlc/%{name}-%{version}.tar.gz
Source1:        https://kernel.org/pub/linux/utils/net/hdlc/%{name}-%{version}.tar.sign
Source99:       %name.keyring
BuildRequires:  gcc

%description
The sethdlc utility is used to set physical interface, clock rate,
used HDLC mode, and can add any required PVCs if using Frame Relay.

https://www.kernel.org/doc/Documentation/networking/generic-hdlc.txt

%prep
%setup -q

%build
rm sethdlc
gcc %{optflags} %{name}.c -o %{name}

%install
install -D -m0755 sethdlc %{buildroot}/%{_sbindir}/sethdlc

%files
%{_sbindir}/sethdlc

%changelog
