#
# spec file for package vacation
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


Name:           vacation
Version:        1.2.7.1
Release:        0
Summary:        A way to automatically reply to incoming e-mail
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            https://www.csamuel.org/software/vacation
Source:         https://downloads.sf.net/vacation/%{name}-%{version}.tar.gz
Patch0:         vacation-%{version}.diff
Patch1:         vacation-%{version}.multiple-vacationmsg_files.diff
Patch3:         vacation-%{version}.strip.diff
# PATCH-FIX-UPSTREAM bsc#944326 - long From: header (two lines) not handled correctly
Patch4:         0001-Patch-to-handle-long-folded-headers-from-Zdenek-Havr.patch
# PATCH-FIX-SUSE Also handle junkfilter based on procmail
Patch5:         vacation-%{version}-junkfilter.diff
Patch6:         vacation-1.2.7.1-nogecos.patch
BuildRequires:  gdbm-devel

%description
This program answers your e-mail when you are lying on the beach.

Documentation: man vacation

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4
%patch5
%patch6 -p1

%build
chmod -R u+w,g+r,o+r .
%make_build clobber
%make_build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man{1,5}
make install MANDIR=%{buildroot}%{_mandir}/man BINDIR=%{buildroot}%{_bindir}
rm -f %{buildroot}%{_mandir}/man5/forward.5
echo '.so man5/aliases.5' > %{buildroot}%{_mandir}/man5/forward.5
chmod 0444 %{buildroot}%{_mandir}/man5/forward.5

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/vacation
%{_bindir}/vaclook
%{_mandir}/man1/vacation.1%{?ext_man}
%{_mandir}/man1/vaclook.1%{?ext_man}
%{_mandir}/man5/forward.5%{?ext_man}

%changelog
