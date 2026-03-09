# Copyright (c) 2025 Szőts Ákos <szotsaki@gmail.com>
# Copyright (c) 2013 Huaren Zhong <huaren.zhong@gmail.com>
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

Name:           uniutils
Version:        2.28
Release:        0
Summary:        Unicode utilities
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://billposer.org/Software/unidesc.html
Source:         http://billposer.org/Software/Downloads/uniutils-%{version}.tar.bz2
Patch0:         error-return-type.patch
# Debian patches: https://sources.debian.org/patches/uniutils
Patch1:         gcc-14.patch
Patch2:         uniname_typo.patch
Patch3:         unicode14.patch
Patch4:         unicode15.patch
Patch5:         unicode16.patch
BuildRequires:  autoconf
BuildRequires:  automake

%description
This package consists of a set of programs for manipulating and analyzing Unicode text. The analysis utilities are useful when working with Unicode files when one doesn't know the writing system, doesn't have the necessary font, needs to inspect invisible characters, needs to find out whether characters have been combined or in what order they occur, or needs statistics on which characters occur.

%prep
%autosetup -p1

%build
%configure
%make_build

%check
%make_build check

%install
%make_install

install -D -m 444 genunames.awk %{buildroot}%{_datadir}/%{name}/genunames.awk

# "install-strip" handling is buggy in "install-sh":
# cp: cannot create regular file '/usr/bin/#inst.595163#': Permission denied
# %%make_build install-strip

%files
%doc ChangeLog NEWS README TODO CREDITS AUTHORS
%license COPYING
%{_bindir}/ExplicateUTF8
%{_bindir}/unidesc
%{_bindir}/uniname
%{_bindir}/unihist
%{_bindir}/unireverse
%{_bindir}/unifuzz
%{_bindir}/unisurrogate
%{_bindir}/utf8lookup
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/genunames.awk
%{_mandir}/man1/*.1%{?ext_man}

%changelog
