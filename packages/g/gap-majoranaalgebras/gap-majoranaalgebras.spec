#
# spec file for package gap-majoranaalgebras
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


Name:           gap-majoranaalgebras
Version:        1.5.1
Release:        0
Summary:        GAP: Majorana algebra and representation construction
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/MajoranaAlgebras/
#Git-Clone:	https://github.com/gap-packages/MajoranaAlgebras
Source:         https://github.com/gap-packages/MajoranaAlgebras/releases/download/v%version/MajoranaAlgebras-%version.tar.gz
BuildRequires:  gap-rpm-devel
Requires:       gap-automata >= 1.13
Requires:       gap-core >= 4.8
Requires:       gap-datastructures >= 0.2.2
Requires:       gap-gapdoc >= 1.5
Requires:       gap-gauss
Suggests:       gap-char0gauss

%description
MajoranaAlgebras is a package for constructing Majorana
representations of finite groups. It also offers some functions to
calculate with a constructed Majorana representation. The main
constructive functions use the algorithm described in the preprint
Constructing Majorana Representations [arxiv.org/abs/1803.10723] by
Markus Pfeiffer and Madeleine Whybrow.

%prep
%autosetup -n MajoranaAlgebras-%version

%build
find . -type f -size 0 -name _Chunks.xml -delete

%install
%gappkg_simple_install

%files -f %name.files

%changelog
