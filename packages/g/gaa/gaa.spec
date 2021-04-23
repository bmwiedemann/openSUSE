#
# spec file for package gaa
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


Name:           gaa
Version:        1.6.6
Release:        0
Summary:        GAA Argument Analyzer and Code Generator
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            http://gaa.sf.net/

Source:         http://downloads.sf.net/gaa/%name-%version.tar.gz
Patch1:         gaa-getline.diff
Patch2:         gaa-parser.diff
BuildRequires:  bison
BuildRequires:  flex

%description
GAA is a code generator that turns GAA language expressions into C
code which then analyze the arguments and creates program help
descriptions.

%prep
%autosetup -p1

%build
%configure --disable-static
# not so parallel safe due to use of bison
make -j1 gaadocdir="%_docdir/%name"

%install
%make_install gaadocdir="%_docdir/%name"

%files
%_bindir/gaa
%_datadir/%name/
%_docdir/%name/
%license COPYING

%changelog
