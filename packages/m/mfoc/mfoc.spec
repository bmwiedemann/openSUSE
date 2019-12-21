#
# spec file for package mfoc
#
# Copyright (c) 2019 SUSE LLC
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


Name:           mfoc
Version:        0.10.7+git38
Release:        0
Summary:        Mifare Classic Offline Cracker: key recovery tool for MC cards
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://github.com/nfc-tools/mfoc

Source:         %name-%version.tar.xz
BuildRequires:  automake
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libnfc) >= 1.7

%description
MFOC is a tool to recover keys from Mifare Classic cards.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%files
%_bindir/mfoc
%_mandir/man1/mfoc.1*

%changelog
