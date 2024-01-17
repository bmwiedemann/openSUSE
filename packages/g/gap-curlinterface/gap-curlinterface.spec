#
# spec file for package gap-curlinterface
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gap-curlinterface
Version:        2.3.2
Release:        0
Summary:        GAP: Web Access via curl
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/curlInterface/
#Git-Clone:	https://github.com/gap-packages/curlInterface
Source:         https://github.com/gap-packages/curlInterface/releases/download/v%version/curlInterface-%version.tar.gz
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
BuildRequires:  pkgconfig(libcurl)
Requires:       gap-core >= 4.9
Requires:       gap-gapdoc >= 1.5

%description
This package provides a wrapper around libcurl, to allow downloading
files over http, ftp and https from within the GAP processor.

%prep
%autosetup -n curlInterface-%version

%build
%configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$fmoddir/"
rm -Rfv config.* configure* Makefile* gen/ src/
find . -type f -size 0 -name _Chunks.xml -print -delete
popd

%files -f %name.files

%changelog
