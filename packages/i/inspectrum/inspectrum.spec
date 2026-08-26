#
# spec file for package inspectrum
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2015-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           inspectrum
Version:        0.4.0
Release:        0
Summary:        A tool for analysing captured signals from SDRs
License:        GPL-3.0-or-later
URL:            https://github.com/miek/inspectrum
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz/#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libliquid-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(fftw3f)

%description
A tool for analysing captured signals, primarily from software-defined radio receivers

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
install -D -m 0644 screenshot.jpg %{buildroot}%{_datadir}/pixmaps/%{name}.jpg
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.jpg

%changelog
