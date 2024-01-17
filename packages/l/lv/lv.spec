#
# spec file for package lv
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lv
Version:        4.51
Release:        0
Summary:        Multilingual file viewer with user interface like "less"
License:        GPL-2.0+
Group:          Productivity/Text/Utilities
Url:            http://www.ff.iij4u.or.jp/~nrt/lv/
Source:         lv451.tar.bz2
Patch0:         lv-add-lgrep-man-page.patch
Patch2:         lv-fixes.patch
Patch3:         lv-strip.patch
Patch4:         missing-include.patch
Patch5:         lv-splitted-libtinfo.patch
BuildRequires:  automake
BuildRequires:  ncurses-devel
Provides:       locale(ja;ko;zh)

%description
Lv is a multilingual file viewer and looks like the "less" utility.
It can decode and encode multilingual streams through many coding
systems, and can be used as a coding system translation filter. Lv
can recognize multibyte patterns as regular expressions, and provides
multilingual grep functionality under the name lgrep. It also
recognizes ANSI escape sequences for text decoration.

%prep
%setup -q -n lv451
%patch0 -p1 -b .add-lgrep-man-page
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
pushd src
autoreconf -fvi
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing" \
CXXFLAGS="%{optflags}  -D_FILE_OFFSET_BITS=64 -fno-strict-aliasing" \
%configure
make %{?_smp_mflags}
popd

%install
cd src
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
make install bindir=%{buildroot}%{_bindir} libdir=%{buildroot}%{_libdir} mandir=%{buildroot}%{_mandir} INSTALL="install -p"

%files
%defattr(-,root,root)
%doc GPL.txt README *.html hello*
%{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/lv

%changelog
