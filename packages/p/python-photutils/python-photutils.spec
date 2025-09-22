#
# spec file for package python-photutils
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


Name:           python-photutils
Version:        2.3.0
Release:        0
Summary:        An Astropy package for photometry
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/astropy/photutils
Source:         https://files.pythonhosted.org/packages/source/p/photutils/photutils-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.1 with %python-Cython < 4}
BuildRequires:  %{python_module devel >= 3.11}
BuildRequires:  %{python_module extension-helpers >= 1.3}
BuildRequires:  %{python_module numpy-devel >= 1.25}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy >= 5.3
Requires:       python-numpy >= 1.25
Requires:       python-scipy >= 1.11.1
Recommends:     python-Bottleneck >= 1.3.6
Recommends:     python-Shapely >= 2
Recommends:     python-gwcs >= 0.20
Recommends:     python-matplotlib >= 3.8
Recommends:     python-rasterio >= 1.3.7
Recommends:     python-scikit-image >= 0.21.0
Recommends:     python-tqdm >= 4.65
# SECTION test requirements
BuildRequires:  %{python_module Bottleneck >= 1.3.6}
BuildRequires:  %{python_module astropy >= 5.3}
BuildRequires:  %{python_module gwcs >= 0.20}
BuildRequires:  %{python_module matplotlib >= 3.8}
BuildRequires:  %{python_module pytest-astropy >= 0.10}
BuildRequires:  %{python_module pytest-xdist >= 2.5}
BuildRequires:  %{python_module scikit-image >= 0.21.0}
BuildRequires:  %{python_module scipy >= 1.11.1}
# /SECTION
%python_subpackages

%description
Photutils is an affiliated package of Astropy to provide tools for detecting
and performing photometry of astronomical sources.

%prep
%autosetup -p1 -n photutils-%{version}
sed -i "/'--color=yes',/d" pyproject.toml

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv photutils photutils.src
%pytest_arch -n auto --pyargs photutils -rsxfE
mv photutils.src photutils

%files %{python_files}
%doc CHANGES.rst photutils/CITATION.rst README.rst
%license LICENSE.rst
%{python_sitearch}/photutils
%{python_sitearch}/photutils-%{version}.dist-info

%changelog
