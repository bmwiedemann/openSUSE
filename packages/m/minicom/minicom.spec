#
# spec file for package minicom
#
# Copyright (c) 2024 SUSE LLC
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


Name:           minicom
Version:        2.9
Release:        0
Summary:        A Terminal Program
License:        GPL-2.0-or-later
Group:          Hardware/Modem
URL:            https://salsa.debian.org/minicom-team/minicom
Source0:        https://salsa.debian.org/minicom-team/minicom/-/archive/%{version}/minicom-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE openSUSE-defaults.patch -- Fix default settings for *SUSE
Patch0:         openSUSE-defaults.patch
# PATCH-FIX-OPENSUSE openSUSE-no-root-setup.patch
Patch1:         openSUSE-no-root-setup.patch
# PATCH-FIX-UPSTREAM minicom-2.8-replace-sigrelse.patch -- Replace deprecated sigrelse https://salsa.debian.org/minicom-team/minicom/-/commit/c43a18c25b09f6968219f3ecbaec7215e804838d
Patch3:         minicom-2.8-replace-sigrelse.patch
# PATCH-FIX-UPSTREAM fix-undefined-reference.patch -- Fix undefined reference to external COLS and LINES
Patch4:         minicom-2.8-fix-undefined-reference.patch
BuildRequires:  ckermit
BuildRequires:  gettext-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
Requires:       ckermit
Requires:       rzsz
Requires(pre):  group(uucp)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A terminal program similar to Telix(tm) (a program for calling other
computers via modem) under MS-DOS.

If you want to access your modem with minicom, you have to be a member
of the uucp group.

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} $(ncursesw6-config --cflags)"
export LDFLAGS="$(ncursesw6-config --libs)"
%configure \
    --disable-rpath \
    --enable-music \
    --enable-dfl-baud=57600 \
    --enable-dfl-port=/dev/modem \
    --enable-socket \
    --enable-cfg-dir=%{_sysconfdir}
%make_build

%install
%make_install
%find_lang %{name}

%files
%license COPYING
%doc doc/minicom.FAQ AUTHORS NEWS README
%attr(0755,root,root) %{_bindir}/ascii-xfr
%attr(0755,root,uucp) %{_bindir}/minicom
%attr(0755,root,root) %{_bindir}/runscript
%attr(0755,root,root) %{_bindir}/xminicom
%{_mandir}/man1/ascii-xfr.1.gz
%{_mandir}/man1/minicom.1.gz
%{_mandir}/man1/xminicom.1.gz
%{_mandir}/man1/runscript.1.gz

%files lang -f %{name}.lang

%changelog
