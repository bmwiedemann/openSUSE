#
# spec file for package apg
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           apg
Version:        2.2.3
Release:        0
Summary:        Tool Set for Random Password Generation
License:        BSD-3-Clause
Group:          Productivity/Security
Url:            http://www.adel.nursat.kz/apg/
Source0:        http://www.adel.nursat.kz/apg/download/apg-%{version}.tar.gz
Patch1:         apg-do_not_install_as_root.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
APG (Automated Password Generator) is a tool set for generating random
passwords. A standalone tool generates some random words of the required type
and prints them to standard output. A networked client/server following RFC972
is also provided.

%prep
%setup -q
%patch1

%build
make %{?_smp_mflags} \
    CC="gcc" \
    FLAGS="%{optflags} -Wall" \
    CS_LIBS="-lnsl" \
    FIND_GROUP="0" \
    USE_SHA="APG_USE_SHA" \
    CRYPTED_PASS="APG_USE_CRYPT" \
    INSTALL_PREFIX="%{_prefix}" \
    APG_MAN_DIR="/share/man/man1" \
    APGD_MAN_DIR="/share/man/man8" \
    standalone

%install
make %{?_smp_mflags} \
    FIND_GROUP="0" \
    USE_SHA="APG_USE_SHA" \
    CRYPTED_PASS="APG_USE_CRYPT" \
    INSTALL_PREFIX="%{buildroot}%{_prefix}" \
    APG_MAN_DIR="/share/man/man1" \
    APGD_MAN_DIR="/share/man/man8" \
    install

%files
%defattr(-,root,root)
%doc CHANGES COPYING README THANKS TODO
%doc doc/APG_TIPS doc/*.txt
%{_bindir}/apg
%{_bindir}/apgbfm
%{_mandir}/man1/apg.1%{ext_man}
%{_mandir}/man1/apgbfm.1%{ext_man}

%changelog
