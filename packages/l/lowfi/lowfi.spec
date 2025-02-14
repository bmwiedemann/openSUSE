#
# spec file for package lowfi
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


Name:           lowfi
Version:        1.5.6
Release:        0
Summary:        An extremely simple lofi player
License:        MIT
URL:            https://github.com/talwat/lowfi
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  alsa-devel
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  pkgconfig(openssl)
ExclusiveArch:  %{rust_tier1_arches}

%description
A tiny rust app that serves a single purpose: play lofi.
It'll do this as simply as it can: no albums, no ads, just lofi.
All of the audio files played in lowfi are from Lofi Girl's website,
https://lofigirl.com/
under their licensing guidelines : https://form.lofigirl.com/CommercialLicense

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

%files
%doc README.md
%license LICENSE
%{_bindir}/lowfi

%changelog
