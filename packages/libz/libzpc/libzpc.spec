#
# spec file for package libzpc
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           libzpc
Version:        2.0.0
Release:        0
Summary:        IBM Z Protected-key Crypto library
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/opencryptoki/libzpc
Source0:        https://github.com/opencryptoki/libzpc/archive/refs/tags/v%{version}.tar.gz#/libzpc-%{version}.tar.gz
Source1:        libzpc-man-%{version}.tar.gz

BuildRequires:  clang
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc-c++
BuildRequires:  libjson-c-devel

BuildRequires:  pkgconfig(libcrypto) >= 3.0.7
BuildRequires:  pkgconfig(libssl) >= 3.0.7

ExclusiveArch:  s390x

# Upgrade path handling for v2.0.0 architectural split.
# The current architecture of libzpc 2.0.0
# does not support a development package.
### Obsoletes:      libzpc1 < %%{version}-%%{release}
### Obsoletes:      libzpc-devel < %%{version}-%%{release}
### Provides:       libzpc = %%{version}-%%{release}

%description
The IBM Z Protected-key Crypto library libzpc is a library targeting
the 64-bit Linux on IBM Z (s390x) platform. It provides interfaces for
cryptographic primitives. The underlying implementations make use of
z/Architecture's performance-boosting hardware support and its
protected-key feature which ensures that key material is never present
in main memory at any time.

%prep
%autosetup -p1

%build
%cmake -DBUILD_DOC=OFF
%make_build

%install
cd build
# Create dummy files so the installer doesn't crash when BUILD_DOC=OFF
touch zpckey.1 hbkzpcprovider.conf.5 hbkzpcprovider.7
%make_install

# Overwrite the dummy files with the real pre-generated man pages
tar -xzf %{SOURCE1} -C %{buildroot}%{_datadir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/zpckey
%{_libdir}/ossl-modules/zpcprovider.so
%{_mandir}/man1/zpckey.1*
%{_mandir}/man5/hbkzpcprovider.conf.5*
%{_mandir}/man7/hbkzpcprovider.7*

%changelog
