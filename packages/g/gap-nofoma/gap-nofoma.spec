#
# spec file for package gap-localnr
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gap-nofoma
Version:        1.0.1
Release:        0
Summary:        GAP: Frobenius normal form
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/nofoma/
#Git-Clone:     https://github.com/gap-packages/nofoma
Source:         https://github.com/gap-packages/nofoma/releases/download/v%version/nofoma-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10
Requires:       gap-sonata >= 2.4

%description
This package computes the Frobenius normal form and the
Jordan—Chevalley decomposition of a (square) matrix over any field
that is available in GAP. It also computes the Jordan normal form of
matrices over finite fields.

%prep
%autosetup -n nofoma-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
