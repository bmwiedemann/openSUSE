#
# spec file for package mcqd
#
# Copyright (c) 2020 SUSE LLC
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


Name:           mcqd
Version:        1.0.0
Release:        0
Summary:        Algorithm to find the maximum clique in a graph
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://insilab.org/maxclique/
Source:         https://gitlab.com/janezkonc/mcqd/-/archive/v%version/%name-v%version.tar.gz
BuildRequires:  gcc-c++

%description
MaxCliqueDyn is an exact algorithm for finding a maximum clique in an undirected graph.

%prep
%autosetup -p1 -n %name-v%version

%build
g++ %optflags -o mcqd mcqd.cpp

%install
b="%buildroot"
mkdir -p "$b/%_bindir"
cp -a mcqd "$b/%_bindir/"

%files
%_bindir/mcqd
%license COPYING

%changelog
