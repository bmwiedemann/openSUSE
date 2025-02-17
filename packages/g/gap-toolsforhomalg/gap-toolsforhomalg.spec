#
# spec file for package gap-toolsforhomalg
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


Name:           gap-toolsforhomalg
Version:        2024.09.01
%define sillyver 2024.09-01
Release:        0
Summary:        GAP: Special methods and knowledge propagation tools
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            http://homalg-project.github.io/homalg_project/ToolsForHomalg/
#Git-Clone:	https://github.com/homalg-project/ToolsForHomalg
Source:         https://github.com/homalg-project/homalg_project/releases/download/ToolsForHomalg-%sillyver/ToolsForHomalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12.1

%description
The ToolsForHomalg package provides GAP extensions for the homalg
project.

%prep
%autosetup -n ToolsForHomalg-%sillyver

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
