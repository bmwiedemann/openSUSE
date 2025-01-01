#
# spec file for package topgrade
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


Name:           topgrade
Version:        16.0.1
Release:        0
Summary:        Upgrade all the things
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://github.com/%{name}-rs/%{name}
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}

%description
Keeping your system up to date usually involves invoking multiple package managers. This results in big, non-portable shell one-liners saved in your shell.
To remedy this, Topgrade detects which tools you use and runs the appropriate commands to update them

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
