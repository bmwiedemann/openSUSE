#
# spec file for package python-pysndfile
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
Name:           python-pysndfile
Version:        1.3.2
Release:        0
Summary:        Cython wrapper class for reading/writing soundfiles
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://forge-2.ircam.fr/roebel/pysndfile
Source:         https://files.pythonhosted.org/packages/source/p/pysndfile/pysndfile-%{version}.tar.gz
Source10:       https://forge-2.ircam.fr/roebel/pysndfile/raw/master/COPYING.txt
Source11:       https://forge-2.ircam.fr/roebel/pysndfile/raw/master/COPYING.LESSER.txt
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel
BuildRequires:  python-rpm-macros
Requires:       python-numpy
%python_subpackages

%description
pysndfile is a python package providing PySndfile a
Cython wrapper class around libsndfile . PySndfile
provides methods for reading and writing a large variety of soundfile
formats on a variety of plattforms. PySndfile provides a rather complete
access to the different sound file manipulation options that are
available in libsndfile.

Due to the use of libsndfile nearly all sound file formats, (besides mp3
and derived formats) can be read and written with PySndfile.

The interface has been designed such that a rather large subset of the
functionality of libsndfile can be used, notably the reading and writing
of strings into soundfile formats that support these, and a number of
sf\_commands that allow to control the way libsndfile reads and writes
the samples. One of the most important ones is the use of the clipping
command.

%prep
%setup -q -n pysndfile-%{version}
cp %{SOURCE10} .
cp %{SOURCE11} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python tests/pysndfile_test.py
}

%files %{python_files}
%doc ChangeLog README.md
%license COPYING.txt COPYING.LESSER.txt
%{python_sitearch}/*

%changelog
