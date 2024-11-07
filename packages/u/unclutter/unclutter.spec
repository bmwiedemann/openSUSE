#
# spec file for package unclutter
#
# Copyright (c) 2024 SUSE LLC
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


Name:           unclutter
Version:        8
Release:        0
Summary:        Remove the idle cursor image from the screen
License:        SUSE-Public-Domain
Group:          System/X11/Utilities
URL:            https://www.ibiblio.org/pub/X11/contrib/utilities/
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-return.diff
Patch1:         %{name}-%{version}-gcc14.patch
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Provides:       unclutt = %{version}
Obsoletes:      unclutt < %{version}

%description
Unclutterer removes the cursor image from the screen so that it does
not obstruct the area you are looking at after it has not moved for a
given period of time.

%prep
%autosetup -p0

%build
xmkmf
%make_build

%install
%make_install
make install.man DESTDIR=%{buildroot}

%files
%doc README
%{_bindir}/*
%{_mandir}/*/*

%changelog
