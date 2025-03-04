#
# spec file for package samply
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


Name:           samply
Version:        0.13.1
Release:        0
Summary:        A command line CPU profiler which uses the Firefox profiler as its UI
License:        Apache-2.0 OR MIT
URL:            https://github.com/mstange/samply
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source3:        README.suse-maint
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.74

%description
samply is a command line CPU profiler which uses the Firefox profiler as its UI.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
mkdir -p "%{buildroot}%{_bindir}"
install -D -m 0755 target/release/samply %{buildroot}%{_bindir}/samply

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md RELEASES.md
%{_bindir}/%{name}

%changelog
