#
# spec file for package zutils
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


Name:           zutils
Version:        1.12
Release:        0
Summary:        Collection of utilities for dealing with compressed files
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://www.nongnu.org/zutils/zutils.html
Source0:        https://download.savannah.gnu.org/releases/zutils/zutils-%{version}.tar.lz
Source1:        https://download.savannah.gnu.org/releases/zutils/zutils-%{version}.tar.lz.sig
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE zutils-1.7-noconflict.patch
Patch1:         zutils-1.7-noconflict.patch
BuildRequires:  gcc-c++
BuildRequires:  lzip

%description
Zutils is a collection of utilities able to deal with any combination
of compressed and uncompressed files transparently. If any given file,
including standard input, is compressed, its decompressed content is
used. Compressed files are decompressed on the fly; no temporary files
are created.
These utilities are not wrapper scripts but safer and more efficient
C++ programs. In particular the "--recursive" option is very efficient
in those utilities supporting it.

%prep
%autosetup -p1

%build
%configure CXXFLAGS="%{optflags}"
%make_build

%install
%make_install

%check
%make_build check

%files
%doc ChangeLog README
%license COPYING
%{_sysconfdir}/zutils.conf
%{_bindir}/*
%{_infodir}/*.info%{?ext_info}
%{_mandir}/man1/*.1%{?ext_man}

%changelog
