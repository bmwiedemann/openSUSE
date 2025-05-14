#
# spec file for package tinyssh
#
# Copyright (c) 2025 SUSE LLC
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


Name:           tinyssh
Version:        20250501
Release:        0
Summary:        A minimalistic SSH server which implements only a subset of SSHv2 features
License:        CC0-1.0
Group:          Productivity/Networking/SSH
URL:            https://tinyssh.org/
Source0:        https://github.com/janmojzis/tinyssh/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/janmojzis/tinyssh/releases/download/%{version}/%{version}.tar.gz.asc
Source2:        %{name}-%{version}.tar.gz
Source3:        %{version}.tar.gz.asc
Source4:        %{name}.keyring
Patch0:         tinyssh-gcc14-compat.patch

%description
tinyssh is a minimalistic SSH server which implements only a subset of SSHv2
features. It supports only secure cryptography (minimum 128-bit security,
protected against cache-timing attacks) and doesn't implement unnecessary
features (such as SSH1 protocol, compression, ...) or older crypto (such as
RSA, DSA, HMAC-MD5, HMAC-SHA1, 3DES, RC4, ...). tinysshd doesn't implement
unsafe features (such as password or hostbased authentication) or doesn't
use dynamic memory allocation (no allocation failures, etc.)

%prep
%autosetup -a2

%build
export CFLAGS="%{optflags}"
%make_build

%install
export PREFIX=/usr
%make_install

%if 0%{?suse_version} > 1315
%check
%make_build test
%endif

%files
%license LICENCE.md
%doc README*
%{_sbindir}/tinysshd
%{_sbindir}/tinysshd-makekey
%{_sbindir}/tinysshd-printkey
%{_sbindir}/tinysshnoneauthd
%{_mandir}/man8/tinysshd-makekey.8%{?ext_man}
%{_mandir}/man8/tinysshd-printkey.8%{?ext_man}
%{_mandir}/man8/tinysshd.8%{?ext_man}
%{_mandir}/man8/tinysshnoneauthd.8%{?ext_man}

%changelog
