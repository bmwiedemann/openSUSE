#
# spec file for package compsize
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


Name:           compsize
Version:        1.3
Release:        0
Summary:        Utility for measuring compression ratio of files on btrfs
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://github.com/kilobyte/compsize
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libbtrfs-devel

%description
compsize takes a list of files (given as arguments) on a btrfs
filesystem and measures used compression types and effective
compression ratio, producing a report.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags}"

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
