#
# spec file for package gap-crypting
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gap-crypting
Version:        0.10.4
Release:        0
Summary:        GAP: Support for hashes and crypto
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/crypting/
#Git-Clone:	https://github.com/gap-packages/crypting
Source:         https://github.com/gap-packages/crypting/releases/download/v%version/crypting-%version.tar.gz
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10
Requires:       gap-gapdoc >= 1.5

%description
This GAP module implements some cryptographic primitives. At the
moment this is a custom implementation of SHA256 and HMAC, which is
needed to sign messages in the Jupyter kernel.

%prep
%autosetup -n crypting-%version

%build
./configure "%gapdir"
%make_build
find . -type f -size 0 -name _Chunks.xml -print -delete

%install
%gappkg_simple_install
pushd "%buildroot/$moddir/"
rm -Rf src
popd

%files -f %name.files

%changelog
