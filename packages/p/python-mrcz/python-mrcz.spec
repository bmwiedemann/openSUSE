#
# spec file for package python-mrcz
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


%{?sle15_python_module_pythons}
Name:           python-mrcz
Version:        0.5.9
Release:        0
Summary:        MRCZ meta-compressed image file-format library
License:        BSD-3-Clause
URL:            https://github.com/em-MRCZ/python-mrcz
Source0:        https://files.pythonhosted.org/packages/source/m/mrcz/mrcz-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/em-MRCZ/python-mrcz/pull/15 Numpy 2.0 and deprecation fixes
Patch:          numpy2.patch
# PATCH-FIX-UPSTREAM https://github.com/em-MRCZ/python-mrcz/pull/16 Remove distutils / support python >=3.12
Patch:          new-pythons.patch
BuildRequires:  %{python_module blosc >= 1.4}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module numpy >= 1.8}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.8
Recommends:     python-blosc >= 1.4
BuildArch:      noarch
%python_subpackages

%description
mrcz is a package designed to supplement the venerable MRC image file
format with a highly efficient compressed variant, using the blosc
meta-compressor library to shrink files on disk and greatly accelerate
file input/output for the era of "Big Data" in electron and optical
microscopy.

%prep
%setup -n mrcz-%{version}
dos2unix mrcz/ReliablePy.py mrcz/ioMRC.py mrcz/test_mrcz.py utils/update_mrcz_to_0.5.0.py
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.txt README.rst
%license LICENSE.txt
%{python_sitelib}/mrcz
%{python_sitelib}/mrcz-%{version}.dist-info

%changelog
