#
# spec file for package fs_mark
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2003-2004 EMC Corporation
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


Name:           fs_mark
Version:        3.3
Release:        0
Summary:        Filesystem benchmark
License:        GPL-2.0+
Group:          System/Benchmark
Url:            http://fsmark.sf.net
Source0:        http://sourceforge.net/projects/fsmark/files/fsmark/%{version}/%{name}-%{version}.tar.gz
Source1:        http://www.gnu.org/licenses/gpl-2.0.txt
Patch1:         fs_mark-Allow-creating-files-filled-with-random-bytes.patch
Patch2:         fs_mark-nostatic.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The fs_mark benchmark tests synchronous write workloads. It can vary the number
of files, directory depth, etc. It has detailed timings for reads, writes,
unlinks and fsyncs that make it good for simulating mail servers and other
setups.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
cp %{SOURCE1} .

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -D -m 0755 fs_mark %{buildroot}%{_bindir}/fs_mark

%files
%defattr(-,root,root)
%doc README gpl-2.0.txt
%{_bindir}/fs_mark

%changelog
