#
# spec file for package jless
#
# Copyright (c) 2022, Martin Hauke <mardnh@gmx.de>
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


Name:           jless
Version:        0.8.0
Release:        0
Summary:        Pager for JSON (or YAML) data
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://jless.io/
Source:         https://github.com/PaulJuliusMartinez/jless/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(xcb)

%description
JLess is a command-line JSON viewer designed for reading, exploring, and
searching through JSON data.

JLess will pretty print your JSON and apply syntax highlighting. Use it when
exploring external APIs, or debugging request payloads.

Expand and collapse Objects and Arrays to grasp the high- and low-level
structure of a JSON document. JLess has a large suite of vim-inspired commands
that make exploring data a breeze.

JLess supports full text regular-expression based search. Quickly find the data
you're looking for in long String values, or jump between values for the same
Object key.

%prep
%autosetup -p 1 -a 1
install -D -m 0644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/jless

%changelog
