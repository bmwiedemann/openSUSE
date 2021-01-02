#
# spec file for package dash
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2013 Guido Berhoerster.
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


Name:           dash
Version:        0.5.11.3
Release:        0
Summary:        POSIX-compliant Implementation of /bin/sh
License:        BSD-3-Clause
Group:          System/Shells
URL:            http://gondor.apana.org.au/~herbert/dash/
Source:         http://gondor.apana.org.au/~herbert/dash/files/dash-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: https://git.kernel.org/pub/scm/utils/dash/dash.git/commit/?id=29d6f2148f10213de4e904d515e792d2cf8c968e
Patch1:         check-nflag-in-evaltree.patch
BuildRequires:  libedit-devel

%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as
possible without sacrificing speed where possible.

%prep
%setup -q
%autopatch -p1

%build
%global optflags %{optflags} -fcommon
%configure \
	--enable-fnmatch \
	--enable-glob \
	--with-libedit
%make_build

%install
%make_install
# compatibility symlink to /bin
%if !0%{?usrmerged}
mkdir -p %{buildroot}/bin
ln -s %{_bindir}/dash %{buildroot}/bin/dash
%endif

%files
%license COPYING
%doc ChangeLog
%{_bindir}/dash
%if !0%{?usrmerged}
/bin/dash
%endif
%{_mandir}/man1/dash.1%{?ext_man}

%changelog
