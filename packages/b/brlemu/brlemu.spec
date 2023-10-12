#
# spec file for package brlemu
#
# Copyright (c) 2023 SUSE LLC
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


Name:           brlemu
Version:        0.1
Release:        0
Summary:        Emulates a braille display
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://build.opensuse.org/package/show/Base:System/brlemu
Source:         brlemu-0.1.tgz
Patch0:         brlemu-fakeport.diff
Patch1:         brlemu-0.1-gcc7.diff
Patch2:         brlemu-0.1-nostrip.diff
BuildRequires:  ncurses-devel

%description
Brlemu emulates a braille display. It is intended for testing braille
support without needing to acquire expensive hardware devices.

%prep
%setup -q -n brlemu-0.1
%autopatch -p1

%build
%make_build CFLAGS="%{optflags}" CC="gcc"

%install
mkdir -p %{buildroot}%{_bindir}
%make_install

%files
%{_bindir}/brlemu
%doc README
%license COPYING

%changelog
