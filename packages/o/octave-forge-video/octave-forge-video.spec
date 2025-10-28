#
# spec file for package octave-forge-video
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define octpkg  video
Name:           octave-forge-%{octpkg}
Version:        2.1.3
Release:        0
Summary:        A wrapper for OpenCV's CvCapture_FFMPEG and CvVideoWriter_FFMPEG
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/video/
Source0:        https://github.com/Andy1978/octave-video/releases/download/%{version}/video-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  (pkgconfig(libavcodec) >= 58.35.100 with pkgconfig(libavcodec) < 62)
BuildRequires:  pkgconfig(libavformat) >= 58.20.100
BuildRequires:  pkgconfig(libswscale) >= 5.3.100
BuildRequires:  pkgconfig(octave)
Requires:       octave-cli >= 4.4.1

%description
A wrapper for OpenCV's CvCapture_FFMPEG and CvVideoWriter_FFMPEG.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%global octskiptests VideoWriter
echo "Skip tests requiring full ffmpeg: %{octskiptests}"
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}/
%{octlib_dir}/%{octpkg}-%{version}/

%changelog
