#
# spec file for package pagetools
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016 Víctor Cuadrado Juan <vcuadradojuan@suse.de>
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


Name:           pagetools
Version:        0.1
Release:        0
Summary:        Automatic de-skew and bounding box determination for scanned page images
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Convertors
URL:            https://sourceforge.net/projects/pagetools
Source0:        https://sourceforge.net/projects/pagetools/files/pagetools/%{version}/pagetools-%{version}.tar.gz
Patch0:         01-makefile-clean-fix.patch
Patch1:         02-makefile-ldflags-add.patch
Patch2:         03-pbmfact.patch
BuildRequires:  gcc-c++
BuildRequires:  libnetpbm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libtiff-4)

%description
This program determines the skew angle for text, and works with black/white
images in TIFF or PBM format. To achieve this, it uses an original
algorithm based on a fast implementation of the Radon transform. This
program is part of the Page Layout Detection Tools project, which aims to
automate the layout detection in scanned page images.

%prep
%autosetup -c -p0

%build
%make_build C++_FLAGS="%{optflags}"

%install
install -Dpm 0755 pbm_findskew/pbm_findskew \
  %{buildroot}%{_bindir}/pbm_findskew
install -Dpm 0755 tiff_findskew/tiff_findskew \
  %{buildroot}%{_bindir}/tiff_findskew
install -Dpm 0644 pbm_findskew/pbm_findskew.1 \
  %{buildroot}%{_mandir}/man1/pbm_findskew.1
install -Dpm 0644 tiff_findskew/tiff_findskew.1 \
  %{buildroot}%{_mandir}/man1/tiff_findskew.1

%files
%license COPYING
%doc README.txt TODO
%{_bindir}/pbm_findskew
%{_bindir}/tiff_findskew
%{_mandir}/man1/pbm_findskew.1%{?ext_man}
%{_mandir}/man1/tiff_findskew.1%{?ext_man}

%changelog
