#
# spec file for package ouch
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


Name:           ouch
Version:        0.4.0~0
Release:        0
Summary:        Compression and decompression utility for the terminal
License:        MIT
Group:          Productivity/Archiving/Compression
URL:            https://github.com/ouch-org/ouch
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
The "Obvious Unified Compression Helper" is a CLI tool for
compressing and decompressing files from and to several formats.

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
%{_bindir}/ouch

%changelog
