#
# spec file for package pbzip2
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


Name:           pbzip2
Version:        1.1.13
Release:        0
Summary:        Parallelized Implementation of bzip2
License:        BSD-4-Clause
Group:          Productivity/Archiving/Compression
URL:            http://compression.ca/pbzip2/
Source0:        https://launchpad.net/pbzip2/1.1/%{version}/+download/pbzip2-%{version}.tar.gz
# pbleser: fix not using the result value of fwrite()
Patch3:         pbzip2-fix_unused_result.patch
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines.

%prep
%setup -q
%patch3

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"

%install
%make_install

for x in pbunzip2 pbzcat; do
    ln -s "pbzip2.1%{ext_man}" "%{buildroot}%{_mandir}/man1/${x}.1%{ext_man}"
done

%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_bindir}/pbzip2
%{_bindir}/pbunzip2
%{_bindir}/pbzcat
%{_mandir}/man1/pbzip2.1%{?ext_man}
%{_mandir}/man1/pbunzip2.1%{?ext_man}
%{_mandir}/man1/pbzcat.1%{?ext_man}

%changelog
