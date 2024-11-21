#
# spec file for package gap-example
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


Name:           gap-example
Version:        4.4.0
Release:        0
Summary:        GAP: A Demo for Package Authors
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/example
#Git-Clone:     https://github.com/gap-packages/example
Source:         https://github.com/gap-packages/example/releases/download/v%version/Example-%version.tar.gz
Source9:        %name-rpmlintrc
BuildRequires:  gap-devel >= 4.10
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.10
Requires:       gap-gapdoc >= 1.5

%description
The Example package, as its name suggests, is an example of how to
create a GAP package. It has little functionality except for being a
package, however, it contains an extensive appendix with guidelines
for package authors.

%prep
%autosetup -n Example-%version

%build
./configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
