#
# spec file for package pari-galpol
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pari-galpol
Version:        20180625
Release:        0
Summary:        GALPOL polynomial database for the PARI CAS
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://pari.math.u-bordeaux.fr/

Source:         http://pari.math.u-bordeaux.fr/pub/pari/packages/galpol.tgz
Source2:        http://pari.math.u-bordeaux.fr/pub/pari/packages/galpol.tgz.asc
Source3:        LICENSE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Conflicts:      libpari-gmp < 2.4.3

%description
PARI package of the GALPOL database of polynomials defining Galois
extensions of the rationals, accessed by the "galoisgetpol" function.

%prep
%setup -qn data
cp "%_sourcedir/LICENSE" .

%build

%install
c="%buildroot/%_datadir/pari"
mkdir -p "$c"
mv galpol "$c/"

%files
%defattr(-,root,root)
%_datadir/pari
%doc LICENSE

%changelog
