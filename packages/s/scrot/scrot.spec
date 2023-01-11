#
# spec file for package scrot
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


Name:           scrot
Version:        1.8
Release:        0
Summary:        Screenshot Capture Utility
License:        SUSE-Scrot
Group:          Productivity/Graphics/Other
URL:            https://github.com/resurrecting-open-source-projects/scrot
Source:         https://github.com/resurrecting-open-source-projects/scrot/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(zlib)

%description
A nice and straightforward screen capture utility implementing
the dynamic loaders of imlib2.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
mkdir -p %{buildroot}/%{_datadir}/pixmaps/
rm -rf %{buildroot}/%{_datadir}/doc/scrot

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
