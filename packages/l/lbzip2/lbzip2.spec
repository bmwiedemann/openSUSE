#
# spec file for package lbzip2
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


Name:           lbzip2
Version:        2.5
Release:        0
Summary:        Parallel bzip2/bunzip2 Filter
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Compression
URL:            http://lbzip2.org/
Source:         http://archive.lbzip2.org/lbzip2-%{version}.tar.bz2
BuildRequires:  libbz2-devel
Provides:       lbunzip2 = %{version}
Obsoletes:      lbunzip2 < %{version}

%description
Lbzip2 is a Pthreads-based parallel bzip2/bunzip2 filter, passable to GNU tar
with the --use-compress-program option.

It isn't restricted to regular files on input, nor output. Successful
splitting for decompression isn't guaranteed, just very likely (failure is
detected). Splitting in both modes and compression itself occur with an
approximate 900k block size.

On an Athlon-64 X2 6000+, lbzip2 was 92% faster than standard bzip2 when
compressing, and 45% faster when decompressing (based on wall clock time).

Lbzip2 strives to be portable by requiring UNIX 98 APIs only, besides an
unmodified libbz2.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/lbzip2
%{_bindir}/lbunzip2
%{_bindir}/lbzcat
%{_mandir}/man1/lbzip2.1%{?ext_man}
%{_mandir}/man1/lbunzip2.1%{?ext_man}
%{_mandir}/man1/lbzcat.1%{?ext_man}

%changelog
