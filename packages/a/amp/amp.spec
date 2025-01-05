#
# spec file for package amp
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


Name:           amp
Version:        0.7.1
Release:        0
Summary:        A modal text editor for the terminal
License:        GPL-3.0-only
URL:            https://github.com/jmacdonald/amp
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(zlib)

%description
Text editor written in Rust, that aims to take the core interaction model of Vim,
simplify it, and bundle in the essential features required for a modern text editor.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -Dm0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}

%changelog
