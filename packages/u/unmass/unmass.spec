#
# spec file for package unmass
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009 - 2014 guru@unixtech.be
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


Name:           unmass
Version:        0.92
Release:        0
Summary:        Tool to Extract Game Archives
License:        GPL-2.0
Group:          Productivity/Archiving/Compression
Url:            http://mirex.mypage.sk/index.php?selected=1#Unmass
Source0:        http://mirex.mypage.sk/FILES/unmass-%{version}.tar.gz
#Patch1:         unmass-fix_error.patch
# PATCH-FIX-UPSTREAM unmass-no_return.patch pgajdos@suse.cz -- Add missing return.
Patch2:         unmass-no_return.patch
# PATCH-FIX-UPSTREAM - unmass-fix-unix-def.patch malcolmlewis@opensuse.org -- Fix incorrect UNIX ifdef.
Patch3:         unmass-fix-unix-def.patch
BuildRequires:  gcc-c++

%description
unmass is a tool to extract game archives.

It supports the following archive types: Crimson Land, Baldur's Gate 2,
Civilization 4, Doom (WADs), Dune 2, Etherlords 2, Final Fantasy 7 and 8,
Flashpoint, Knights of Xentar, Metal Gear Solid (DARs), Moorhuhn 2 and 3,
Megaman Legends, Oni, Operation Flashpoint, Princess Maker 2, Quake 1,
RollCage, Swine, Unreal Tournament umods, Virtua Fighter bitmaps, MEA exe's,
and some economy file formats.

%prep
%setup -q
%patch2 -p1
%patch3 -p1

%build
cd kdev_cmd
cp ../src/* src/
%configure --enable-static=no
make %{?_smp_mflags}

%install
install -Dpm0755 kdev_cmd/src/unmass_kdev \
  %{buildroot}%{_bindir}/unmass

%files
%defattr(-,root,root)
%doc kdev_cmd/AUTHORS
%{_bindir}/unmass

%changelog
