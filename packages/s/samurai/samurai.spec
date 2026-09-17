#
# spec file for package samurai
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           samurai
Version:        1.3
Release:        0
Summary:        C99 implementation of the ninja build tool
License:        Apache-2.0
URL:            https://github.com/michaelforney/samurai
Source:         https://github.com/michaelforney/samurai/releases/download/%version/samurai-%version.tar.gz
BuildRequires:  c_compiler
BuildRequires:  make

%description
samurai is a ninja-compatible build tool written in C99.

samurai implements the ninja build language through version 1.9.0
except for MSVC dependency handling. It uses the same format for the
".ninja_log" and ".ninja_deps" files as ninja, currently version 5
and 4, respectively.

%prep
%autosetup -p1

%build
export CC=cc
%set_build_flags

%make_build clean
%make_build

%install
%make_install PREFIX="%_prefix"

%files
%license LICENSE
%_bindir/samu
%_mandir/man1/samu.1*

%changelog
