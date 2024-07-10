#
# spec file for package gap-liealgdb
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


Name:           gap-liealgdb
Version:        2.2.1
Release:        0
Summary:        GAP: A database of Lie algebras
License:        GPL-2.0
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/liealgdb/
#Git-Clone:     https://github.com/gap-packages/liealgdb
Source:         https://github.com/gap-packages/liealgdb/releases/download/v%version/liealgdb-%version.tar.gz
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.8

%description
The package LieAlgDB provides access to several classifications of
Lie algebras. This package tries to make a few classifications of
small dimensional Lie algebras that have appeared in recent years
more accessible. For each classification that is contained in the
package, functions are provided that construct Lie algebras from that
classification inside GAP. This allows the user to obtain access to
the often rather complicated data contained in a classification, and
to directly interface the Lie algebras to the functionality for Lie
algebras which is already contained in GAP.

%prep
%autosetup -n liealgdb-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
