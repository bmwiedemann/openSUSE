#
# spec file for package xcalib
#
# Copyright (c) 2021 SUSE LLC
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


Name:           xcalib
Version:        0.10
Release:        0
Summary:        Load ICC profile calibration part to graphics card
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://github.com/OpenICC/xcalib
Source0:        https://github.com/OpenICC/xcalib/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  color-filesystem
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
%if "%{_repository}" == "SUSE_Linux_10.1" || "%{_repository}" == "SLE_10"
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-compat70-devel
%endif

%description
The command line tool applies the 'vcgt'-tag of ICC profiles to your X-server
like MS-Windows or MacOS can to set your display to a calibrated state.

Versions 0.5 and higher are also usable with Microsoft Windows.
They can be used as a free alternative to other calibration loaders.

%package profiles
Summary:        ICC profiles for testing with xcalib
Group:          Productivity/Graphics/Other

%description profiles
The ICC profiles are special for testing xcalib.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
rm -fv %{buildroot}%{_datadir}/color/icc/xcalib/test/Adobe*.icm

%files
%defattr(0644,root,root, 0755)
%license COPYING
%doc README.md README.profilers
%defattr(0755,root,root)
%{_bindir}/xcalib
%defattr(0644,root,root)
%{_mandir}/man1/xcalib.1%{?ext_man}

%files profiles
%license COPYING
%doc README.md README.profilers
%{_datadir}/color/icc/xcalib/test/bluish.icc
%{_datadir}/color/icc/xcalib/test/gamma_1_0.icc
%{_datadir}/color/icc/xcalib/test/gamma_2_2_bright.icc
%{_datadir}/color/icc/xcalib/test/gamma_2_2.icc
%{_datadir}/color/icc/xcalib/test/gamma_2_2_lowContrast.icc
%dir %{_datadir}/color/icc/xcalib
%dir %{_datadir}/color/icc/xcalib/test

%changelog
