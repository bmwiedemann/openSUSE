#
# spec file for package python-pydicom
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         oldpython python
Name:           python-pydicom
Version:        1.3.0
Release:        0
Summary:        Pure python package for DICOM medical file reading and writing
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/darcymason/pydicom
Source:         https://files.pythonhosted.org/packages/source/p/pydicom/pydicom-%{version}.tar.gz
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-dicom < %{version}
Provides:       %{oldpython}-dicom = %{version}
%endif
%python_subpackages

%description
pydicom is a pure python package for parsing DICOM files
into natural pythonic structures for further manipulation.
Modified datasets can be written again to DICOM format files.

DICOM is a standard (http://medical.nema.org) for communicating
medical images and related information such as reports
and radiotherapy objects.

%prep
%setup -q -n pydicom-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest pydicom/tests

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
