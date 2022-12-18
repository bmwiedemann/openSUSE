#
# spec file for package starship
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


Name:           starship
Version:        1.12.0
Release:        0
Summary:        A customizable prompt for many shells
License:        ISC
URL:            https://starship.rs/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  pkgconfig(openssl)

%description
Starship generates shell code which modifies the current shell
behavior to display an extravagant prompt. It installs a hook before
every command invocation to gather additional information for the
prompt, which increases the latency of the prompt (by about 5 ms with
bash on a contemporary 3700X CPU).
The default setup requires Nerd Font and a terminal in dark colors.
dash is not supported as of 1.10.2.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%doc README.md
%license LICENSE
%{_bindir}/starship

%changelog
