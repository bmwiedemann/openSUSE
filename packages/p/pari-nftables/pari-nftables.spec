#
# spec file for package pari-nftables
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


Name:           pari-nftables
Version:        20080929
Release:        0
Summary:        Megrez Number Field tables for the PARI CAS
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://pari.math.u-bordeaux.fr/

Source:         nftables.tar.xz
Source2:        LICENSE
BuildRequires:  xz
BuildArch:      noarch
Conflicts:      libpari-gmp < 2.2.11

%description
This package contains the historical megrez number field tables
(errors fixed, 1/10th the size, easier to use) for the PARI CAS.

%prep
%autosetup -cn data
cp "%_sourcedir/LICENSE" .

%build

%install
c="%buildroot/%_datadir/pari"
mkdir -p "$c"
mv nftables "$c/"

%files
%_datadir/pari
%license LICENSE

%changelog
