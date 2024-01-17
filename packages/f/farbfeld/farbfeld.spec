#
# spec file for package farbfeld
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


Name:           farbfeld
Version:        4
Release:        0
Summary:        Farbfeld image conversion tools
License:        ISC
Group:          Productivity/Graphics/Convertors
URL:            https://tools.suckless.org/farbfeld/
Source:         https://dl.suckless.org/farbfeld/farbfeld-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  pkgconfig

%description
Tools for converting images into and from the suckless.org farbfeld
format, which is practically the same as the Netpbm P7 RGB_ALPHA
format, only with a custom header.

%prep
%autosetup

%build
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%{_bindir}/png2ff
%{_bindir}/ff2png
%{_bindir}/jpg2ff
%{_bindir}/ff2jpg
%{_bindir}/ff2pam
%{_bindir}/ff2ppm
%{_bindir}/2ff
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/farbfeld.5%{?ext_man}

%changelog
