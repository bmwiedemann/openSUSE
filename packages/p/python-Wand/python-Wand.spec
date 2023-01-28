#
# spec file for package python-Wand
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


Name:           python-Wand
Version:        0.6.11
Release:        0
Summary:        Ctypes-based simple MagickWand API binding for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/emcconville/wand
Source:         https://files.pythonhosted.org/packages/source/W/Wand/Wand-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
Requires:       ImageMagick
BuildRequires:  ImageMagick-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module psutil >= 1.0.1}
BuildRequires:  %{python_module pytest >= 7.2.0}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
# /SECTION
%python_subpackages

%description
Ctypes-based simple MagickWand API binding for Python.

%prep
%setup -q -n Wand-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Our ImageMagick is build without support of fftw library
# see identify -version and gh#emcconville/wand#476
export PYTEST_ADDOPTS="--skip-fft"
# Three tests failing with
# wand.exceptions.PolicyError: attempt to perform an operation not allowed by the security policy `PDF'
# due to https://build.opensuse.org/package/view_file/graphics/ImageMagick/ImageMagick-configuration-SUSE.patch
%pytest -rs -k 'not (test_resolution_set_03 or test_resolution_set_04 or test_read_with_colorspace or test_histogram)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/wand
%{python_sitelib}/Wand-%{version}*-info

%changelog
