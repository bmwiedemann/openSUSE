#
# spec file for package gap-ctbllib
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gap-ctbllib
Version:        1.3.6
Release:        0
Summary:        GAP Character Table Library
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.math.rwth-aachen.de/homes/Thomas.Breuer/ctbllib/
Source:         https://www.math.rwth-aachen.de/homes/Thomas.Breuer/ctbllib/ctbllib-%version.tar.gz
#changelog in chap1.txt
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-atlasrep >= 2.1
Requires:       gap-core >= 4.11
Requires:       gap-gapdoc >= 1.6.2
Suggests:       gap-browse >= 1.8.10
Suggests:       gap-chevie >= 1.0
Suggests:       gap-primgrp >= 1.0
Suggests:       gap-smallgrp >= 1.0
Suggests:       gap-spinsym >= 1.5
Suggests:       gap-tomlib >= 1.0
Suggests:       gap-transgrp >= 1.0

%description
The package contains the GAP Character Table Library.

%prep
%autosetup -n ctbllib-%version
chmod a-x doc/*.xml

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
