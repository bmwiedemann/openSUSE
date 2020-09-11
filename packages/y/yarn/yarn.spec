#
# spec file for package yarn
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yarn
Version:        1.22.5
Release:        0
Summary:        📦🐈 Fast, reliable, and secure dependency management
License:        BSD-2-Clause
Group:          Development/Languages/NodeJS
Url:            https://github.com/yarnpkg/yarn/releases
Source:         https://github.com/yarnpkg/yarn/releases/download/v%{version}/yarn-v%{version}.tar.gz
Source1:        https://github.com/yarnpkg/yarn/releases/download/v%{version}/yarn-v%{version}.tar.gz.asc
BuildArch:      noarch
Requires:       nodejs >= 4.0
%description
Fast: Yarn caches every package it has downloaded, so it never needs to
download the same package again. It also does almost everything concurrently to
maximize resource utilization. This means even faster installs.

Reliable: Using a detailed but concise lockfile format and a deterministic
algorithm for install operations, Yarn is able to guarantee that any
installation that works on one system will work exactly the same on another
system.

Secure: Yarn uses checksums to verify the integrity of every installed package
before its code is executed.

%prep
%setup -q -n %{name}-v%{version}

%build
rm bin/*.cmd
perl -p -i -e 's|/usr/bin/env node|/usr/bin/node|g' bin/* lib/*

%install
install -D -d -m 0755              %{buildroot}%{_datadir}/yarn/ %{buildroot}%{_bindir}
cp -av bin/ lib/ package.json      %{buildroot}%{_datadir}/yarn/
ln -s %{_datadir}/yarn/bin/yarn    %{buildroot}%{_bindir}/yarn
ln -s %{_datadir}/yarn/bin/yarnpkg %{buildroot}%{_bindir}/yarnpkg

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_datadir}/yarn/
%{_bindir}/yarn
%{_bindir}/yarnpkg

%changelog

