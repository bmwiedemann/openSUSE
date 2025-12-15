#
# spec file for package bkcrack
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


Name:           bkcrack
Version:        1.8.1
Release:        0
Summary:        Crack legacy zip encryption with Biham and Kocher's known plaintext attack
License:        Zlib
URL:            https://github.com/kimci86/bkcrack/
Source:         https://github.com/kimci86/bkcrack/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake

%description
bkcrack is a command-line tool which implements a known plaintext attack
against legacy encrypted ZIP archives. The vulnerability was shown by Eli Biham
and Paul C. Kocher in the research paper "A known plaintext attack on the PKZIP
stream cipher." The main features are:

* Recover internal state from ciphertext and plaintext.
* Remove or change a ZIP archive's password using the internal state.
* Recover the original password from the internal state.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
install build/src/%{name} %{buildroot}%{_bindir}

%check
%ctest

%files
%license license.txt
%doc readme.md
%{_bindir}/%{name}

%changelog
