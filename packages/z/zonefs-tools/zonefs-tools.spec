#
# spec file for package zonefs-tools
#
# Copyright (c) 2021 SUSE LLC
# Copyright (C) 2020, Western Digital Corporation or its affiliates.
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


Name:           zonefs-tools
Version:        1.5.0
Release:        0
Summary:        Utilities for the Zonefs filesystem
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/damien-lemoal/zonefs-tools.git
Source:         zonefs-tools.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(uuid)

%description
Utilities needed to create and maintain zonefs file systems under Linux.

%prep
%setup -q 

%build
sh ./autogen.sh
%configure
%make_build

%install
%make_install
rm %{buildroot}/%{_sbindir}/mkfs.zonefs
ln -s %{_sbindir}/mkzonefs %{buildroot}/%{_sbindir}/mkfs.zonefs

%post
%postun

%files
%license COPYING.GPL
%doc README.md
%{_sbindir}/mkfs.zonefs
%{_sbindir}/mkzonefs
%{_mandir}/man8/mkzonefs.8%{?ext_man}

%changelog
