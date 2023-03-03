#
# spec file for package jpegoptim
#
# Copyright (c) 2023 SUSE LLC
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


Name:           jpegoptim
Version:        1.5.2
Release:        0
Summary:        Utility for Optimizing JPEG Files
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.kokkonen.net/tjko/projects.html
Source0:        https://github.com/tjko/jpegoptim/archive/refs/tags/v%{version}.tar.gz#/jpegoptim-%{version}.tar.gz
Source1:        https://github.com/tjko/jpegoptim/releases/download/v%{version}/jpegoptim-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  libjpeg-devel

%description
jpegoptim is a utility for optimizing JPEG files. It provides lossless
optimization (based on optimizing the Huffman tables) and "lossy" optimization
based on setting a maximum quality factor.

%prep
%setup -q

%build
%configure --with-arith
%make_build

%install
%make_install

%files
%license COPYRIGHT
%doc README
%{_bindir}/%{name}
%{_mandir}/man?/*

%changelog
