#
# spec file for package ViTables
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


%define pythons python3

Name:           ViTables
Version:        3.0.3
Release:        0
Summary:        A viewer package for PyTables
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Other
URL:            https://github.com/uvemas/ViTables
Source0:        https://github.com/uvemas/ViTables/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-QtPy
BuildRequires:  python3-hatchling
BuildRequires:  python3-numpy
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-qt5
BuildRequires:  python3-tables
Requires:       hdf5
Requires:       hicolor-icon-theme
Requires:       python3-QtPy
Requires:       python3-blosc2
Requires:       python3-numpy
Requires:       python3-qt5
Requires:       python3-tables
Provides:       ViTables2 = %{version}
Obsoletes:      ViTables2 < %{version}
BuildArch:      noarch

%description
ViTables is a graphical tool for browsing and editing files in both
PyTables and HDF5 format. With ViTables you can easily navigate
through the data hierarchy, view and modify metadata, view actual data
and more.

%prep
%setup -q -n ViTables-%{version}
find -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} \;

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

for p in 16 22 32 48 64 128; do
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${p}x${p}/apps/
install -m 644 -D vitables/icons/unixapp/vitables_${p}x${p}.png %{buildroot}%{_datadir}/icons/hicolor/${p}x${p}/apps/vitables.png
done
install -m 644 -D vitables/icons/unixapp/vitables.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/vitables.svg

%check
export QT_QPA_PLATFORM=offscreen
%pytest

%files
%doc ANNOUNCE.txt ChangeLog.txt README.md
%license LICENSE.txt
%{_bindir}/vitables
%{python3_sitelib}
%{_datadir}/icons/hicolor/*/apps/vitables.*

%changelog
