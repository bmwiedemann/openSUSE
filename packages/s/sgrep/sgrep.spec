#
# spec file for package sgrep
#
# Copyright (c) 2020 SUSE LLC
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


Name:           sgrep
Version:        1.94a
Release:        0
Summary:        Searching for Structured Patterns
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.cs.helsinki.fi/~jjaakkol/sgrep.html
Source:         https://fossies.org/linux/misc/old/%{name}-%{version}.tar.gz
Patch0:         sgrep-sgreprc.diff

%description
Sgrep is like "grep" but it will also work for structured patterns. You can
use the program to extract fragments from SGML/XML or any other well formed
text files (including UTF-8 encoded files).

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
install -Dpm 0644 sample.sgreprc \
  %{buildroot}/%{_sysconfdir}/sgreprc
rm %{buildroot}%{_datadir}/sample.sgreprc

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README sgrep.lsm
%doc sample.sgreprc
%config %{_sysconfdir}/sgreprc
%{_bindir}/sgrep
%{_mandir}/man1/sgrep.1%{?ext_man}

%changelog
