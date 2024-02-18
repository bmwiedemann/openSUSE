#
# spec file for package python-samplerate
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


Name:           python-samplerate
Version:        0.2.1
Release:        0
License:        MIT
Summary:        Python bindings for libsamplerate
URL:            https://github.com/tuxu/python-samplerate
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/s/samplerate/samplerate-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libsamplerate-devel >= 0.2.2
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-numpy

%python_subpackages

%description
This is a wrapper around Erik de Castro Lopo's libsamplerate (aka Secret
Rabbit Code) for sample rate conversion.

It implements all three APIs available in libsamplerate:

* Simple API: for resampling a large chunk of data with a single library
  call
* Full API: for obtaining the resampled signal from successive chunks of
  data
* Callback API: like Full API, but input samples are provided by a callback
  function

%prep
%autosetup -p1 -n samplerate-%{version}
# debundle pybind11 and libsamplerate
# https://pybind11.readthedocs.io/en/stable/compiling.html#find-package-vs-add-subdirectory
rm -r external
sed -i 's/add_subdirectory(external)/find_package(pybind11 REQUIRED)/' CMakeLists.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitearch}/samplerate.*.so
%{python_sitearch}/samplerate-%{version}.dist-info

%changelog
