#
# spec file for package gap-io_forhomalg
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


Name:           gap-io_forhomalg
Version:        2023.02.04
%define sillyver 2023.02-04
Release:        0
Summary:        GAP: IO Capabilities for the homalg Project
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://homalg-project.github.io/pkg/IO_ForHomalg
#Git-Clone:	https://github.com/homalg-project/homalg_project
Source:         https://github.com/homalg-project/homalg_project/releases/download/IO_ForHomalg-%sillyver/IO_ForHomalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12.1
Requires:       gap-homalgtocas >= 2009.06.18
Requires:       gap-io >= 2.3
Suggests:       gap-gapdoc >= 1.0

%description
The IO_ForHomalg package launches the command-line-interface of an
external computer algebra system and connects it to homalg using an
Input/Output stream.

%prep
%autosetup -n IO_ForHomalg-%sillyver

%build
find . -type f -name .gitkeep -delete
rm -v doc/clean

%install
%gappkg_simple_install

%files -f %name.files

%changelog
