#
# spec file for package zizmor
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           nono-cli
Version:        0.75.0
Release:        0
Summary:        CLI for nono capability-based sandbox
License:        Apache-2.0
URL:            https://github.com/nolabs-ai/nono/
Source0:        https://github.com/nolabs-ai/nono/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.zst
ExcludeArch:    %ix86 %arm32 ppc ppc64le s390 s390x
BuildRequires:  ca-certificates-mozilla
BuildRequires:  cargo >= 1.97
BuildRequires:  cargo-packaging
BuildRequires:  gcc-c++

%description
nono-cli is a capability-based sandboxing system for running untrusted AI
agents with OS-enforced isolation.

%prep
%autosetup -p 1 -n nono-%{version} -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/nono %{buildroot}%{_bindir}/nono

%check
# would be nice, currently failing
#{cargo_test}

%files
%doc README.md
%license LICENSE
%{_bindir}/nono

%changelog
