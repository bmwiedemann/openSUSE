#
# spec file for package afflib
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 0
Name:           afflib
Version:        3.7.22
Release:        0
Summary:        Library and tools for working with the Advanced Forensics Format
License:        BSD-4-Clause
URL:            https://github.com/sshock/AFFLIBv3
Source:         https://github.com/sshock/AFFLIBv3/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)

%description
The Advanced Forensics Format (AFF) is an openly specified, extensible file
format for storing and analyzing hard disk images and other types of digital
evidence.

%package -n libafflib%{sover}
Summary:        Library for working with the Advanced Forensics Format-Runtime support

%description -n libafflib%{sover}
The Advanced Forensics Format (AFF) is an openly specified, extensible file
format for storing and analyzing hard disk images and other types of digital
evidence.

This package contains the shared libraries necessary for software that needs to
work with the AFF library.

%package devel
Summary:        Library for working with the Advanced Forensics Format - Build support
Requires:       libafflib%{sover} = %{version}

%description devel
The Advanced Forensics Format (AFF) is an openly specified, extensible file
format for storing and analyzing hard disk images and other types of digital
evidence.

This package contains the files that are necessary to develop software that
makes use of afflib.

%package tools
Summary:        Tools for working with the Advanced Forensics Format

%description tools
The Advanced Forensics Format (AFF) is an openly specified, extensible file
format for storing and analyzing hard disk images and other types of digital
evidence.

This package contains the command line tools.

%prep
%autosetup -p1 -n AFFLIBv3-%{version}

%build
autoreconf -fiv
%configure \
	--disable-static \
	--enable-s3 \
	--enable-fuse \
	--with-expat \
	--with-curl \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n libafflib%{sover}

%files -n libafflib%{sover}
%license COPYING
%doc AUTHORS BUGLIST.txt NEWS README README_Linux.txt
%{_libdir}/libafflib.so.%{sover}{,.*}

%files devel
%license COPYING
%{_includedir}/afflib
%{_libdir}/libafflib.so
%{_libdir}/pkgconfig/afflib.pc

%files tools
%license COPYING
%{_bindir}/affcat
%{_bindir}/affcompare
%{_bindir}/affconvert
%{_bindir}/affcopy
%{_bindir}/affcrypto
%{_bindir}/affdiskprint
%{_bindir}/affinfo
%{_bindir}/affix
%{_bindir}/affrecover
%{_bindir}/affsegment
%{_bindir}/affsign
%{_bindir}/affstats
%{_bindir}/affuse
%{_bindir}/affverify
%{_bindir}/affxml
%{_mandir}/man1/*.1%{?ext_man}

%changelog
