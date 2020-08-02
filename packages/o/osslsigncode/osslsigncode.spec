#
# spec file for package osslsigncode
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Summary:        Platform-independent tool for Authenticode signing of EXE/CAB files
License:        GPL-3.0
Group:          Productivity/Security
Url:            http://osslsigncode.sourceforge.net/
Name:           osslsigncode
Version:        1.7.1
Release:        0
Source0:        http://downloads.sourceforge.net/project/osslsigncode/osslsigncode/osslsigncode-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libgsf-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcrypto) >= 1.1
BuildRequires:  pkgconfig(libcurl)
Patch0:         0001-Make-code-work-with-OpenSSL-1.1.patch

%description
osslsigncode is a small utility for placing signatures on Microsoft cabinate
files and executables.

%prep
%setup -q
%patch0 -p1
%build
%configure
make

%install
%make_install

%files
%defattr(-, root, root)
%license COPYING
%doc README
%{_bindir}/*

%changelog
