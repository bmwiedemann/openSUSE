#
# spec file for package gap-browse
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gap-browse
Version:        1.8.21
Release:        0
Summary:        GAP: ncurses interface and browsing applications
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.math.rwth-aachen.de/homes/Browse/
Source:         https://www.math.rwth-aachen.de/homes/Browse/Browse-%version.tar.bz2
BuildRequires:  gap-devel >= 4.12
BuildRequires:  gap-rpm-devel >= 4.12
BuildRequires:  gmp-devel
BuildRequires:  ncurses-devel
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.6
Suggests:       gap-atlasrep >= 2.0
Suggests:       gap-io >= 2.2

%description
The Browse package provides three levels of functionality

* A GAP interface to the ncurses library.
* A generic function for interactive browsing through two-dimensional
  arrays of data.
* Several applications of the first two, e.g., a method for browsing
  character tables, browsing through the content of some data
  collections, or some games.

%prep
%autosetup -n Browse-%version

%build
./configure "%gapdir"
# Browse must be compiled with ncurses-5 or -w5. Crashes with ncurses-6.
make %{?_smp_mflags} \
	CFLAGS="%optflags -DWIDECHARS $(ncursesw5-config --cflags)" \
	LOPTS="$(ncursesw5-config --libs) -lpanelw"

%install
%gappkg_simple_install
pushd "%buildroot/$moddir/"
rm -Rf Makefile configure src
popd

%files -f %name.files

%changelog
