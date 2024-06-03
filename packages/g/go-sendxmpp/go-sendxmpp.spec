#
# spec file for package go-sendxmpp
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


Name:           go-sendxmpp
Version:        0.11.0
Release:        0
Summary:        A little tool to send messages to an XMPP contact or MUC
License:        BSD-2-Clause
Group:          Productivity/Networking/Instant Messenger
URL:            https://salsa.debian.org/mdosch/go-sendxmpp
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging

%description
A little tool to send messages to an XMPP contact or MUC.

%prep
%setup -q -a1

%build
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -D -m0644 man/%{name}.1 %{buildroot}%{_mandir}/man1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
