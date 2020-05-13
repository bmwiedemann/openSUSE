#
# spec file for package dbxtool
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


Name:           dbxtool
Version:        7
Release:        0
Summary:        Secure Boot DBX updater
License:        GPL-2.0-only
URL:            https://github.com/rhboot/dbxtool
BuildRequires:  efivar-devel >= 26-1
BuildRequires:  popt-devel
Requires:       efivar >= 26-1
Source0:        https://github.com/rhboot/dbxtool/releases/download/dbxtool-%version/dbxtool-%version.tar.bz2
Patch0:         dbxtool-fixes.patch
%systemd_requires

%description
This package contains DBX updates for UEFI Secure Boot.

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="%optflags"

%install
%make_install 

rm %buildroot/usr/share/doc/dbxtool/COPYING

%pre
%service_add_pre dbxtool.service

%post
%service_add_post dbxtool.service

%preun
%service_del_preun dbxtool.service

%postun
%service_del_postun dbxtool.service


%files
%license COPYING
%{_bindir}/dbxtool
%doc %{_mandir}/man1/*
%dir %{_datadir}/dbxtool/
%{_datadir}/dbxtool/*.bin
%{_unitdir}/dbxtool.service

%changelog
