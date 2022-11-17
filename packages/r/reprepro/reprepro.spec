#
# spec file for package reprepro
#
# Copyright (c) 2022 SUSE LLC
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


Name:           reprepro
Version:        5.4.1
Release:        0
Summary:        Debian repository metadata generator
License:        GPL-2.0-only AND GPL-2.0-or-later AND MIT
URL:            https://salsa.debian.org/debian/reprepro
Source:         http://deb.debian.org/debian/pool/main/r/reprepro/reprepro_%version.orig.tar.xz
BuildRequires:  automake
BuildRequires:  gpgme-devel
BuildRequires:  libarchive-devel
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version}
BuildRequires:  libbz2-devel
BuildRequires:  libdb-4_8-devel
Requires:       gpg2
%else
BuildRequires:  bzip2-devel
BuildRequires:  (db4-devel or libdb-devel)
Requires:       gnupg2
%endif
Requires:       bzip2
Requires:       tar
Requires:       zstd

%description
reprepro is a tool to manage a repository of Debian packages (.deb).  It
stores files either being injected manually or downloaded from some other
repository (partially) mirrored into one pool/ hierarchy.  Managed packages
and files are stored in a Berkeley DB, so no database server is needed.
Checking signatures of mirrored repositories and creating signatures of the
generated Package indexes is supported.

%prep
%autosetup -p1
find docs -type f -exec chmod -x {} +

%build
export CFLAGS="%optflags -g"
autoreconf -fi
%configure
%make_build

%install
%make_install
pushd docs
rm -v Makefile Makefile.am Makefile.in changestool.1 rredtool.1 reprepro.1

%files
%license COPYING
%doc docs/ AUTHORS README NEWS
%_mandir/man1/*.1*
%_bindir/changestool
%_bindir/reprepro
%_bindir/rredtool

%changelog
