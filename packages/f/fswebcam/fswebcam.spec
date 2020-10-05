#
# spec file for package fswebcam
#
# Copyright (c) 2020 SUSE LLC
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


Name:           fswebcam
Version:        20200725
Release:        0
Summary:        Tiny and flexible webcam program
License:        GPL-2.0-only
URL:            https://www.sanslogic.co.uk/fswebcam/
Source0:        https://www.sanslogic.co.uk/fswebcam/files/%{name}-%{version}.tar.xz
BuildRequires:  gd-devel > 2
Requires:       gd > 2

%description
Tiny and flexible webcam program for capturing images from a V4L1/V4L2
device, and overlaying a caption or image.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README CHANGELOG example.conf
%{_bindir}/fswebcam
%{_mandir}/man1/fswebcam.1%{?ext_man}

%changelog
