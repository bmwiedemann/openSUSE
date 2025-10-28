#
# spec file for package archivemount-ng
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           archivemount-ng
Version:        1a
Release:        0
Summary:        Mount archives as a file system
License:        0BSD AND LGPL-2.1-or-later
URL:            https://git.sr.ht/~nabijaczleweli/archivemount-ng
Source:         https://git.sr.ht/~nabijaczleweli/archivemount-ng/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# fails download_files
#Source2:        https://git.sr.ht/~nabijaczleweli/archivemount-ng/archive/%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source2:        %{name}-%{version}.tar.gz.asc
Source3:        https://nabijaczleweli.xyz/pgp.txt#/%{name}.keyring
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libarchive)
Requires:       fuse3
Conflicts:      archivemount
Provides:       archivemount = %{version}
Obsoletes:      archivemount < %{version}
%if 0%{?suse_version} < 1600
# -std=c++2b
BuildRequires:  gcc12-c++
%endif

%description
Archivemount is a piece of glue code between libarchive and FUSE. It can be
used to mount a (possibly compressed) archive (as in .tar.gz or .zip or .iso)
and use it like an ordinary filesystem.

This version of the package is a fork and continuation of the original
archivemount, with fuse 3 support and bug fixes.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif
# for --version output
export VERSION=%{version}
%make_build

%install
%make_install \
	PREFIX=%{_prefix} \
	%{nil}

# qemu emulation does not support setuid programs
%if !0%{?qemu_user_space_build}
%check
%make_build check
%endif

%files
%license LICENSES/LGPL-2.0-or-later.txt LICENSES/0BSD.txt
%doc README
%{_bindir}/archivemount
%{_mandir}/man1/archivemount.1%{?ext_man}

%changelog
