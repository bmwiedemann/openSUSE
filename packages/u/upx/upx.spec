#
# spec file for package upx
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


Name:           upx
Version:        5.0.0
Release:        0
Summary:        The Ultimate Packer for eXecutables
License:        Apache-2.0 WITH LLVM-exception AND GPL-2.0-or-later AND BSD-4-Clause AND BSD-3-Clause AND MIT AND Zlib AND (CPL-1.0 OR LGPL-2.1-only)
Group:          Development/Tools/Other
URL:            https://upx.github.io/
Source:         https://github.com/upx/upx/releases/download/v%version/%name-%version-src.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libucl1-devel
BuildRequires:  zlib-devel

%description
UPX is a compressor for several different executable formats.
Programs receive a stub that makes them self-runnable. When run,
decompression either happens in memory in-place if possible, or to a
temporary file, the latter of which does not support setuid programs,
or the proper name in argv[0].

%prep
%autosetup -p1 -n %name-%version-src

# BSD-4-Clause licensed file, remove just in case bnc#753791
rm src/stub/src/i386-dos32.djgpp2-stubify.asm

%build
%cmake -DCMAKE_INSTALL_DOCDIR="%_docdir/%name"
%cmake_build

%install
%cmake_install
# separate picked with %%license
rm -f "%_defaultdocdir/%name/LICENSE"

%files
%license LICENSE
%_bindir/%name
%_mandir/man1/%name.1%{?ext_man}
%_defaultdocdir/%name/

%changelog
