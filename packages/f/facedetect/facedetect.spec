#
# spec file for package facedetect
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


Name:           facedetect
Version:        0.1
Release:        0
Summary:        A face detector for batch processing
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.thregr.org/~wavexx/software/facedetect/
Source:         https://gitlab.com/wavexx/facedetect/-/archive/v%{version}/facedetect-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         https://gitlab.com/wavexx/facedetect/-/commit/8037d4406eb76dd5c106819f72c3562f8b255b5b.patch#/python3.patch
BuildRequires:  python3-numpy
BuildRequires:  python3-opencv
Requires:       python3-numpy
Requires:       python3-opencv
BuildArch:      noarch

%description
facedetect is a face detector for batch processing. It determines
whether there is a face in an image and gives back either an exit
code or the coordinates of each detected face, on standard output.

It provides a basic command-line interface that can be used with
software such as ImageMagick.

%prep
%autosetup -p1 -n %{name}-v%{version}
sed -i '1s/^#!\/usr\/bin\/env /#!\/usr\/bin\//' facedetect

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 facedetect %{buildroot}%{_bindir}

%files
%doc README.rst
%license COPYING.txt
%{_bindir}/%name

%changelog
