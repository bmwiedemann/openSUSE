#
# spec file for package bonk
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


Name:           bonk
Version:        0.3.2
Release:        0
Summary:        Touch with mkdir tool
License:        MIT
Group:          System/Console
URL:            https://github.com/elliot40404/bonk
Source0:        %{name}-%{version}.tar.gz
# Project uses no deps
# Source1:        vendor.tar.gz
# Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo

%description
Bonk is a touch alternative with an added feature to
create directories.

%prep
%setup -q
# mkdir .cargo
# cp %%{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/bonk

%changelog
