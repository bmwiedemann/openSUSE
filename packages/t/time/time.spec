#
# spec file for package time
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           time
Version:        1.10
Release:        0
Summary:        Run Programs And Summarize System Resource Usage
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://www.gnu.org/software/time/
Source:         https://ftp.gnu.org/gnu/time/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/gnu/time/%{name}-%{version}.tar.gz.sig
# https://savannah.gnu.org/project/release-gpgkeys.php?group=time
Source3:        %{name}.keyring

%description
The "time" command runs another program, then displays information
about the resources used by that program, collected by the system
while the program was running.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
# time.1 is part of man-pages (bnc#878057)
install -d %{buildroot}%{_mandir}/man1

%check
%make_build check

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/time
%{_infodir}/time.info*%{ext_info}

%changelog
