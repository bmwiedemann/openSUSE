#
# spec file for package QSVEnc
#
# Copyright (c) 2024 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           QSVEnc
Version:        7.71+0
Release:        0
Summary:        HW encoder (QSV) testing
License:        MIT
URL:            https://github.com/rigaya/QSVEnc
Source0:        %{name}-%{version}.tar.xz
#PATCH-FIX-OPENSUSE QSVEnc-remove-git.patch malcolmlewis@opensuse.org -- Remove git call for ENCODER_REV
Patch0:         QSVEnc-remove-git.patch
#PATCH-FIX-OPENSUSE QSVEnc-enable-vulkan.patch malcolmlewis@opensuse.org -- Enable Vulkan and Placebo.
Patch1:         QSVEnc-enable-vulkan.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig(dovi)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libplacebo) 
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(vapoursynth)
BuildRequires:  pkgconfig(vulkan)

%description
Investigate performance and image quality of HW encoder (QSV) of Intel.

%prep
%autosetup
# Fix end of line encoding warning
sed -i 's/\r//' QSVEncC_Options.en.md;

%build
./configure --prefix=%{_prefix} \
            --disable-avisynth \
            --disable-dtl \
            --enable-lto \
            --extra-ldflags="-Wl,-z,noexecstack"
%make_build

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 qsvencc %{buildroot}%{_bindir}/qsvencc

%files
%license license.txt
%doc QSVEncC_Options.en.md
%{_bindir}/qsvencc

%changelog

