#
# spec file for package mp3_check
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2011 Packman Team <packman@links2linux.de>
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


%define _lto_cflags %{nil}
Name:           mp3_check
Version:        1.98
Release:        0
Summary:        MP3 Format Validator
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://sourceforge.net/projects/mp3check/
Source:         https://downloads.sourceforge.net/mp3check/mp3_check-%{version}.tar.gz
Patch1:         mp3_check-fix_makefile.patch
Patch2:         mp3_check-fix_printf_format_for_size_t.patch
# PATCH-FIX-OPENSUSE mp3_check-gcc10.patch
Patch3:         mp3_check-gcc10.patch

%description
mp3_check helps identifying, in detail, MP3 files that do not
correctly follow the MPEG-1 Layer 3 format. It looks for invalid
frame headers, missing frames, etc., and generates statistics. This
can especially be important when building a file archive of a certain
quality.

%prep
%autosetup -p1

%build
%make_build \
    CC="gcc" \
    LOCALBASE="%{_prefix}" \
    CFLAGS="%{optflags} -fPIE" \
    OPT_FLAGS=""

%install
%make_build \
    CC="gcc" \
    LOCALBASE="%{_prefix}" \
    CFLAGS="%{optflags} -pie" \
    OPT_FLAGS="" \
    DESTDIR=%{buildroot} \
    install

%files
%doc README TODO
%{_bindir}/mp3_check

%changelog
