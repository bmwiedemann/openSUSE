#
# spec file for package dm-zoned-tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dm-zoned-tools
Version:        1.0.1
Release:        0
Summary:        "dm-zoned" device-mapper target manager
License:        GPL-3.0-only
Group:          Hardware/Other
URL:            https://github.com/hgst/dm-zoned-tools
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
The dmzadm utility formats backend devices used with the dm-zoned device
mapper. This utility will inspect the device verifying that the device is a
zoned block device and will prepare and write on-disk dm-zoned metadata
according to the device capacity, zone size, etc.

%prep
%setup -q

%build
sh ./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING COPYING.GPL
%doc README.md
%{_sbindir}/dmzadm
%{_mandir}/man8/*

%changelog
