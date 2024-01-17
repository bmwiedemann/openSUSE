#
# spec file for package python-pyroomacoustics
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


# NEP 29: NumPy dropped Python 3.6
%define skip_python36 1
Name:           python-pyroomacoustics
Version:        0.7.3
Release:        0
Summary:        A framework for room acoustics and audio processing in Python
License:        MIT
URL:            https://github.com/LCAV/pyroomacoustics
Source:         https://github.com/LCAV/pyroomacoustics/archive/v%{version}.tar.gz#/pyroomacoustics-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pybind11-devel >= 2.2}
BuildRequires:  %{python_module samplerate}
BuildRequires:  %{python_module scipy >= 0.18.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sounddevice}
BuildRequires:  c++_compiler
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Cython
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-pybind11 >= 2.2
Requires:       python-samplerate
Requires:       python-scipy >= 0.18.0
Requires:       python-sounddevice
# SECTION test requirements
BuildRequires:  %{python_module pytest}
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
# First build the extension with custom include path:
# Use eigen3 headers from system instead of from the empty submodule dir in the github archive.
%python_exec setup.py build_ext -I %{_includedir}/eigen3
# Then build everything
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Only test on x86_64: All other platforms fail because of rounding errors vs.
# too tight precision requirements in tests.
%ifarch x86_64
%pytest_arch pyroomacoustics/tests --import-mode=append
%endif

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pyroomacoustics
%{python_sitearch}/pyroomacoustics-%{version}*-info

%changelog
