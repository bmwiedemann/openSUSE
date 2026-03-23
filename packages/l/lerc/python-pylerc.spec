#
# spec file for package python-pylerc
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

%define  sover  4
%define  lname  libLerc
%define  cversion 4.1.0
Name:           python-pylerc
Version:        4.1
Release:        0
Summary:        Python Bindings for LERC: Limited Error Raster Compression
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/Esri/lerc
Source0:        lerc-%{cversion}.tar.gz
# PATCH-FEATURE-OPENSUSE: Use the system library instead of copying to the python sitelib
Patch0:         pylerc-use-syslib.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  lerc-devel
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module numpy >= 2.3.0}
Requires:       python-numpy >= 2.3.0
Requires:       %{lname}%{sover} = %{cversion}-%{release}
BuildArch:      noarch
%python_subpackages


%description
LERC is an open-source image or raster format which supports rapid encoding
and decoding for any pixel type (not just RGB or Byte). Users set the
maximum compression error per pixel while encoding, so the precision of the
original input image is preserved (within user defined error bounds).

This package provides the Python bindings for LERC.

%prep
%autosetup -p1 -n lerc-%{cversion}
dos2unix -v -o NOTICE

%build
cd OtherLanguages/Python
%pyproject_wheel

%install
cd OtherLanguages/Python
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}/lerc}

%check
%{python_expand # Test python bindings
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{python_sitelib}
$python -c "import lerc; lerc.test()"
}

%files %{python_files}
%doc OtherLanguages/Python/lerc/README.md
%license LICENSE NOTICE
%{python_sitelib}/lerc
%{python_sitelib}/pylerc-%{version}.dist-info

%changelog
