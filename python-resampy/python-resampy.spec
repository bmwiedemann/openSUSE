#
# spec file for package python-resampy
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-resampy
Version:        0.2.1
Release:        0
Summary:        Signal resampling in Python
License:        ISC
Group:          Development/Languages/Python
Url:            https://github.com/bmcfee/resampy
Source:         https://files.pythonhosted.org/packages/source/r/resampy/resampy-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numba >= 0.32}
BuildRequires:  %{python_module numpy >= 1.10}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.13}
BuildRequires:  %{python_module six >= 1.3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numba >= 0.32
Requires:       python-numpy >= 1.10
Requires:       python-scipy >= 0.13
Requires:       python-six >= 1.3
Suggests:       python-sphinx
Suggests:       python-numpydoc
BuildArch:      noarch

%python_subpackages

%description
This package implements the band-limited sinc interpolation method
in Python for sampling rate conversion as described by:

Smith, Julius O. Digital Audio Resampling Home Page Center for
Computer Research in Music and Acoustics (CCRMA), Stanford
University, 2015-02-23. Web published at
http://ccrma.stanford.edu/~jos/resample/.

%prep
%setup -q -n resampy-%{version}
# Remove shebang from files
sed -i -e '/^#!\//, 1d' */*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
