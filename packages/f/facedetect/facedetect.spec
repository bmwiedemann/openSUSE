#
# spec file for package facedetect
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           facedetect
Version:        0.1
Release:        0
Summary:        A simple face detector for batch processing
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Url:            https://www.thregr.org/~wavexx/software/facedetect/
Source:         https://github.com/wavexx/facedetect/archive/v%{version}.tar.gz
Patch1:         https://github.com/wavexx/facedetect/commit/8037d4406eb76dd5c106819f72c3562f8b255b5b.patch
BuildRequires:  python3-numpy
BuildRequires:  python3-opencv
Requires:       python3-numpy
Requires:       python3-opencv
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
facedetect is a simple face detector for batch processing. It answers the basic question: “Is there a face in this image?” and gives back either an exit code or the coordinates of each detected face in the standard output.

The aim is to provide a basic command-line interface that’s consistent and easy to use with software such as ImageMagick, while progressively improving the detection algorithm over time.

%prep
%setup -q
%patch1 -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 facedetect %{buildroot}%{_bindir}

%check
./%{name} -h

%files
%defattr(-,root,root)
%doc README.rst
%if 0%{?leap_version} >= 420200 || 0%{?suse_version} > 1320
%license COPYING.txt
%else
%doc COPYING.txt
%endif
%{_bindir}/%name

%changelog

