#
# spec file for package gap-scscp
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


Name:           gap-scscp
Version:        2.4.2
Release:        0
Summary:        GAP: Symbolic Computation Software Composability Protocol in GAP
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/scscp/
#Git-Clone:     https://github.com/gap-packages/scscp
Source:         https://github.com/gap-packages/scscp/releases/download/v%version/scscp-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10
Requires:       gap-gapdoc >= 1.5
Requires:       gap-io >= 4.4
Requires:       gap-openmath >= 11.4.1

%description
The GAP package SCSCP implements the Symbolic Computation Software
Composability Protocol for the computational algebra system GAP in
accordance with:

* SCSCP specification: http://www.symbolic-computation.org/scscp

* OpenMath content dictionary scscp1:
  http://www.win.tue.nl/SCIEnce/cds/scscp1.html

* OpenMath content dictionary scscp2:
  http://www.win.tue.nl/SCIEnce/cds/scscp2.html

%prep
%setup -qn SCSCP-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
