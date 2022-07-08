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
Version:        1.9.1
Release:        0
Summary:        The minimal, blazing-fast, and infinitely customizable prompt for any shell
License:        ISC
URL:            https://starship.rs/
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(openssl)

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!
    Fast: it's fast – really really fast! rocket
    Customizable: configure every aspect of your prompt.
    Universal: works on any shell, on any operating system.
    Intelligent: shows relevant information at a glance.
    Feature rich: support for all your favorite tools.
    Easy: quick to install – start using it in minutes.

%prep
%setup -qa1
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
