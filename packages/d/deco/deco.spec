#
# spec file for package deco
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


Name:           deco
Version:        1.6.4
Release:        0
Summary:        Deco Archive File Extractor
License:        GPL-3.0-only
URL:            https://github.com/peha/deco
Source:         https://github.com/peha/deco/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       bzip2
Requires:       gzip
Requires:       tar
Suggests:       arc
Suggests:       arj
Suggests:       cpio
Suggests:       flac
Suggests:       lha
Suggests:       lzop
Suggests:       nomarch
Suggests:       p7zip
Suggests:       rar
Suggests:       unace
Suggests:       unalz
Suggests:       unarj
Suggests:       unrar
Suggests:       unzip
Suggests:       zip

%description
deco is a generic archive file extractor that has a consistent command line
interface ("deco 1.tar.bz2 2.zip 3.flac 4.rar 5.deb" will just work) and
consistent behavior (it never deletes archives after extraction, extracts
relative to the current working directory, and extracts just verbosely enough,
all unless explicitly requested otherwise). It provides automatic handling of
extractor gotchas by creating an extraction directory if there is more than
one file or directory at the archive top level and by being able to fix
strange permissions. 33 archive file extensions are supported out of the box,
and adding support for others requires very little work.

%prep
%autosetup

%build
%make_build CC="cc" CFLAGS="%{optflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/deco

%changelog
