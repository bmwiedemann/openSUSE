#
# spec file for package mapitags
#
# Copyright (c) 2024 SUSE LLC
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


Name:           mapitags
Version:        20240617
Release:        0
Summary:        MAPI tag name database
License:        MIT
Group:          Development/Other
URL:            https://github.com/jengelh/mapitags
Source:         https://github.com/jengelh/mapitags/archive/refs/tags/mt-%version.tar.gz
BuildRequires:  automake
BuildRequires:  gcc-c++

%description
A list of mnemonics for MAPI property tags. MAPI programs (e.g.
gromox-eml2mt) can use these to translate between 32-bit property
numbers and a human-readable mnemonic name.

%prep
%autosetup -p1 -n mapitags-mt-%version

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%_bindir/mt*
%_datadir/mapi*
%_mandir/man*/mt*.1*

%changelog
