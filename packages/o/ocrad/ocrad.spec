#
# spec file for package ocrad
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


Name:           ocrad
Version:        0.29
Release:        0
Summary:        Optical Character Recognition Program
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.gnu.org/software/ocrad/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.lz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.lz.sig
Source2:        %{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  lzip
Requires(post): info
Requires(preun): info

%description
GNU Ocrad is an OCR (Optical Character Recognition) program based on a feature
extraction method. It reads images in pbm (bitmap), pgm (greyscale) or ppm
(color) formats and produces text in byte (8-bit) or UTF-8 formats.

Also includes a layout analyser able to separate the columns or blocks of text
normally found on printed pages.

Ocrad can be used as a stand-alone console application, or as a backend to
other programs.

%package devel
Summary:        Development files for GNU ocrad
Group:          Development/Libraries/C and C++

%description devel
Development files for GNU ocrad - useful for programs implementing OCR.

%prep
%setup -q

%build
%configure
%make_build CXXFLAGS="%{optflags}"

%install
%make_install
rm -f %{buildroot}%{_libdir}/libocrad.a

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/ocrad
%{_infodir}/ocrad*
%{_mandir}/man1/ocrad*

%files devel
%{_includedir}/ocradlib.h

%changelog
