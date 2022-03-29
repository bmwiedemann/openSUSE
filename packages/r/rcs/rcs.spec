#
# spec file for package rcs
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


Name:           rcs
Version:        5.10.1
Release:        0
Summary:        Revision Control System
License:        GPL-3.0-or-later
Group:          Development/Tools/Version Control
URL:            https://www.gnu.org/software/rcs/
Source:         https://ftp.gnu.org/pub/gnu/rcs/%{name}-%{version}.tar.lz
Source1:        https://ftp.gnu.org/pub/gnu/rcs/%{name}-%{version}.tar.lz.sig
Source2:        rcs.keyring
Patch0:         rcs-glibc-2.34.patch
BuildRequires:  ed
BuildRequires:  lzip
Requires:       diffutils

%description
RCS, the Revision Control System, manages multiple revisions of files.
RCS can store, retrieve, log, identify, and merge revisions. It is
useful for files that are frequently revised, for example: programs,
documentation, graphics, and papers.

%prep
%setup -q
%if 0%{?suse_version} >= 1550
%patch0 -p1
%endif

%build
ac_cv_path_SENDMAIL=%{_sbindir}/sendmail \
%configure --with-diff-utils
%make_build

%check
%make_build check

%install
%make_install
mkdir -p %{buildroot}%{_defaultdocdir}/rcs

%files
%{_defaultdocdir}/rcs
%{_bindir}/*
%license COPYING
%doc AUTHORS README NEWS THANKS ChangeLog
%{_mandir}/man?/*.gz
%{_infodir}/*.*

%changelog
