#
# spec file for package viu
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


Name:           viu
Version:        1.5.0
Release:        0
Summary:        Terminal image viewer with native support
License:        MIT
URL:            https://github.com/atanunq/viu
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
A small command-line application to view images from the terminal written
in Rust. It is basically the front-end of viuer. It uses either iTerm,
Kitty or SIXEL graphics protocol, if supported. If not, lower half blocks
are displayed instead.

%prep
%autosetup -a1 -p1

%build
%{cargo_build} --features sixel

%install
%{cargo_install} --features sixel

%files
%license LICENSE*
%doc README*
%{_bindir}/%{name}

%changelog

