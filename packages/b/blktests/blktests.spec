#
# spec file for package blktests
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define version_unconverted 0+git.20181114
Name:           blktests
Version:        0+git.20181114
Release:        0
Summary:        Linux kernel block layer testing framework
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-2.0-or-later
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          System/Benchmark
URL:            https://github.com/osandov/blktests
Source:         blktests-0+git.20181114.tar.xz
BuildRequires:  gcc-c++
Requires:       gcc
Requires:       make
Requires:       gawk
Requires:       fio
Recommends:     multipath-tools
Recommends:     nvme-cli
Recommends:     device-mapper
Recommends:     e2fsprogs
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
%license LICENSES/GPL-2.0
%{_prefix}/lib/blktests

%changelog
