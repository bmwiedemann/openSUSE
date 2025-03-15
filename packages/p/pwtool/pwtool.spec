#
# spec file for package pwtool
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           pwtool
Version:        0.6.1
Release:        0
Summary:        Password generation tool
License:        GPL-3.0-or-later
URL:            https://www.usenix.org.uk/content/pwtool.html
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.78
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Generate passwords from random characters or words and optionally show their
cryptographic hash.

The default generated password set is copy/paste friendly without extended
characters that would break the default copy selection you get when
double-clicking a word. They also are don't break quotation strings (quote
marks, double quotes or backticks).

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%doc changelog.md
%{_bindir}/pwtool

%changelog
