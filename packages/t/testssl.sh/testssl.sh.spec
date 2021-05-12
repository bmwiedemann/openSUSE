#
# spec file for package testssl.sh
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2018 Matthias Fehring <buschmann23@opensuse.org>
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


%define _data_dir_name testssl-sh

Name:           testssl.sh
Version:        3.0.5
Release:        0
Summary:        Testing TLS/SSL Encryption Anywhere On Any Port
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://testssl.sh
Source0:        https://github.com/drwetter/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Patch0:         testssl.sh-2.9.95-set-install-dir.patch
Requires:       bash >= 3.2
Requires:       openssl
BuildArch:      noarch

%description
testssl.sh is a free command line tool which checks a server's service on
any port for the support of TLS/SSL ciphers, protocols as well as some
cryptographic flaws.

%prep
%setup -q
%patch0 -p1
%if 0%{?suse_version} > 1500
sed -i 's|#!/usr/bin/env bash|#!/usr/bin/bash|g' testssl.sh
%else
# in Leap 15.x, it's still /bin/bash
sed -i 's|#!/usr/bin/env bash|#!/bin/bash|g' testssl.sh
%endif

%build

%install
install -D -m 0644 -t %{buildroot}/%{_datadir}/%{_data_dir_name}/etc etc/*
install -D -m 0755 -t %{buildroot}/%{_bindir} %{name}
install -D -m 0644 -T doc/testssl.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc CHANGELOG.md CREDITS.md Readme.md
%{_bindir}/%{name}
%{_datadir}/%{_data_dir_name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
