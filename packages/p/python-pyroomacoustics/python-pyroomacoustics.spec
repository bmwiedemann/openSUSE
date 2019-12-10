#
# spec file for package python-pyroomacoustics
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pyroomacoustics
Version:        0.3.1
Release:        0
Summary:        A framework for room acoustics and audio processing in Python
License:        MIT
URL:            https://github.com/LCAV/pyroomacoustics
Source:         https://github.com/LCAV/pyroomacoustics/archive/v%{version}.tar.gz#/pyroomacoustics-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Cython
Requires:       python-numpy
Requires:       python-scipy >= 0.18.0
# SECTION test requirements
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy >= 0.18.0}
# /SECTION
%python_subpackages

%description
Pyroomacoustics is a package for audio signal processing for indoor
applications. It was developed as a prototyping platform for
beamforming algorithms in indoor scenarios.

%prep
%setup -q -n pyroomacoustics-%{version}
chmod a-x README.rst

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv pyroomacoustics pyroomacoustics_temp
rm -rf build _build.*
%{python_expand rm -rf build _build.*
export PYTHONPATH=%{buildroot}%{$python_sitearch}
nosetests-%{$python_bin_suffix} --no-byte-compile pyroomacoustics_temp/tests/
}
mv pyroomacoustics_temp pyroomacoustics

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
