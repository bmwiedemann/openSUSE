#
# spec file for package edid-decode
#
# Copyright (c) 2016-2021 SUSE LLC
# Copyright (c) 2013-2023 Guillaume GARDET <guillaume@opensuse.org>
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



Name:           edid-decode
Version:        0.0~git20231123.d6d86cb
Release:        0
Summary:        EDID decoder and conformance tester
Group:          Hardware/Other
Url:            https://git.linuxtv.org/edid-decode.git/about/
Source:         %{name}-%{version}.tar.xz
License:        GPL-2.0+
BuildRequires:  gcc-c++
BuildRequires:  make

%description
Decodes to text the binary EDID information from monitors.
EDID is binary data encoded in the monitor firmware, which the kernel exposes via /sys/devices/.../drm/card*/card*/edid. edid-decode renders this binary data into a human-readable text form.


%prep
%setup -q

%build
%make_build

%install
%make_install


%files
%{_bindir}/edid-decode
%{_mandir}/man1/edid-decode.1.gz


%changelog
