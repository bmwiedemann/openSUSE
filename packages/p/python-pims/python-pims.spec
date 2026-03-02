#
# spec file for package python-PIMS
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-pims
Version:        0.7
Release:        0
Summary:        Python Image Sequence
License:        BSD-3-Clause
URL:            https://github.com/soft-matter/pims
# PyPi tarball does not contain test data
Source:         https://github.com/soft-matter/pims/archive/refs/tags/v%{version}.tar.gz#/pims-%{version}.tar.gz
Patch0:         support-pillow-12.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module imageio}
BuildRequires:  %{python_module numpy >= 1.19}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module slicerator >= 0.9.8}
BuildRequires:  %{python_module tifffile}
# /SECTION
BuildRequires:  fdupes
Requires:       python-imageio
Requires:       python-numpy >= 1.19
Requires:       python-packaging
Requires:       python-slicerator >= 0.9.8
Requires:       python-tifffile
BuildArch:      noarch
%python_subpackages

%description
Python Image Sequence

%prep
%autosetup -p1 -n pims-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# numpy 2.4 fallout
%pytest -k 'not (TestSpeStack and test_metadata)'

%files %{python_files}
%doc README.md
%license license.txt
%{python_sitelib}/pims
%{python_sitelib}/[Pp][Ii][Mm][Ss]-%{version}.dist-info

%changelog
