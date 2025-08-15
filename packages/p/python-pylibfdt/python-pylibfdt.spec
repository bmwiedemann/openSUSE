#
# spec file for package python-pylibfdt
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-pylibfdt
Version:        1.7.2.post1
Release:        0
Summary:        Python binding for libfdt
License:        BSD-2-Clause AND GPL-2.0-only
URL:            https://pypi.org/project/pylibfdt/
Source:         https://files.pythonhosted.org/packages/source/p/pylibfdt/pylibfdt-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  swig
%python_subpackages

%description
libfdt is a library to process Open Firmware style device trees on various
architectures.

Python binding part.

%prep
%setup -q -n pylibfdt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license BSD-2-Clause GPL
%{python_sitearch}/libfdt.py
%{python_sitearch}/_libfdt.*.so
%{python_sitearch}/__pycache__
%{python_sitearch}/pylibfdt-%{version}.dist-info

%changelog
