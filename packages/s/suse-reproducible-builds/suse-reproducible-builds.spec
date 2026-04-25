#
# spec file for package suse-reproducible-builds
#
# Copyright (c) 2026 SUSE LLC
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


Name:           suse-reproducible-builds
Summary:        Enable reproducible builds
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        1.0
Release:        0
Source0:        macros.suse-reproducible-builds
Source1:        suse-reproducible-builds.sh
Source2:        COPYING
BuildArch:      noarch

%description
Installing this package tweaks the build process
to create reproducible packages.

%prep

%build
%define _lto_cflags %{nil}
cp %SOURCE2 .

%install
install -m 644 -D %SOURCE0 $RPM_BUILD_ROOT/usr/lib/rpm/macros.d/macros.suse-reproducible-builds
install -m 644 -D %SOURCE1 $RPM_BUILD_ROOT/etc/profile.d/suse-reproducible-builds.sh

%files
%license COPYING
/etc/profile.d/suse-reproducible-builds.sh
/usr/lib/rpm/macros.d/macros.suse-reproducible-builds

%changelog
