#
# spec file for package iprange
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           iprange
Version:        1.0.4
Release:        0
Summary:        IP address range management tool for FireHOL
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Url:            http://firehol.org/
Source:         https://github.com/firehol/iprange/releases/download/v%{version}/iprange-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This tool manages IP address ranges for FireHOL.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md
%{_mandir}/man1/iprange.1%{ext_man}
%{_bindir}/iprange

%changelog
