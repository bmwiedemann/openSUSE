#
# spec file for package python-ffmpeg-python
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
Name:           python-ffmpeg-python
Version:        0.2.0
Release:        0
Summary:        Python bindings for FFmpeg
License:        Apache-2.0
URL:            https://github.com/kkroening/ffmpeg-python
Source:         https://github.com/kkroening/ffmpeg-python/archive/%{version}.tar.gz#/ffmpeg-python-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
Recommends:     ffmpeg
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  ffmpeg
# /SECTION
%python_subpackages

%description
Python bindings for FFmpeg - with complex filtering support

%prep
%setup -q -n ffmpeg-python-%{version}
# https://github.com/kkroening/ffmpeg-python/issues/617
sed -i 's:pytest-runner::' setup.py
# https://github.com/kkroening/ffmpeg-python/issues/624
sed -i 's/collections.Iterable/collections.abc.Iterable/' ffmpeg/_run.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip some tests since we do not have FFmpeg with mp4-support on the public OBS instance
# test__probe fails because of missing libopenh264 on plain openSUSE
# test_pipe - fails on Leap due to too old FFmpeg
%pytest -k 'not (test__run or test__run__multi_output or test_pipe or test__probe)'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/ffmpeg
%{python_sitelib}/ffmpeg_python-%{version}*-info

%changelog
