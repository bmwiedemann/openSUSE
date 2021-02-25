#
# spec file for package python-av
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
%define skip_python36 1
Name:           python-av
Version:        8.0.3
Release:        0
Summary:        Python bindings for FFmpeg's libraries
License:        BSD-3-Clause
URL:            https://github.com/PyAV-Org/PyAV
Source:         https://files.pythonhosted.org/packages/source/a/av/av-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libavutil-devel >= 4.3
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Pythonic bindings for FFmpeg's libraries.

%prep
%setup -q -n av-%{version}

# doctests and timeout require network to setup tests
rm tests/test_doctests.py tests/test_timeout.py

# All tests using fate_suite require fetching data from http://fate.ffmpeg.org/fate-suite/
sed -Ei 's/(from .common import .*), fate_suite(, .*)?/\1\2\ndef fate_suite(*a):\n  import unittest; raise unittest.SkipTest\n/' tests/test_*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyav
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative pyav

%postun
%python_uninstall_alternative pyav

%check
mv av .av
# Skipping 4 tests requiring mpeg4 codec
%pytest_arch tests -k 'not (test_codec_mpeg4 or test_encoding_with_pts or test_stream_index or test_video_default_options)'
mv .av av

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/pyav
%{python_sitearch}/av
%{python_sitearch}/av-%{version}-py%{python_version}.egg-info

%changelog
