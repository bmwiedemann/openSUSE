#
# spec file for package python-pikepdf
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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
Version:        1.17.3
Release:        0
Summary:        Read and write PDFs with Python, powered by qpdf
License:        MPL-2.0
URL:            https://github.com/pikepdf/pikepdf
Source:         https://files.pythonhosted.org/packages/source/p/pikepdf/pikepdf-%{version}.tar.gz
## SECTION test requirements
BuildRequires:  %{python_module Pillow >= 5.0.0}
BuildRequires:  %{python_module attrs >= 19.1.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis >= 4.24}
BuildRequires:  %{python_module lxml >= 4.0}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pybind11 >= 2.4.3}
BuildRequires:  %{python_module pybind11-devel >= 2.4.3}
BuildRequires:  %{python_module pytest >= 4.4.0}
BuildRequires:  %{python_module pytest-helpers-namespace >= 2019.1.8}
BuildRequires:  %{python_module pytest-timeout >= 1.3.3}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module setuptools_scm_git_archive}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
## /SECTION
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libqpdf)
Requires:       python-Pillow >= 5.0.0
Requires:       python-lxml >= 4.0
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
%license LICENSE.txt licenses
%doc README.md
%{python_sitearch}/pikepdf*

%changelog
