#
# spec file for package gp2c
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gp2c
Version:        0.0.13
Release:        0
Summary:        GP script to PARI C program compiler
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://pari.math.u-bordeaux.fr/

#Git-Clone:	https://pari.math.u-bordeaux.fr/git/gp2c.git
#Git-Web:	https://pari.math.u-bordeaux.fr/cgi-bin/gitweb.cgi
Source:         https://pari.math.u-bordeaux.fr/pub/pari/GP2C/gp2c-%version.tar.gz
Source2:        https://pari.math.u-bordeaux.fr/pub/pari/GP2C/gp2c-%version.tar.gz.asc
Source9:        %name.keyring
BuildRequires:  fdupes

%description
The gp2c compiler is a package for translating GP routines into the C
programming language, so that they can be compiled and used with the PARI
system or the GP calculator.

The main advantage of doing this is to speed up computations and to include
your own routines within the preexisting GP ones. It may also find bugs in GP
scripts.

%prep
%autosetup -p1

%build
%configure --docdir="%_docdir/%name" CFLAGS="%optflags -fno-common"
%make_build

%install
%make_install
%fdupes %buildroot/%_prefix

%files
%_bindir/gp2c*
%_docdir/%name/
%_datadir/%name/
%_mandir/man1/gp2c*
%license COPYING

%changelog
