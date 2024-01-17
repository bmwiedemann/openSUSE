#
# spec file for package xfs_undelete
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xfs_undelete
Version:        12.0
Release:        0
Summary:        An undelete tool for the XFS filesystem
License:        GPL-3.0-only
Group:          System/Filesystems
URL:            https://github.com/ianka/xfs_undelete
Source:         https://github.com/ianka/xfs_undelete/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       coreutils
Requires:       file
Requires:       file-magic
Requires:       tcl >= 8.6
Requires:       tcllib
BuildArch:      noarch

%description
xfs_undelete tries to recover all files on an XFS filesystem marked as
deleted. You may also specify a date or age since deletion, and file types
to ignore or to recover exclusively.

%prep
%setup -q

%build

%install
#---env-shebangs generate warnings / error messages in OBS:
sed -i -e '1 s|/usr/bin/env tclsh|/usr/bin/tclsh|' xfs_undelete

mkdir -p %{buildroot}%{_sbindir}
cp -a xfs_undelete %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man8
gzip -c xfs_undelete.man >%{buildroot}%{_mandir}/man8/xfs_undelete.8.gz

%files
%license LICENSE
%doc README.md
%{_sbindir}/xfs_undelete
%{_mandir}/man8/xfs_undelete.8.gz

%changelog
