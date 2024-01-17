#
# spec file for package sympow
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


Name:           sympow
Version:        2.023.6
Release:        0
Summary:        Program to compute symmetric power elliptic curve L-functions
License:        BSD-2-Clause
Group:          Productivity/Scientific/Math
URL:            https://gitlab.com/rezozer/forks/sympow
Source:         https://gitlab.com/rezozer/forks/sympow/-/archive/v%version/%name-v%version.tar.bz2
Patch1:         sympow-2.023.5-cachedir.patch
BuildRequires:  help2man
BuildRequires:  pari-gp
Requires:       grep
Requires:       sed
Requires:       pari-gp

%description
SYMPOW is a mathematical program to compute special values of
symmetric power elliptic curve L-functions; it can compute up to
about 64 digits of precision.

%prep
%autosetup -p1 -n %name-v%version

%build
PREFIX="%_prefix" ./Configure
cat >>config.h <<-EOF
	#define PKGLIBDIR "%_libexecdir/%name"
EOF
perl -i -pe 's{%_prefix/lib/%name}{%_libexecdir/%name}' Makefile
%make_build OPT="%optflags"

%install
%make_install

%files
%_bindir/sympow
%_mandir/man1/*.1*
%_libexecdir/%name/
%_datadir/%name/
%license COPYING

%changelog
