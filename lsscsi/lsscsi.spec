#
# spec file for package lsscsi
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


%define         distver 030r154
Name:           lsscsi
Version:        0.30
Release:        0
Summary:        List all SCSI devices in the system
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://sg.danny.cz/scsi/lsscsi.html
Source:         http://sg.danny.cz/scsi/%{name}-%{version}.tar.xz
BuildRequires:  xz
Provides:       scsi:%{_bindir}/lsscsi

%description
The lsscsi command lists information about SCSI devices in Linux.

%prep
%setup -q -n %{name}-%{distver}

%build
%configure

%install
%make_install

%files
%license COPYING
%doc README ChangeLog
%{_bindir}/lsscsi
%{_mandir}/man8/lsscsi.8%{?ext_man}

%changelog
