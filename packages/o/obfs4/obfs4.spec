#
# spec file for package obfs4
#
# Copyright (c) 2022 SUSE LLC
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


Name:           obfs4
Version:        0.0.13
Release:        0%{?dist}
Summary:        Pluggable transport proxy for Tor
License:        BSD-2-Clause AND GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://gitlab.com/yawning/obfs4
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.16

%description
A tool that attempts to circumvent censorship by transforming the Tor traffic
between the client and the bridge. This way censors, who usually monitor traffic
between the client and the bridge, will see innocent-looking transformed traffic
instead of the actual Tor traffic.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build -o obfs4proxy/obfs4proxy -mod=vendor -buildmode=pie ./obfs4proxy

%install
%__install -D -m 0755 -t %{buildroot}%{_bindir} obfs4proxy/obfs4proxy
%__install -D -m 0644 -t %{buildroot}%{_mandir}/man1 doc/obfs4proxy.1

%files
%{_bindir}/obfs4proxy
%{_mandir}/man1/obfs4proxy.1*
%doc doc README.md ChangeLog
%license LICENSE LICENSE-GPL3.txt

%changelog
