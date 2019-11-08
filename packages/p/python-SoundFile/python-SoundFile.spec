#
# spec file for package python-SoundFile
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
%define         oldpython python
Name:           python-SoundFile
Version:        0.10.2
Release:        0
Summary:        An audio library based on libsndfile, CFFI and NumPy
License:        BSD-3-Clause
URL:            https://github.com/bastibe/PySoundFile
Source:         https://files.pythonhosted.org/packages/source/S/SoundFile/SoundFile-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 0.6}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libsndfile1
BuildRequires:  python-rpm-macros
Requires:       libsndfile1
Requires:       python-cffi >= 0.6
Recommends:     python-numpy
Obsoletes:      python-PySoundFile < %{version}
Provides:       python-PySoundFile = %{version}
%ifpython2
Obsoletes:      %{oldpython}-PySoundFile < %{version}
Provides:       %{oldpython}-PySoundFile = %{version}
%endif
%python_subpackages

%description
PySoundFile is an audio library based on libsndfile, CFFI and NumPy.
Full documentation is available on http://pysoundfile.readthedocs.org/.

PySoundFile can read and write sound files. File reading/writing is
supported through libsndfile, which itself is accessed through CFFI,
a foreign function interface for Python calling C code. PySoundFile
represents audio data as NumPy arrays.

%prep
%setup -q -n SoundFile-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test --pytest-args="-knot\ read_int_data_from_float_file"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
