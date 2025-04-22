#
# spec file for package mboxgrep
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           mboxgrep
Version:        0.7.13
Release:        0
Summary:        Mailbox scanning tool
License:        GPL-2.0-or-later
URL:            https://mboxgrep.org/
Source:         https://git.datatipp.se/dspiljar/mboxgrep/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(zlib)

%description
mboxgrep is a small utility that scans a mailbox for messages matching a
regular expression. Found messages can be either displayed on standard output,
counted, deleted, piped to a shell command or written to another mailbox.

%prep
%autosetup -p1

%build
%configure \
	--without-sense-of-humor \
	%{nil}
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING.md
%doc NEWS.md README.md AUTHORS.md
%{_bindir}/mboxgrep
%{_infodir}/mboxgrep.info%{?ext_info}
%{_mandir}/man1/mboxgrep.1%{?ext_man}

%changelog
