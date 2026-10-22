#
# spec file for package lsscsi
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           lsscsi
Version:        0.33
Release:        0
Summary:        List all SCSI devices in the system
License:        GPL-2.0-or-later
URL:            http://sg.danny.cz/scsi/lsscsi.html
Source:         https://github.com/doug-gilbert/lsscsi/archive/refs/tags/r%{version}.tar.gz#/lsscsi-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  perl(Autom4te::C4che)
BuildRequires:  perl(Autom4te::ChannelDefs)
BuildRequires:  perl(Autom4te::Channels)
BuildRequires:  perl(Autom4te::Config)
BuildRequires:  perl(Autom4te::Configure_ac)
BuildRequires:  perl(Autom4te::FileUtils)
BuildRequires:  perl(Autom4te::General)
BuildRequires:  perl(Autom4te::Getopt)
BuildRequires:  perl(Autom4te::Request)
BuildRequires:  perl(Autom4te::XFile)
Provides:       scsi:%{_bindir}/lsscsi

%description
The lsscsi command lists information about SCSI devices in Linux.

%prep
%autosetup -n %{name}-r%{version}

%build
./autogen.sh
%configure

%install
%make_install

%files
%license COPYING
%doc README ChangeLog
%{_bindir}/lsscsi
%{_bindir}/ls_name_value
%{_bindir}/ls_name_value_rd
%{_mandir}/man8/lsscsi.8%{?ext_man}
%{_mandir}/man8/lsscsi_json.8%{?ext_man}
%{_mandir}/man8/ls_name_value.8%{?ext_man}
%{_mandir}/man8/ls_name_value_rd.8%{?ext_man}

%changelog
