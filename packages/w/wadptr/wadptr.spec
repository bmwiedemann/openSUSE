#
# spec file for package wadptr
#
# Copyright (c) 2025 SUSE LLC
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


Name:           wadptr
Version:        3.6
Release:        0
Group:          Development/Tools/Building
Summary:        Redundancy compressor for Doom WAD files
License:        GPL-2.0-or-later
URL:            http://soulsphere.org/projects/wadptr/
#Git-Clone:     https://github.com/fragglet/wadptr
Source:         https://github.com/fragglet/wadptr/archive/refs/tags/%name-%version.tar.gz
BuildRequires:  automake
BuildRequires:  xz

%description
WADptr is a utility for reducing the size of Doom WAD files. The
"compressed" WADs will still work the same as the originals. The
program works by exploiting the WAD file format to combine repeated /
redundant material.

%prep
%autosetup -p1 -n %name-%name-%version

%build
%make_build CFLAGS="%optflags"

%install
%make_install PREFIX="%_prefix"

%files
%_bindir/*
%_mandir/man*/*.[0-9]*
%license COPYING.md

%changelog
