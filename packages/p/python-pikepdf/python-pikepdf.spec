#
# spec file for package python-pikepdf
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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
%define skip_python2 1
Name:           python-pikepdf
Version:        6.2.7
Release:        0
Summary:        Read and write PDFs with Python, powered by qpdf
License:        MPL-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/pikepdf/pikepdf
Source:         https://files.pythonhosted.org/packages/source/p/pikepdf/pikepdf-%{version}.tar.gz
## SECTION test requirements
BuildRequires:  %{python_module Pillow >= 9.0.0}
BuildRequires:  %{python_module attrs >= 20.2.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis >= 5.0}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module lxml >= 4.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module psutil >= 5}
BuildRequires:  %{python_module pybind11 >= 2.10.0}
BuildRequires:  %{python_module pybind11-devel >= 2.10.0}
BuildRequires:  %{python_module pytest >= 6.0.0}
BuildRequires:  %{python_module pytest-cov >= 2.10.1}
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module pytest-helpers-namespace >= 2019.1.8}
# Upstream use pytest-timeout >= 1.4.2
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist >= 1.28}
BuildRequires:  %{python_module python-dateutil >= 2.8.0}
#BuildRequires:  %%{python_module python-xmp-toolkit >= 2.0.1}
BuildRequires:  %{python_module setuptools >= 50}
BuildRequires:  %{python_module setuptools_scm >= 4.1}
BuildRequires:  %{python_module setuptools_scm_git_archive}
#BuildRequires:  %%{python_module wheel >= 0.35}
## /SECTION
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libqpdf) >= 11.1.1
Requires:       python-Pillow >= 9.0.0
Requires:       python-lxml >= 4.0
Requires:       python-packaging
%python_subpackages

%description
Read and write PDFs with Python, powered by qpdf.

%prep
%setup -q -n pikepdf-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE.txt
%doc README.md docs/*/*.rst
%{python_sitearch}/pikepdf/
%{python_sitearch}/pikepdf-%{version}-py%{python_version}.egg-info/

%changelog
