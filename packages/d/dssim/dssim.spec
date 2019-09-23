#
# spec file for package dssim
#
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           dssim
Version:        1.3.2
Release:        0
Summary:        This tool computes (dis)similarity between two (or more) PNG images
License:        AGPL-3.0
Group:          Productivity/Graphics/Other
Url:            https://kornel.ski/dssim
Source:         https://github.com/pornel/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpng16)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This tool computes (dis)similarity between two PNG images using 
(my approximation of) algorithms approximating human vision.

%prep
%setup -q

%build
make CFLAGS='%{optflags} -std=c99' %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m 0755 bin/dssim %{buildroot}%{_bindir}/dssim

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_bindir}/dssim

%changelog
