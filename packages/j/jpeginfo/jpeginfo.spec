#
# spec file for package jpeginfo
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020-2023 Szőts Ákos <szotsaki@gmail.com>
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


Name:           jpeginfo
Version:        1.7.1
Release:        0
Summary:        Generate informative listings from JPEG files and check them for errors
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/tjko/jpeginfo
Source:         v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libturbojpeg)

%description
Utility to generate informative listings from JPEG files and to check them for errors.
Also supports automatic deletion of broken JPEGs.

%prep
%setup -q
autoconf -f

%build
%configure
%make_build
%make_build strip

%install
%make_install

%files
%license COPYRIGHT
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
