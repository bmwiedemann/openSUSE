#
# spec file for package himalaya
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


Name:           himalaya
Version:        0.9.0~0
Release:        0
Summary:        Command-line interface for email management
License:        AGPL-3.0-only AND AGPL-3.0-or-later AND GPL-2.0-or-later AND MIT AND bzip2-1.0.6 AND MPL-2.0 AND CC-BY-3.0 AND BSD-4-Clause AND OpenSSL AND OFL-1.1
Group:          Productivity/Networking/Email/Clients
URL:            https://pimalaya.org/himalaya/cli/latest/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  libopenssl-devel
ExclusiveArch:  %{rust_tier1_arches}

%description
Command-line interface for email management.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%{_bindir}/himalaya

%changelog
