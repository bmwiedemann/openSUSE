#
# spec file for package bat
#
# Copyright (c) 2021 SUSE LLC
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


Name:           bat
Version:        0.18.1
Release:        0
Summary:        A cat(1) clone with syntax highlighting and Git integration
License:        Apache-2.0 OR MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/sharkdp/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  rust >= 1.45
BuildRequires:  rust-packaging
ExclusiveArch:  %{rust_arches}

%description
A cat(1) clone which supports syntax highlighting for a large number of
programming and markup languages. It has git integration and automatic paging.

%prep
%setup -qa1
%define cargo_registry $(pwd)/vendor
%{cargo_prep}

%build
export CARGO_NET_OFFLINE=true
%{cargo_build}

%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%if %{with check}
%check
%{cargo_test}
%endif

%files
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/%{name}

%changelog
