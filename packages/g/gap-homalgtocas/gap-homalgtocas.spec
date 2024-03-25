#
# spec file for package gap-homalgtocas
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gap-homalgtocas
Version:        2023.11.01
%define sillyver 2023.11-01
Release:        0
Summary:        GAP: Abstraction layer for Homalg to access external CAS
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/HomalgToCAS
#Git-Clone:	https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/HomalgToCAS-%sillyver/HomalgToCAS-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-matricesforhomalg >= 2023.08.01
Requires:       gap-toolsforhomalg >= 2023.11.01
Suggests:       gap-io >= 2.3

%description
HomalgToCAS provides a layer for abstraction for further GAP modules
to access an external CAS program (computer algebra system).

%prep
%autosetup -n HomalgToCAS-%sillyver

%build
find . -type f -name "*.git*" -delete
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
