#
# spec file for package python-pikepdf
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2020-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           python-pikepdf
Version:        10.18.0
Release:        0
Summary:        Read and write PDFs with Python, powered by qpdf
License:        MPL-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/pikepdf/pikepdf
Source:         https://files.pythonhosted.org/packages/source/p/pikepdf/pikepdf-%{version}.tar.gz
## SECTION test requirements
BuildRequires:  %{python_module Pillow >= 10.0.1}
BuildRequires:  %{python_module devel >= 3.11}
BuildRequires:  %{python_module fonttools >= 4.40}
BuildRequires:  %{python_module hypothesis >= 6.36}
BuildRequires:  %{python_module jsonschema >= 4.18}
BuildRequires:  %{python_module lxml >= 4.8}
BuildRequires:  %{python_module nanobind-devel >= 3.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytest-cov >= 3.0.0}
BuildRequires:  %{python_module pytest-helpers-namespace >= 2019.1.8}
BuildRequires:  %{python_module pytest-timeout >= 2.1.0}
BuildRequires:  %{python_module pytest-xdist >= 2.5.0}
BuildRequires:  %{python_module python-dateutil >= 2.8.1}
BuildRequires:  %{python_module referencing}
BuildRequires:  %{python_module scikit-build-core >= 0.10}
BuildRequires:  %{python_module setuptools >= 80.9.0}
BuildRequires:  %{python_module tzdata}
BuildRequires:  %{python_module wheel >= 0.37}
BuildRequires:  timezone
## /SECTION
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjpeg8-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libqpdf) >= 12.4.2
Requires:       python-Pillow >= 10.0.1
Requires:       python-fonttools >= 4.40
Requires:       python-jsonschema >= 4.18
Requires:       python-lxml >= 4.8
Requires:       python-packaging
Requires:       python-referencing
%python_subpackages

%description
Read and write PDFs with Python, powered by qpdf.

%prep
%setup -q -n pikepdf-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/pikepdf*

%changelog
