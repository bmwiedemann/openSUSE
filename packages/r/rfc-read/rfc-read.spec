#
# spec file for package rfc-read
#
# Copyright (c) 2023 SUSE LLC
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


Name:           rfc-read
Version:        0.2.6
Release:        0
Summary:        Read RFCs from the command-line
License:        MIT
URL:            https://github.com/bfontaine/rfc
Source:         https://github.com/bfontaine/rfc/archive/refs/tags/v%{version}.tar.gz
Requires:       bash
Requires:       curl
Requires:       less
BuildArch:      noarch

%description
A tool written in Bash to read RFCs from the command-line. It fetches RFCs and drafts from the Web and caches them locally.

%prep
%setup -q -n rfc-%{version}

%build
sed -i "s|/env bash|/bash|g" rfc

%install
install -D -m755 rfc %{buildroot}%{_bindir}/rfc
install -D -m644 man/rfc.1 %{buildroot}%{_mandir}/man1/rfc.1

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/rfc
%{_mandir}/man1/rfc.1%{?ext_man}

%changelog
