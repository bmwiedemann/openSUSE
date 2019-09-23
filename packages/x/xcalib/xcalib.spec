#
# spec file for package xcalib
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xcalib
Summary:        Load ICC profile calibration part to graphics card 
License:        GPL-2.0+
Group:          System/X11/Utilities
Version:        0.9.0
Release:        0
Source0:        %{name}-%{version}.tar.bz2 
Url:            http://www.etg.e-technik.uni-erlangen.de/web/doe/xcalib/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  cmake
BuildRequires:  color-filesystem
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
%if "%_repository" == "SUSE_Linux_10.1" || "%_repository" == "SLE_10"
BuildRequires:  pkg-config
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
export CFLAGS="$RPM_OPT_FLAGS"
%cmake
make VERBOSE=1 %{_smp_mflags}

%install
%cmake_install
rm -fv %{buildroot}%{_datadir}/color/icc/xcalib/test/Adobe*.icm

%files
%defattr(0644,root,root, 0755)
%doc README README.profilers COPYING
%defattr(0755,root,root)
%{_bindir}/xcalib
%defattr(0644,root,root)
%{_mandir}/man1/xcalib.1.gz

%files profiles
%defattr(-,root,root)
%{_datadir}/color/icc/xcalib/test/bluish.icc
%{_datadir}/color/icc/xcalib/test/gamma_1_0.icc
%{_datadir}/color/icc/xcalib/test/gamma_2_2_bright.icc
%{_datadir}/color/icc/xcalib/test/gamma_2_2.icc
%{_datadir}/color/icc/xcalib/test/gamma_2_2_lowContrast.icc
%doc README README.profilers COPYING
%dir %{_datadir}/color/icc/xcalib
%dir %{_datadir}/color/icc/xcalib/test

%changelog
