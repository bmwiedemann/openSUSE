#
# spec file for package scrot
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


Name:           scrot
Version:        1.3
Release:        0
Summary:        Screenshot Capture Utility
License:        SUSE-Scrot
Group:          Productivity/Graphics/Other
URL:            https://github.com/resurrecting-open-source-projects/scrot 
Source:         https://github.com/resurrecting-open-source-projects/scrot/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(giblib)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(zlib)

%description
A nice and straightforward screen capture utility implementing
the dynamic loaders of imlib2.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README.md TODO CONTRIBUTING.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
