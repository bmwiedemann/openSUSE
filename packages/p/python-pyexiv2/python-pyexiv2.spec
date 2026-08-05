#
# spec file for package python-pyexiv2
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         modname pyexiv2
%{?sle15_python_module_pythons}
Name:           python-pyexiv2
Version:        2.15.5
Release:        0
Summary:        A Python library for reading and writing image metadata
License:        GPL-3.0-only
URL:            https://github.com/LeoHsiao1/pyexiv2
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(exiv2)
BuildArch:      noarch
%python_subpackages

%description
A Python library for reading and writing image metadata, including EXIF, IPTC, XMP, ICC Profile.

%prep
%autosetup -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#remove unnecessary files
%python_expand rm %{buildroot}%{$python_sitelib}/%{modname}/lib/exiv2api.cpp
%python_expand rm -r %{buildroot}%{$python_sitelib}/%{modname}/tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info

%changelog
