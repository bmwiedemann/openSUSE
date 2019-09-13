#
# spec file for package duperemove
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


%define samename btrfs-extent-same
Name:           duperemove
Version:        0.11.1
Release:        0
Summary:        Software to find duplicate extents in files and remove them
License:        GPL-2.0
Group:          System/Filesystems
Url:            https://github.com/markfasheh/duperemove
Source:         https://github.com/markfasheh/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%if 0%{?suse_version} <= 1200
make %{?_smp_mflags} CFLAGS="%{optflags} -DNO_BTRFS_HEADER"
%else
make %{?_smp_mflags} CFLAGS="%{optflags}"
%endif

%install
%make_install PREFIX="%{_prefix}"

%files -n %{samename}
%defattr(-, root, root)
%{_sbindir}/%{samename}
%{_mandir}/man?/%{samename}.8%{ext_man}

%files
%defattr(-, root, root)
%doc LICENSE README.md
%{_sbindir}/duperemove
%{_sbindir}/hashstats
%{_sbindir}/show-shared-extents
%{_mandir}/man?/%{name}.8%{ext_man}
%{_mandir}/man?/hashstats.8%{ext_man}
%{_mandir}/man?/show-shared-extents.8%{ext_man}

%changelog
