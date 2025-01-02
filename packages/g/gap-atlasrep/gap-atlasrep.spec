#
# spec file for package gap-atlasrep
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


Name:           gap-atlasrep
Version:        2.1.9
Release:        0
Summary:        GAP: Interface to the Atlas of Group Representations
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.math.rwth-aachen.de/homes/Thomas.Breuer/atlasrep
Source:         https://www.math.rwth-aachen.de/homes/Thomas.Breuer/atlasrep/atlasrep-%version.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11.0
Requires:       gap-gapdoc >= 1.6.2
Requires:       gap-utils >= 0.77
Suggests:       gap-browse >= 1.8.3
Suggests:       gap-ctbllib >= 1.2
Suggests:       gap-ctblocks >= 1.0
Suggests:       gap-io >= 3.3
Suggests:       gap-mfer >= 1.0
Suggests:       gap-recog >= 1.3.1
Suggests:       gap-standardff >= 0.9
Suggests:       gap-tomlib >= 1.0
# changelog in chap1.html

%description
AtlasRep provides an interface between GAP and the Atlas of Group
Representations, a database that comprises representations of many
almost simple groups and information about their maximal subgroups.

%prep
%autosetup -n atlasrep-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
