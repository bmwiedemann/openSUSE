#
# spec file for package duperemove
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


%define samename btrfs-extent-same
%if 0%{?suse_version} <= 1500
%define req_gcc_ver 12
BuildRequires:  gcc%{req_gcc_ver}
%endif
Name:           duperemove
Version:        0.14.1
Release:        0
Summary:        Software to find duplicate extents in files and remove them
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://github.com/markfasheh/duperemove
Source:         https://github.com/markfasheh/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sqlite3)

%description
Duperemove finds duplicate extents in files and prints them to the
console. It also has the option to deduplicate extents on those file
systems which support the Linux extent-same ioctl.

%package -n %{samename}
Summary:        Debug/Test tool to exercise the btrfs out-of-band deduplication ioctl
Group:          System/Filesystems

%description -n %{samename}
Debug/Test tool to exercise a btrfs ioctl for deduplicating file regions.

%prep
%setup -q

%build
%if 0%{?suse_version} <= 1500
CC="CC=%{_bindir}/gcc-%{req_gcc_ver}"
%endif
%make_build $CC CFLAGS="%{optflags} -fcommon"

%install
%make_install PREFIX="%{_prefix}"

%files -n %{samename}
%{_bindir}/%{samename}
%{_mandir}/man?/%{samename}.8%{?ext_man}

%files
%license LICENSE
%doc README.md
%{_bindir}/duperemove
%{_bindir}/hashstats
%{_mandir}/man?/%{name}.8%{?ext_man}
%{_mandir}/man?/hashstats.8%{?ext_man}
%{_mandir}/man?/show-shared-extents.8%{?ext_man}

%changelog
