#
# spec file for package lepton
#
# Copyright (c) 2022 SUSE LLC
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


Name:           lepton
Version:        1.2.1+git.20201230
Release:        0
Summary:        Tool and file format for losslessly compressing JPEGs
License:        Apache-2.0
Group:          Productivity/Archiving/Compression
URL:            https://github.com/dropbox/lepton
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  x86_64

%description
Lepton is a tool and file format for losslessly compressing JPEGs by an
average of 22%.

This can be used to archive large photo collections, or to serve images
live and save 22% bandwidth.

%prep
%autosetup

%build
autoreconf -fiv
%configure \
  --disable-vectorization \
  --enable-system-dependencies
%make_build

%install
%make_install

%check
# Tests get randomly stuck
#make %{?_smp_mflags} check

%files
%license LICENSE
%doc README.md
%{_bindir}/lepton

%changelog
