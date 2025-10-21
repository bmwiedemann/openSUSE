#
# spec file for package gap-autodoc
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gap-autodoc
Version:        2025.10.16
Release:        0
Summary:        GAP: Tools for generating automatic GAPDoc documentations
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            http://gap-packages.github.io/AutoDoc/
Source:         https://github.com/gap-packages/AutoDoc/releases/download/v%version/AutoDoc-%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
BuildRequires:  xz
BuildArch:      noarch
Requires:       gap-core >= 4.5
Requires:       gap-gapdoc >= 1.6.3

%description
This package is supposed to help creating documentations for GAP
packages. It makes it possible to create documentation without
writing .xml. It is not in any way a substitution for GAPDoc, but
needs it to compile its output.

%prep
%autosetup -n AutoDoc-%version

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
