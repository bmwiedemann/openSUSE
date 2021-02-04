#
# spec file for package lsof
#
# Copyright (c) 2021 SUSE LLC
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


Name:           lsof
Version:        4.93.2
Release:        0
Summary:        A Program That Lists Information about Files Opened by Processes
License:        Zlib
Group:          System/Monitoring
URL:            https://github.com/lsof-org/lsof
# From https://github.com/lsof-org/lsof/archive/%{version}.tar.gz
# Always repack the source to remove legally problematic files - bnc#705143
# dialects/uw/uw7/sys/fs/{fifonode.h,namenode.h,README}
Source:         lsof-%{version}_repacked.tar.gz
Patch0:         lsof_4.81-include.patch
Patch1:         lsof_4.81-fmt.patch
Patch2:         lsof-no-build-date-etc.patch
Patch3:         lsof_4.81-perl.patch
Patch4:         lsof-glibc-linux-5.0.patch
BuildRequires:  libselinux-devel
BuildRequires:  xz

%description
Lsof lists information about files opened by processes. An open file
may be a regular file, a directory, a block special file, a character
special file, an executing text reference, a library, a stream, or a
network file (Internet socket, NFS file, or UNIX domain socket.)  A
specific  file or all the files in a file system may be selected by
path.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4 -p1

%build
./Configure -n linux
make %{?_smp_mflags} DEBUG="%{optflags} -Wall -Wno-unused"

%install
install -m755 -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man8
install -m755 lsof %{buildroot}%{_bindir}
install -m644 Lsof.8 %{buildroot}%{_mandir}/man8/lsof.8
mkdir SUSE_docs
for s in 00* ; do
	mv $s SUSE_docs/${s#00}
done
sed -i -e "s|%{_prefix}/local/bin/perl|%{_bindir}/perl|g" scripts/*
mv scripts/00MANIFEST scripts/MANIFEST
mv scripts/00README scripts/README

%check
cd tests
chmod u+w TestDB
./Add2TestDB
make %{?_smp_mflags} DEBUG="%{optflags} -Wall -Wno-unused"

%files
%doc SUSE_docs/* scripts
%{_mandir}/man8/lsof.8%{ext_man}
%{_bindir}/lsof

%changelog
