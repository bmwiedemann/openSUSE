#
# spec file for package pari-elldata
#
# Copyright (c) 2021 SUSE LLC
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


Name:           pari-elldata
Version:        20210301
Release:        0
Summary:        Elliptic Curve Data for the PARI CAS
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://pari.math.u-bordeaux.fr
Source:         %url/pub/pari/packages/elldata.tgz
Source2:        %url/pub/pari/packages/elldata.tgz.asc
Source3:        LICENSE
Source4:        COPYING
Source5:        %name.keyring
BuildArch:      noarch
Conflicts:      libpari-gmp < 2.2.11

%description
PARI/GP version of J. E. Cremona's Elliptic Curve Data, needed by
the PARI functions "ellsearch" and "ellidentify".

%prep
%autosetup -n data
cp -av %_sourcedir/LICENSE %_sourcedir/COPYING .
mv -v elldata/README .

%build

%install
install -dm0755 %buildroot/%_datadir/pari
mv -v elldata %buildroot/%_datadir/pari/

%files
%_datadir/pari/
%license COPYING LICENSE
%doc README

%changelog
