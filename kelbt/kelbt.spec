#
# spec file for package kelbt
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kelbt   
Version:        0.16
Release:        0
Summary:        Backtracking LALR(1) parser generator
License:        GPL-2.0+
Group:          Development/Tools/Other
Url:            http://complang.org/kelbt/

Source:         http://www.colm.net/files/kelbt/%name-%version.tar.gz
Source2:        kelbt.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q

%build
install -pm0644 "%{S:2}" .
export CXXFLAGS="%optflags -Wno-narrowing"
%configure
make %{?_smp_mflags}

%install
b="%buildroot"
%make_install

%files
%defattr(-,root,root)
%doc COPYING kelbt.txt
%_bindir/kelbt

%changelog
