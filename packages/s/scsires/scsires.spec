#
# spec file for package scsires
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           scsires
Version:        0.7
Release:        0
Summary:        A SCSI reservation tool
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
Source:         scsires.tgz
Patch0:         scsi_resevers_text.diff
Patch1:         scsires_remove_unused_vars.diff
BuildRequires:  popt-devel

%description
This tool is for issuing SCSI-2 reservation and release commands, for
controlling exclusive access to a SCSI device that is shared between
more than one SCSI host adapter.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -Dpm 0755 scsi_reserve \
  %{buildroot}%{_sbindir}/scsi_reserve

%files
%license COPYING
%{_sbindir}/scsi_reserve

%changelog
