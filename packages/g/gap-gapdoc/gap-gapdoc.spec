#
# spec file for package gap-gapdoc
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gap-gapdoc
Version:        1.6.6
Release:        0
Summary:        GAP: package for GAP Documentation
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.math.rwth-aachen.de/~Frank.Luebeck/GAPDoc/

Source:         http://www.math.rwth-aachen.de/~Frank.Luebeck/GAPDoc/GAPDoc-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11
Suggests:       gap-io >= 4.7

%description
This package contains a definition of a structure for GAP (package)
documentation, based on XML. It also contains conversion programs for
producing text, PDF or HTML versions of such documents, with
hyperlinks, if possible.

%prep
%setup -qn GAPDoc-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
