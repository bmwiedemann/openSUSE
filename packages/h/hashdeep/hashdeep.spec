#
# spec file for package hashdeep
#
# Copyright (c) 2020 SUSE LLC
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


Name:           hashdeep
Version:        4.4
Release:        0
Summary:        Compute MD5, SHA-1, SHA-256, Tiger or Whirlpool message digests
License:        SUSE-Public-Domain AND GPL-2.0-or-later
Group:          System/Base
URL:            http://md5deep.sourceforge.net/
Source0:        https://github.com/jessek/hashdeep/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-errors-found-by-clang.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
Provides:       md5deep = %{version}
Obsoletes:      md5deep < %{version}

%description
hashdeep is a program to compute, match, and audit hashsets.
md5deep computes the MD5, SHA-1, SHA-256, Tiger, or Whirlpool message digest
for any number of files while optionally recursively digging through the
directory structure. md5deep can also match input files against lists of known
hashes in a variety of formats.

%prep
%autosetup -p1 -n %{name}-release-%{version}

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/hashdeep
%{_bindir}/md5deep
%{_bindir}/sha1deep
%{_bindir}/sha256deep
%{_bindir}/tigerdeep
%{_bindir}/whirlpooldeep
%{_mandir}/man1/hashdeep.1%{?ext_man}
%{_mandir}/man1/md5deep.1%{?ext_man}
%{_mandir}/man1/sha1deep.1%{?ext_man}
%{_mandir}/man1/sha256deep.1%{?ext_man}
%{_mandir}/man1/whirlpooldeep.1%{?ext_man}
%{_mandir}/man1/tigerdeep.1%{?ext_man}

%changelog
