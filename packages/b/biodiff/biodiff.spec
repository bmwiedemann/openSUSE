#
# spec file for package biodiff
#
# Copyright (c) 2023-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           biodiff
Version:        1.2.1
Release:        0
Summary:        A tool for binary diffing
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/8051Enthusiast/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Hex diff viewer using alignment algorithms from biology.

The tool is able to show two binary files side by side so that similar
places will be at the same position on both sides and bytes missing
from one side are padded. It uses bio-informatics algorithms from the
rust-bio library (typically used for DNA sequence alignment) for that.

Features
 - Unaligned view for moving both sides independently as contiguous
   byte segments.
 - Aligned view for comparing corresponding bytes of both files.
 - Many configurable byte representations (bases 2, 8, 10, 16;
   mixed ascii/hex, braille, roman numerals).
 - Right-to-left mode, horizontal and vertical split, ascii and bar
   column.
 - bytes per row, adjustable by pressing [, ], 0.
 - Automatic determination of width by finding repetitions in
   visible/selected bytes by pressing '='.
 - Search using text, regex and hexagex.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .

%files
%license LICENSE
%doc CHANGELOG README.md
%{_bindir}/biodiff
%{_bindir}/git-biodiff

%changelog
