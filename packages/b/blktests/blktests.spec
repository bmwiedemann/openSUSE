#
# spec file for package blktests
#
# Copyright (c) 2023 SUSE LLC
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


Name:           blktests
Version:        0+20230302.676d42c
Release:        0
Summary:        Linux kernel block layer testing framework
License:        GPL-2.0-or-later
URL:            https://github.com/osandov/blktests
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
Requires:       fio
Requires:       gawk
Requires:       gcc
Requires:       make
Recommends:     blktrace
Recommends:     device-mapper
Recommends:     e2fsprogs
Recommends:     multipath-tools
Recommends:     nvme-cli
Recommends:     xfsprogs

%description
blktests is a test framework for the Linux kernel block layer and
storage stack. It is inspired by the xfstests filesystem testing
framework.

%prep
%setup -q

%build
make %{?_smp_mflags} V=1

%install
%make_install prefix="%{_prefix}/lib"

%files
%doc README.md
%license LICENSES/GPL-2.0 LICENSES/GPL-3.0
%{_prefix}/lib/blktests

%changelog
