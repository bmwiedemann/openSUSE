#
# spec file for package xbill
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           xbill
Version:        2.1
Release:        0
Summary:        Classic X Game
License:        GPL-1.0-or-later
Group:          Amusements/Games/Action/Shoot
URL:            http://www.xbill.org/
Source0:        http://www.xbill.org/download/%{name}-%{version}.tar.gz
Patch1:         01_makefile_in.diff
Patch2:         02_hurd_logos.diff
Patch3:         03_fix_ftbfs.diff
Patch4:         04_implicit_declaration.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libXaw-devel
BuildRequires:  user(games)
Requires(pre):  group(games)
Requires(pre):  user(games)
Requires(pre):  permissions

%description
Ever get the feeling that nothing is going right? You're a sysadmin, and someone's trying to destroy your computers. The little people running around the screen are trying to infect your computers with Wingdows [TM], a virus cleverly designed to resemble a popular operating system. Additionally, some computers are connected with network cables. When one computer on a network becomes infected, a spark will be sent down the cable, and will infect the computer on the other end when it reaches there.

%prep
%autosetup -p1

%build
autoreconf
%configure --disable-gtk --disable-motif --enable-athena
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_localstatedir}/games/%{name}
mv %{buildroot}%{_localstatedir}/games/xbill.scores.default %{buildroot}%{_localstatedir}/games/%{name}

%files
%doc README README.Ports ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%dir %attr(0750,root,games) %{_localstatedir}/games/xbill
%attr(0660,root,games) %{_localstatedir}/games/xbill/xbill.scores.default

%changelog
