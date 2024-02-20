#
# spec file for package indent
#
# Copyright (c) 2024 SUSE LLC
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


Name:           indent
Version:        2.2.13
Release:        0
Summary:        Indentation of Source Code in various styles
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.gnu.org/software/indent
Source0:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=94096#/%{name}.keyring
# PATCH-FIX-SECURITY fix-out-of-buffer-read-CVE-2023-40305.patch fix-heap-buffer-overwrite-search_brace-CVE-2023-40305 bsc#1214243 CVE-2023-40305 antonio.teixeira@suse.com -- indent: heap-based buffer overflow in search_brace() in indent.c via a crafted file
Patch0:         fix-out-of-buffer-read-CVE-2023-40305.patch
Patch1:         fix-heap-buffer-overwrite-search_brace-CVE-2023-40305.patch
# CVE-2024-0911 [bsc#1219210], heap-based buffer overflow in set_buf_break()
Patch2:         indent-CVE-2024-0911.patch
BuildRequires:  makeinfo
BuildRequires:  texi2html

%description
Indent can be used to make code easier to read. It can also convert
from one style of writing C code to another. indent understands a
substantial amount of C syntax, but it also tries to cope with
incomplete and malformed syntax.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	%{nil}
%make_build

%install
%make_install
rm -f %{buildroot}%{_bindir}/texinfo2man
rm -f %{buildroot}/%{_infodir}/dir
%find_lang %{name}

%check
%make_build check

%files
%{_bindir}/*
%license COPYING
%doc NEWS ChangeLog
%{_docdir}/%{name}
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/indent.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
