#
# spec file for package minicom
#
# Copyright (c) 2020 SUSE LLC
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
Version:        2.7.1
Release:        0
Summary:        A Terminal Program
License:        GPL-2.0-or-later
Group:          Hardware/Modem
URL:            http://alioth.debian.org/projects/minicom/
Source0:        https://alioth.debian.org/frs/download.php/latestfile/3/%{name}-%{version}.tar.gz
Patch0:         minicom-2.2-defaults.diff
Patch2:         03norzsz.diff
Patch4:         minicom-2.3-no-build-date.patch
Patch5:         minicom-2.4-norootsetup.diff
# PATCH-FIX-UPSTREAM increase permitted length of serial device (bnc#707860)
Patch6:         minicom-2.5-serial_device_path_length.patch
Patch7:         fix-upstream-gcc10-build1.patch
Patch8:         fix-upstream-gcc10-build2.patch
Patch9:         fix-upstream-gcc10-build3.patch
BuildRequires:  ckermit
BuildRequires:  gettext-devel
BuildRequires:  lockdev-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
Requires:       ckermit
Requires:       rzsz
Requires(pre):  group(uucp)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A terminal program similar to Telix(tm) (a program for calling other
computers via modem) under MS-DOS.

If you want to access your modem with minicom, you have to be a member
of the uucp group.

%lang_package

%prep
%setup -q
%patch0
%patch2 -p1
%patch4
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

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
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}

%files
%defattr(644,root,root,755)
%doc doc/minicom.FAQ AUTHORS COPYING NEWS README
%attr(0755,root,root) %{_bindir}/ascii-xfr
%attr(0755,root,uucp) %{_bindir}/minicom
%attr(0755,root,root) %{_bindir}/runscript
%attr(0755,root,root) %{_bindir}/xminicom
%{_mandir}/man1/ascii-xfr.1.gz
%{_mandir}/man1/minicom.1.gz
%{_mandir}/man1/xminicom.1.gz
%{_mandir}/man1/runscript.1.gz

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
