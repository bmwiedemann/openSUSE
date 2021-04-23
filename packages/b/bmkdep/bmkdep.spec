#
# spec file for package bmkdep
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bmkdep
Version:        20140112
Release:        0
Summary:        The NetBSD version of mkdep(1) tool
License:        BSD-2-Clause
Group:          Development/Tools/Building
URL:            https://github.com/trociny/bmkdep
Source:         %{name}-%{version}.tar.gz

BuildRequires:  bmake

%description
bmkdep constructs Makefile dependency list. It takes
a set of flags for the C compiler and a list of C source
files as arguments and constructs a set of include file dependencies
which are written into the file ".depend".

%prep
%setup -q

%define env \
  unset MAKEFLAGS \
  env CFLAGS="%{optflags}" \
  export PREFIX=%{_prefix} \
  export SYSCONFDIR=%{_sysconfdir} \
  export BINOWN=`id -un` \
  export MANOWN=$BINOWN \
  export BINGRP=`id -gn` \
  export MANGRP=$BINOWN

%define flags MANTARGET=man MANDIR=%{_mandir}

%build
%{env}
bmake all %{flags}

%install
%{env}
bmake install %{flags} DESTDIR=%{buildroot}

%files
%{_bindir}/bmkdep
%{_mandir}/man1/bmkdep.1%{?ext_man}

%changelog
