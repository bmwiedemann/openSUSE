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
Version:        0.5.11.1
Release:        0
Summary:        POSIX-compliant Implementation of /bin/sh
License:        BSD-3-Clause
Group:          System/Shells
URL:            http://gondor.apana.org.au/~herbert/dash/
Source:         http://gondor.apana.org.au/~herbert/dash/files/dash-%{version}.tar.gz
BuildRequires:  libedit-devel

%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as
possible without sacrificing speed where possible.

%prep
%setup -q

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
mkdir -p %{buildroot}/bin
ln -s %{_bindir}/dash %{buildroot}/bin/dash

%files
%doc ChangeLog
%{_bindir}/dash
/bin/dash
%{_mandir}/man1/dash.1%{?ext_man}

%changelog
