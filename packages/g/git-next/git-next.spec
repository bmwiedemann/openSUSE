#
# spec file for package git-next
#
# Copyright (c) 2025 SUSE LLC
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


Name:           git-next
Version:        2025.12.1
Release:        0
Summary:        Trunk-based development manager for a solo developer
License:        MIT
URL:            https://codeberg.org/kemitix/git-next
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.81
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  pkgconfig(dbus-1)

%description
Trunk-based developement manager.

git-next is a combined server and command-line tool that enables trunk-based
development workflows where each commit must pass CI before being included in
the main branch.

"A source-control branching model, where developers collaborate on code in a
single branch called ‘trunk’, resist any pressure to create other long-lived
development branches by employing documented techniques. They therefore avoid
merge hell, do not break the build, and live happily ever after."
(https://trunkbaseddevelopment.com/)

Features

* Allows enforcing the requirement for each commit to pass the CI pipeline
  before being included in the main branch
* Provides a server component that manages the trunk-based development process
* Ensure a consistent, high-quality codebase by preventing untested changes
  from being added to main
* Requires each commit uses conventional commit format.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
git config --global user.email "test@test.test"
git config --global user.name "test"

%{cargo_test}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
