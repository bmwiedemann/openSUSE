#
# spec file for package drmcru
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license to this file is the file itself (except if the
# license to the file is an unsupported license, in which case the
# license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%global rustflags -C debuginfo=2 -C link-arg=-s
%if "x%{?rust_tier1_arches}" == "x"
%global rust_tier1_arches noarch
%endif

Name:           drmcru
Version:        0.1.5
Release:        0
Summary:        Linux DRM/KMS custom resolution utility
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/ssupt/drmcru
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor-drmcru.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.87
ExclusiveArch:  %{x86_64} %{aarch64} %{rust_tier1_arches}

%description
drmcru is a Direct Rendering Manager (DRM) and Kernel Mode Setting (KMS) custom
resolution utility for Linux systems. 
%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
%{cargo_install}
strip -s %{buildroot}%{_bindir}/%{name}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
