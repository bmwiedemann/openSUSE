#
# spec file for package cargo-vendor-filterer
#
# Copyright (c) 2023 SUSE LLC
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


Name:           cargo-vendor-filterer
Summary:        Cargo vendor filterer
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://github.com/coreos/cargo-vendor-filterer
Version:        0.5.11
Release:        0
Source0:        https://github.com/coreos/cargo-vendor-filterer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
Requires:       (cargo or rustup)

%description
Core cargo vendor does not have filtering and thus, creates large amount of incompatible platform-specific dependencies added to
vendor such as those that are MacOS or Windows only. This utility solves that issue of vendoring dependencies by filtering
what is needed and not needed and can be configured to vendor dependencies for specific platforms such as GNU/Linux.

%prep
%autosetup -a1
mkdir -p .cargo/
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
