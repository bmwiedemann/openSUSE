#
# spec file for package python-SoundFile
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?sle15_python_module_pythons}
Name:           python-SoundFile
Version:        0.13.1
Release:        0
Summary:        An audio library based on libsndfile, CFFI and NumPy
License:        BSD-3-Clause
URL:            https://github.com/bastibe/python-soundfile
Source:         https://files.pythonhosted.org/packages/source/s/soundfile/soundfile-%{version}.tar.gz
Source99:       python-SoundFile.rpmlintrc
# PATCH-FIX-OPENSUSE 0001-Fix-libsndfile-versioning.patch gyee@suse.com -- strip optional -exp suffix from libsndfile version string
Patch0:         0001-Fix-libsndfile-versioning.patch
BuildRequires:  %{python_module cffi >= 1.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(sndfile)
# dlopen()s libsndfile via cffi ABI mode (not linked)
Requires:       libsndfile1
Requires:       python-cffi >= 1.0
Requires:       python-numpy
Obsoletes:      python-PySoundFile < %{version}
Provides:       python-PySoundFile = %{version}
Provides:       python-soundfile = %{version}
BuildArch:      noarch
%python_subpackages

%description
PySoundFile is an audio library based on libsndfile, CFFI and NumPy.
Full documentation is available on https://python-soundfile.readthedocs.io/.

PySoundFile can read and write sound files. File reading/writing is
supported through libsndfile, which itself is accessed through CFFI,
a foreign function interface for Python calling C code. PySoundFile
represents audio data as NumPy arrays.

%prep
%autosetup -p1 -n soundfile-%{version}

%build
# force a pure wheel through unknown platform
# (we do not bundle the libs anyway)
export PYSOUNDFILE_PLATFORM="OBS"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# openSUSE libsndfile is built without MPEG/MP3 (no mpg123/lame) on all
# current products. Skip the MP3 compression test rather than probing
# available_formats() at runtime, which would hide a later MPEG enablement.
%pytest -k 'not test_write_mp3_compression'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/soundfile-%{version}.dist-info
%{python_sitelib}/soundfile.py
%{python_sitelib}/_soundfile.py
%pycache_only %{python_sitelib}/__pycache__/soundfile*.pyc
%pycache_only %{python_sitelib}/__pycache__/_soundfile*.pyc

%changelog
