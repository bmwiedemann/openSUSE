#
# spec file for package pari-seadata
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


Name:           pari-seadata
Version:        20090618
Release:        0
Summary:        Polynomial and Elliptic Curve Data for the PARI CAS
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://pari.math.u-bordeaux.fr/

Source:         seadata.tar.xz
Source2:        LICENSE
BuildRequires:  xz
BuildArch:      noarch
Conflicts:      libpari-gmp < 2.4.3

%description
This package is needed by the "ellap" function of the PARI CAS for
large primes. The second one is a much smaller version that should be
suitable for primes up to 350 bits. These polynomials were extracted
from the ECHIDNA databases and computed by David R. Kohel.

%prep
%autosetup -n data
cp "%_sourcedir/LICENSE" .

%build

%install
c="%buildroot/%_datadir/pari"
mkdir -p "$c"
mv seadata "$c/"

%files
%_datadir/pari
%license LICENSE

%changelog
