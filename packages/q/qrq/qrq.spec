#
# spec file for package qrq
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


Name:           qrq
Version:        0.3.5
Release:        0
Summary:        CW trainer
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Hamradio/Other
URL:            https://fkurz.net/ham/qrq.html
Source:         https://fkurz.net/ham/qrq/%{name}-%{version}.tar.gz
Patch0:         reproducible.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  dos2unix

%description
qrq is a Morse telegraphy trainer. It is not intended for learning telegraphy,
but to improve the ability to copy callsigns at high speeds, as needed for
example for Contesting.

%prep
%autosetup -p1
mtime=$(stat --format=%Y ChangeLog)
dos2unix ChangeLog COPYING README AUTHORS
# keep mtime from before conversion for use in BUILD_INFO
touch -d @$mtime ChangeLog COPYING README AUTHORS

%build
%make_build

%install
%make_install \
	DESTDIR=%{buildroot}%{_prefix} \
	%{nil}

%files
%license COPYING
%doc ChangeLog README AUTHORS
%{_bindir}/qrq
%{_bindir}/qrqscore
%{_datadir}/qrq
%{_mandir}/man1/qrq.1%{?ext_man}

%changelog
