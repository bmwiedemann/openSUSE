#
# spec file for package ohcount
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ohcount
%define lname	libohcount
Version:        4.0.0
Release:        0
Summary:        The Ohloh source code line counter
License:        GPL-2.0
Group:          Development/Tools/Other
URL:            https://www.openhub.net/p/ohcount

#Git-Clone:	git://github.com/blackducksw/ohcount
Source:         https://github.com/blackducksoftware/ohcount/archive/%version.tar.gz
Patch1:         cflags.diff
BuildRequires:  bash
BuildRequires:  file-devel
BuildRequires:  gcc >= 4.1.2
BuildRequires:  gperf
BuildRequires:  pcre-devel
BuildRequires:  ragel >= 7
BuildRequires:  swig
BuildRequires:  xz

%description
Ohcount counts lines of source code. It supports over 70 programming
languages, and has been used to count over 6 billion lines of code by
300,000 developers. Ohcount can also detect open source licenses such
as GPL within a large directory of source code. It can further detect
code that targets a particular programming API, such as Win32 or KDE.

%prep
%autosetup -p1

%build
export CFLAGS="%optflags"
./build ohcount

%install
b="%buildroot"
mkdir -p "$b/%_bindir" "$b/%_libdir"
install -pm0755 bin/ohcount "$b/%_bindir/"

%files
%license COPYING
%_bindir/ohcount

%changelog
