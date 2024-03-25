#
# spec file for package pngcrush
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


Name:           pngcrush
Version:        1.8.13
Release:        0
Summary:        Optimizer for PNG Files that can also insert or delete specified Chunks
License:        Zlib
Group:          Productivity/Graphics/Other
URL:            https://pmt.sourceforge.io/pngcrush/
Source:         https://downloads.sourceforge.net/project/pmt/pngcrush/%{version}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/project/pmt/pngcrush/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM -- https://github.com/glennrp/pmt/pull/2
Patch0:         0001-Check-for-defined-PNG_IGNORE_ADLER32.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
pngcrush is an excellent batch-mode compression utility for PNG
images. Depending on the application that created the original PNGs, it can
improve the file size anywhere from a few percent to 40%% or more (completely
losslessly). The utility also allows specified PNG chunks (e.g. text comments)
to be inserted or deleted, and it can fix incorrect gamma info written by
Photoshop 5.0 as well as the erroneous iCCP chunk written by Photoshop 5.5.

%prep
%autosetup -p1

%build
%make_build -f Makefile-nolib \
	PNGINC="$(pkg-config --variable includedir libpng)" \
	PNGLIB="$(pkg-config --variable libdir libpng)" \
	ZINC="$(pkg-config --variable includedir zlib)" \
	ZLIB="$(pkg-config --variable libdir zlib)" \
	CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 pngcrush %{buildroot}%{_bindir}

%files
%license LICENSE
%doc ChangeLog.html
%{_bindir}/pngcrush

%changelog
