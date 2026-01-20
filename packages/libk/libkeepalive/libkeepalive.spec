#
# spec file for package libkeepalive
#
# Copyright (c) 2026 SUSE LLC
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


Name:           libkeepalive
Version:        0.3
Release:        0
Summary:        Enable TCP keepalive in dynamic binaries
URL:            http://libkeepalive.sourceforge.net/
License:        MIT
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# All patches sent to the upstream maintainer directly via email.
Patch1:         0001-Add-vim-modelines-to-source-files.patch
Patch2:         0002-test-test.c-Whitespace-cleanup.patch
Patch3:         0003-test-Implement-self-test-functionality.patch
Patch4:         0004-Makefile-Make-self-test-accessible-by-make-test.patch
Patch5:         0005-Makefile-Allow-setting-custom-compiler-flags.patch
BuildRequires:  gcc
BuildRequires:  make

%description
libkeepalive is a library that enables tcp keepalive features in glibc based
binary dynamic executables, without any change in the original program.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
LDFLAGS="${LDFLAGS:-%{?build_ldflags}}" ; export LDFLAGS
%make_build

%check
make test

%install
# install the file in src not topdir - the latter is stripped already
install -p -m 0755 -D src/libkeepalive.so %{buildroot}%{_libdir}/libkeepalive.so

%files
%license LICENSE
%doc README
%{_libdir}/libkeepalive.so

%changelog
