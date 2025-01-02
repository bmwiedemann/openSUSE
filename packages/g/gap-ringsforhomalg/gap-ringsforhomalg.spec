#
# spec file for package gap-ringsforhomalg
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


Name:           gap-ringsforhomalg
Version:        2024.11.02
%define sillyver 2024.11-02
Release:        0
Summary:        GAP: Dictionaries of External Rings
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://github.com/homalg-project/homalg_project/tree/master/RingsForHomalg#readme
Source:         https://github.com/homalg-project/homalg_project/releases/download/RingsForHomalg-%sillyver/RingsForHomalg-%sillyver.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.12.1
Requires:       gap-gapdoc >= 1.0
Requires:       gap-gaussforhomalg >= 2023.08.01
Requires:       gap-homalgtocas >= 2023.08.01
Requires:       gap-matricesforhomalg >= 2024.11.02

%description
The RingsForHomalg package provides small dictionaries for homalg to
speak (as much as needed of) the languages of Singular, Macaulay2,
MAGMA, Sage, and Maple.

%prep
%autosetup -n RingsForHomalg-%sillyver

%build

%install
%gappkg_simple_install
%fdupes %buildroot/%_prefix

%files -f %name.files

%changelog
