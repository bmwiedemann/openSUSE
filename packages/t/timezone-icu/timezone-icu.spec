#
# spec file for package timezone-icu
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           timezone-icu
Version:        2026e
Release:        0
Summary:        Timezone definitions for the ICU library
License:        Unicode-3.0
Group:          System/Base
URL:            https://unicode-org.github.io/icu/userguide/datetime/timezone/
Source:         %name-%version.tar.xz
BuildRequires:  fdupes
BuildRequires:  xz
BuildArch:      noarch

%description
This extra package contains updated timezone definitions
that override the built-in set provided by the ICU libraries.

%package ledata
Summary:        Timezone definitions for the ICU library
Group:          System/Base
Provides:       timezone-icu = %version

%description ledata
This extra package contains updated timezone definitions
that override the built-in set provided by the ICU libraries.

This subpackage contains these data tables, in little-endian format.

%package bedata
Summary:        Timezone definitions for the ICU library
Group:          System/Base
Provides:       timezone-icu = %version

%description bedata
This extra package contains updated timezone definitions
that override the built-in set provided by the ICU libraries.

This subpackage contains these data tables, in big-endian format.

%prep
%autosetup -p1

%build

%install
b="%buildroot"
# icu4c >= 54 is able to recognize these override fragments (the binary format is 44).
vlist="60.2 65.1 69.1" # Leap 15
vlist="$vlist 77.1" # Leap 16
vlist="$vlist 78.3" # Slowroll/Tumbleweed
for version in $vlist; do
	maj="${version%.*}"
	d="$b/%_datadir/icu/$version/icudt$maj"
	mkdir -pv "${d}b" "${d}l"
	cp -alv tzdata/icunew/%version/44/be/*.res "${d}b/"
	cp -alv tzdata/icunew/%version/44/le/*.res "${d}l/"
done
%fdupes %buildroot/%_datadir/icu

%files bedata
%dir %_datadir/icu
%dir %_datadir/icu/*
%_datadir/icu/*/icudt*b/

%files ledata
%dir %_datadir/icu
%dir %_datadir/icu/*
%_datadir/icu/*/icudt*l/

%changelog
