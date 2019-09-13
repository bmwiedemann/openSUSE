#
# spec file for package gaa
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gaa
Version:        1.6.6
Release:        0
Summary:        GAA Argument Analyzer and Code Generator
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
#Group: code generators
Url:            http://gaa.sf.net/

Source:         http://downloads.sf.net/gaa/%name-%version.tar.gz
Patch1:         gaa-getline.diff
Patch2:         gaa-parser.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  flex

%description
GAA is a code generator that turns GAA language expressions into C
code which then analyze the arguments and creates program help
descriptions.

%prep
%setup -q
%patch -P 1 -P 2 -p1

%build
%configure --disable-static
# not so parallel safe due to use of bison
make -j1 gaadocdir="%_docdir/%name"

%install
%make_install gaadocdir="%_docdir/%name"

%files
%defattr(-,root,root)
%_bindir/gaa
%_datadir/%name/
%_docdir/%name/

%changelog
