#
# spec file for package SecLists
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


Name:           SecLists
Version:        2022.4
Release:        0
Summary:        SecLists is the security tester's companion
License:        MIT
URL:            https://github.com/danielmiessler/SecLists
Source:         https://github.com/danielmiessler/SecLists/archive/refs/tags/%{version}.tar.gz

%description

SecLists is the security tester's companion. It's a collection of multiple
types of lists used during security assessments, collected in one place. List
types include usernames, passwords, URLs, sensitive data patterns, fuzzing
payloads, web shells, and many more. The goal is to enable a security tester to
pull this repository onto a new testing box and have access to every type of
list that may be needed.

This project is maintained by Daniel Miessler, Jason Haddix, and g0tmi1k.

%prep

%setup -q

%install

mkdir -p %{buildroot}%{_datadir}/seclists
cp -a * %{buildroot}%{_datadir}/seclists

%files
%license LICENSE
%{_datadir}/seclists
# 2022-12: This currently breaks cavil and rpmlint
%exclude %{_datadir}/seclists/Payloads/Zip-Bombs

%changelog
