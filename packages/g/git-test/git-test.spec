#
# spec file for package git-test
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016 Michael Moese <michael.moese@gmail.com>
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


Name:           git-test
Version:        1.0.4
Release:        0
Summary:        Git extension to conveniently test all distinct versions
License:        Apache-2.0
Group:          Development/Tools/Version Control
URL:            https://github.com/spotify/git-test
Source:         https://github.com/spotify/git-test/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       git-core
BuildArch:      noarch

%description
Run tests on each distinct tree in a revision list, skipping versions whose
contents have already been tested.

%prep
%setup -q

%build

%install
install -D -p -m 0755 git-test   %{buildroot}%{_bindir}/git-test
install -D -p -m 0644 git-test.1 %{buildroot}%{_mandir}/man1/git-test.1

%files
%license LICENSE
%doc README.md
%{_bindir}/git-test
%{_mandir}/man1/git-test.1%{?ext_man}

%changelog
