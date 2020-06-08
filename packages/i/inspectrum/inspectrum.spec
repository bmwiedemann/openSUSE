#
# spec file for package inspectrum
#
# Copyright (c) 2020 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           inspectrum
Version:        0.2.2+git.20200527
Release:        0
Summary:        A tool for analysing captured signals from SDRs
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://github.com/miek/inspectrum
Source:         %{name}-%{version}.tar.xz
Patch0:         inspectrum-fix-with-qt-5.15.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libliquid-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
# QCommandLineParser needs QT5.2+
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(fftw3f)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

%description
A tool for analysing captured signals, primarily from software-defined radio receivers

%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
install -Dm 0644 screenshot.jpg %{buildroot}/%{_datadir}/pixmaps/inspectrum.jpg
%suse_update_desktop_file -c inspectrum inspectrum "Offline Radio Signal Analyser" inspectrum inspectrum "Network;HamRadio"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/inspectrum.desktop
%{_datadir}/pixmaps/inspectrum.jpg

%changelog
