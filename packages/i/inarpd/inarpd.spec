#
# spec file for package inarpd
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


Name:           inarpd
Version:        0.17
Release:        0
Summary:        Inverse ARP daemon for Linux
# GPL-2.0-only as stated in the header of inarpd-0.17.c
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            https://www.kernel.org/doc/Documentation/networking/generic-hdlc.txt
Source:         https://kernel.org/pub/linux/utils/net/hdlc/%{name}-%{version}.c.gz
Source1:        https://kernel.org/pub/linux/utils/net/hdlc/%{name}-%{version}.c.sign
Source2:        inarpd.8
Source99:       %name.keyring
BuildRequires:  gcc
BuildRequires:  gzip

%description
Inverse ARP (InARP) daemon for Linux.

%prep
%setup -q -c -T
gunzip -c %{SOURCE0} > %{name}-%{version}.c

%build
gcc %{optflags} %{name}-%{version}.c -o %{name}

%install
install -D -m0755 inarpd %{buildroot}/%{_sbindir}/inarpd
install -D -m0644 %{SOURCE2} %{buildroot}/%{_mandir}/man8/inarpd.8

%files
%{_sbindir}/inarpd
%{_mandir}/man8/inarpd.8%{?ext_man}

%changelog
