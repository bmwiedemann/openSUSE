#
# spec file for package python-soxr
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-soxr
Version:        0.3.4
Release:        0
Summary:        High quality, one-dimensional sample-rate conversion library
License:        LGPL-2.1-or-later
URL:            https://github.com/dofuuz/python-soxr
Source:         https://files.pythonhosted.org/packages/source/s/soxr/soxr-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.0~a7}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  soxr-devel >= 0.1.3
Requires:       python-numpy
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
High quality, one-dimensional sample-rate conversion library

%prep
%setup -q -n soxr-%{version}
# make sure we use the library from the system
rm -r libsoxr

%build
export CFLAGS="%{optflags}"
export PIP_CONFIG_SETTINGS="--global-option=--use-system-libsoxr"
%pyproject_wheel

%install
%pyproject_install
%{python_expand #
rm %{buildroot}%{$python_sitearch}/soxr/*.c
rm %{buildroot}%{$python_sitearch}/soxr/__init__.pxd
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license COPYING.LGPL LICENSE.txt
%{python_sitearch}/soxr
%{python_sitearch}/soxr-%{version}.dist-info

%changelog
