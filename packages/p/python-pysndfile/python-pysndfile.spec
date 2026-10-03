#
# spec file for package python-pysndfile
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-pysndfile
Version:        1.5.3
Release:        0
Summary:        Cython wrapper class for reading/writing soundfiles
License:        LGPL-3.0-only
URL:            https://forge-2.ircam.fr/roebel/pysndfile
Source:         https://forge-2.ircam.fr/roebel/pysndfile/-/archive/Version_%{version}/pysndfile-Version_%{version}.tar.gz#/pysndfile-%{version}.tar.gz
Patch0:         fix-test-imports.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel
BuildRequires:  python-rpm-macros
Requires:       python-numpy
%python_subpackages

%description
pysndfile is a python package providing PySndfile a Cython wrapper class around
libsndfile. PySndfile provides methods for reading and writing a large variety
of soundfile formats on a variety of platforms. PySndfile provides a rather
complete access to the different sound file manipulation options that are
available in libsndfile.

Due to the use of libsndfile nearly all sound file formats can be read and
written with PySndfile.

The interface has been designed such that a rather large subset of the
functionality of libsndfile can be used, notably the reading and writing
of strings into soundfile formats that support these, and a number of
sf\_commands that allow to control the way libsndfile reads and writes
the samples. One of the most important ones is the use of the clipping
command.

%prep
%autosetup -p1 -n pysndfile-Version_%{version}
# Only /usr/lib is checked for the library
cat >>setup.cfg.dist <<EOF
sndfile_libdir = %{_libdir}
sndfile_incdir = %{_includedir}
EOF
mv setup.cfg.dist setup.cfg

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python tests/pysndfile_test.py
}

%files %{python_files}
%doc ChangeLog README.md
%license COPYING.LESSER.txt
%{python_sitearch}/pysndfile
%{python_sitearch}/pysndfile-%{version}.dist-info

%changelog
