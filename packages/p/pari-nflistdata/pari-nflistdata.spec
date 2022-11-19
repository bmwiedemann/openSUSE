#
# spec file for package pari-nflistdata
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           pari-nflistdata
Version:        20220729
Release:        0
Summary:        Data files for the "nflist" program from PARI
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://pari.math.u-bordeaux.fr/packages.html
Source:         https://pari.math.u-bordeaux.fr/pub/pari/packages/nflistdata.tgz
Source2:        https://pari.math.u-bordeaux.fr/pub/pari/packages/nflistdata.tgz.asc
Source9:        LICENSE
BuildArch:      noarch

%description
This package contains fields of small discriminant (currently needed
by the single Galois groups A5 and A5(6)) or to list regular
extensions of Q(T) in degree 7 to 15, using `nflist` from the PARI
CAS.

%prep
%autosetup -n data
cp "%_sourcedir/LICENSE" .

%build

%install
c="%buildroot/%_datadir/pari"
mkdir -p "$c"
mv nflistdata "$c/"

%files
%_datadir/pari
%license LICENSE

%changelog
