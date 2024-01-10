#
# spec file for package gap-ace
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


Name:           gap-ace
Version:        5.6.2
Release:        0
Summary:        GAP: Advanced Coset Enumerator
License:        MIT
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/ace/

#Git-Clone:	https://github.com/gap-packages/ace
Source:         https://github.com/gap-packages/ace/releases/download/v%version/ace-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.7

%description
The ACE package provides functions associated with Todd-Coxeter coset
enumeration by interfacing with the Advanced Coset Enumerator (ACE)
from within GAP.

%prep
%autosetup -n ace-%version

%build
./configure "%gapdir"
%make_build CC="cc %optflags"

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
