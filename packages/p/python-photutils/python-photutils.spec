#
# spec file for package python-photutils
#
# Copyright (c) 2024 SUSE LLC
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


%define shortversion 1.12
Name:           python-photutils
Version:        1.12.0
Release:        0
Summary:        An Astropy package for photometry
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/astropy/photutils
Source:         https://files.pythonhosted.org/packages/source/p/photutils/photutils-%{shortversion}.tar.gz
BuildRequires:  %{python_module Cython >= 3 with %python-Cython < 3.1}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module extension-helpers >= 1 with %python-extension-helpers < 2}
BuildRequires:  %{python_module numpy-devel >= 1.25}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astropy >= 5.1
Requires:       python-numpy >= 1.25
Recommends:     python-Bottleneck
Recommends:     python-Shapely
Recommends:     python-gwcs >= 0.18
Recommends:     python-matplotlib >= 3.5
Recommends:     python-rasterio
Recommends:     python-scikit-image >= 0.19.0
Recommends:     python-scikit-learn >= 1.0
Recommends:     python-scipy >= 1.7.2
Recommends:     python-tqdm
# SECTION test requirements
BuildRequires:  %{python_module Bottleneck}
BuildRequires:  %{python_module astropy >= 5.1}
BuildRequires:  %{python_module gwcs >= 0.18}
BuildRequires:  %{python_module matplotlib >= 3.5}
BuildRequires:  %{python_module pytest-astropy >= 0.10}
BuildRequires:  %{python_module scikit-image >= 0.19.0}
BuildRequires:  %{python_module scikit-learn >= 1.0}
BuildRequires:  %{python_module scipy >= 1.7.2}
# /SECTION
%python_subpackages

%description
Photutils is an affiliated package of Astropy to provide tools for detecting
and performing photometry of astronomical sources.

%prep
%autosetup -p1 -n photutils-%{shortversion}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# do not import source dir without extensions
cd ..
# Use astropy test suite logic. Calling pytest directly would require
# duplicate in-place building of extensions.
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH="%{buildroot}%{$python_sitearch}"
$python -B -c "import photutils, sys; sys.exit(photutils.test(args=\"-v -rsfEx\"))"
}

%files %{python_files}
%doc CHANGES.rst photutils/CITATION.rst README.rst
%license LICENSE.rst
%{python_sitearch}/photutils
%{python_sitearch}/photutils-%{version}.dist-info

%changelog
