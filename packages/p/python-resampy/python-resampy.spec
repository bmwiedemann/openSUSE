#
# spec file for package python-resampy
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%else
%bcond_without test
%define psuffix -%{flavor}
%endif

Name:           python-resampy%{psuffix}
Version:        0.4.3
Release:        0
Summary:        Signal resampling in Python
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/bmcfee/resampy
# The GitHub archive includes the tests
Source:         https://github.com/bmcfee/resampy/archive/refs/tags/%{version}.tar.gz#/resampy-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numba >= 0.53
Requires:       python-numpy >= 1.17
Suggests:       python-numpydoc
Suggests:       python-sphinx
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module resampy = %{version}}
BuildRequires:  %{python_module scipy >= 1.1}
%endif
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
# Remove code coverage options
sed -i '/addopts/d' setup.cfg

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/resampy
%{python_sitelib}/resampy-%{version}.dist-info
%endif

%changelog
