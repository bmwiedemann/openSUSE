#
# spec file for package gnu_ddrescue
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


Name:           gnu_ddrescue
Version:        1.28
Release:        0
Summary:        I/O error aware data recovery and copying utility
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://gnu.org/software/ddrescue/ddrescue.html
Source:         https://download.savannah.gnu.org/releases/ddrescue/ddrescue-%version.tar.lz
Source2:        https://download.savannah.gnu.org/releases/ddrescue/ddrescue-%version.tar.lz.sig
Source3:        %name.keyring
BuildRequires:  gcc-c++
BuildRequires:  lzip
Requires(post): %install_info_prereq
Requires(preun):%install_info_prereq

%description
GNU ddrescue is a data recovery tool. It copies data from one file or
block device (hard disk, CD-ROM, etc.) to another, trying hard to
rescue data in case of read errors.

It is more memory and time efficient than dd_rescue+dd_rhelp on disks
with more than a few hundred bad sectors.

%prep
%autosetup -n ddrescue-%version

%build
# not autoconf, but at least it behaves (nearly) like it.
%configure --enable-linux CFLAGS="%optflags" CXXFLAGS="%optflags"
%make_build

%install
%make_install

%post
%install_info --info-dir=%_infodir %_infodir/ddrescue.info.gz

%preun
%install_info_delete --info-dir=%_infodir %_infodir/ddrescue.info.gz

%files
%_bindir/*
%_mandir/man*/*
%_infodir/ddrescue*
%license COPYING
%doc NEWS README

%changelog
