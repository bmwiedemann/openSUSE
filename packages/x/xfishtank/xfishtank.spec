#
# spec file for package xfishtank
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


Name:           xfishtank
Version:        2.5
Release:        0
Summary:        An aquarium in the root window
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Background
URL:            https://jim.rees.org/computers/xfishtank.html
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)

%description
A nice little aquarium with funny fish -- yet another background screen.

%prep
%autosetup -p0

%build
xmkmf -a
%make_build CCOPTIONS="%{optflags}"

%install
%make_install

%files
%doc README*
%{_bindir}/xfishtank
%{_mandir}/man1/xfishtank.1*

%changelog
