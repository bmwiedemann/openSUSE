#
# spec file for package octave-forge-video
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


%define octpkg  video
Name:           octave-forge-%{octpkg}
Version:        2.0.2
Release:        0
Summary:        A wrapper for OpenCV's CvCapture_FFMPEG and CvVideoWriter_FFMPEG
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig(octave)
BuildRequires:  pkgconfig(libavcodec) < 59
BuildRequires:  pkgconfig(libavformat) < 59
BuildRequires:  pkgconfig(libswscale) < 6
Requires:       octave-cli >= 4.4.0

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
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}/
%{octlib_dir}/%{octpkg}-%{version}/

%changelog
