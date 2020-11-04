#
# spec file for package kelbt
#
# Copyright (c) 2020 SUSE LLC
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


Name:           kelbt   
Version:        0.16
Release:        0
Summary:        Backtracking LALR(1) parser generator
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            http://www.colm.net/files/kelbt/

Source:         http://www.colm.net/files/kelbt/%name-%version.tar.gz
Source2:        kelbt.txt
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf

%description
Kelbt generates backtracking LALR(1) parsers. Where traditional
LALR(1) parser generators require static resolution of shift/reduce
conflicts, Kelbt generates parsers that handle conflicts by
backtracking at runtime. Kelbt is able to generate a parser for any
context-free grammar that is free of hidden left recursion.

%prep
%autosetup -p1

%build
install -pm0644 "%{S:2}" .
export CXXFLAGS="%optflags -Wno-narrowing"
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc kelbt.txt
%_bindir/kelbt

%changelog
