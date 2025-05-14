#
# spec file for package parti
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013-2015 Steffen Winterfeldt
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


Name:           parti
Version:        2.8
Release:        0
Summary:        Show partition table information
License:        GPL-3.0-only
Group:          Hardware/Other
URL:            https://github.com/wfeldt/parti
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libmediacheck-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  rubygem(asciidoctor)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(uuid)
%if 0%{?suse_version} >= 1500
Requires:       mkisofs
%else
Requires:       cdrkit-cdrtools-compat
%endif

%description
Show partition table information for
* Master Boot Record (MBR) Partition Table
* GUID Partition Table (GPT)
* Apple Partition Map
* El Torito Bootable CD/DVD
* zIPL boot info

It shows the complete information but mostly in uninterpreted form (unlike partitioning tools like fdisk or parted).

So it can be used to verify the data your favorite partitioning tool has actually written.

%prep
%setup -q

%build
%make_build

%install
%make_install

%files
%{_bindir}/parti
%{_bindir}/unify-gpt
%license COPYING
%doc README.md
%doc %{_mandir}/man1/unify-gpt.*

%changelog
