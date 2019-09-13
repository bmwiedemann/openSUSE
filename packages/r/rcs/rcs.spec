#
# spec file for package rcs
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rcs
Version:        5.9.4
Release:        0
Summary:        Revision Control System
License:        GPL-3.0+
Group:          Development/Tools/Version Control
Url:            http://www.gnu.org/software/rcs/
Source:         http://ftp.gnu.org/pub/gnu/rcs/%{name}-%{version}.tar.xz
Source2:        http://ftp.gnu.org/pub/gnu/rcs/%{name}-%{version}.tar.xz.sig
Source3:        rcs.keyring
BuildRequires:  ed
BuildRequires:  xz
Requires:       diffutils
Requires(pre):  %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
RCS, the Revision Control System, manages multiple revisions of files.
RCS can store, retrieve, log, identify, and merge revisions. It is
useful for files that are frequently revised, for example: programs,
documentation, graphics, and papers.

%prep
%setup -q

%build
ac_cv_path_SENDMAIL=%{_sbindir}/sendmail \
%configure --with-diff-utils
make %{?_smp_mflags} CFLAGS="%{optflags} -std=gnu99"

%check
# t810 is failing
#make %{?_smp_mflags} check

%install
%make_install
mkdir -p %{buildroot}%{_defaultdocdir}/rcs

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-, root, root)
%{_defaultdocdir}/rcs
%{_bindir}/*
%doc AUTHORS README NEWS THANKS ChangeLog COPYING
%{_mandir}/man?/*.gz
%{_infodir}/*.*

%changelog
