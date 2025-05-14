#
# spec file for package python-pylineclip
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


Name:           python-pylineclip
Version:        1.0.0
Release:        0
Summary:        Line clipping tool
License:        MIT
URL:            https://github.com/scivision/lineclipping-python-fortran
Source:         https://github.com/scivision/lineclipping-python-fortran/archive/v%{version}.tar.gz#/lineclipping-python-fortran-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 38.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Line clipping: Cohen-Sutherland

%prep
%setup -q -n lineclipping-python-fortran-%{version}
sed -i -e '/^#!\//, 1d' pylineclip/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
mkdir demo-%{$python_bin_suffix}
sed -e '1 {s|^#!.*$|#!%{_bindir}/$python|}' DemoLineclip.py > demo-%{$python_bin_suffix}/DemoLineclip.py
%fdupes %{buildroot}%{$python_sitelib}
}
rm %{buildroot}%{_bindir}/DemoLineclip.py

%check
%pytest

%files %{python_files}
%doc README.md demo-%{python_bin_suffix}/DemoLineclip.py
%license LICENSE.txt
%{python_sitelib}/pylineclip
%{python_sitelib}/pylineclip-%{version}.dist-info

%changelog
