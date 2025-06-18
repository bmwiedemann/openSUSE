#
# spec file for package ubi_reader
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2018-2025, Martin Hauke <mardnh@gmx.de>
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


%define pythons python3
Name:           ubi_reader
Version:        0.8.12
Release:        0
Summary:        Extract files from UBI and UBIFS images
License:        LGPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/onekey-sec/ubi_reader
Source:         https://github.com/onekey-sec/ubi_reader/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
Collection of Python scripts for reading information about and extracting
data from UBI and UBIFS images.

The following tools are included:
 - ubireader_display_info:
   Show information about UBI or UBIFS image.
 - ubireader_extract_files:
   Extract contents of a UBI or UBIFS image.
 - ubireader_extract_images:
   Extract UBI or UBIFS images from file containing UBI data in it.
 - ubireader_list_files:
   List and Extract files of a UBI or UBIFS image.
 - ubireader_utils_info:
   Determine settings for recreating UBI image.

%prep
%autosetup -n ubi_reader-%{version}
chmod -x README.md
find ubireader -name "*.py" | xargs sed -i -e '/^#!\//, 1d'

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE
%doc README.md
%{_bindir}/ubireader_display_blocks
%{_bindir}/ubireader_display_info
%{_bindir}/ubireader_extract_files
%{_bindir}/ubireader_extract_images
%{_bindir}/ubireader_utils_info
%{_bindir}/ubireader_list_files
%{python3_sitelib}/ubi*

%changelog
