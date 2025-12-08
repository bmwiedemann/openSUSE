#
# spec file for package obs-service-recompress
#
# Copyright (c) 2025 SUSE LLC
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


# SLE-12 doesn't have the make_build macro
%{!?make_build: %define make_build make %{?_smp_mflags}}

%define service recompress
Name:           obs-service-%{service}
Version:        0.5.2
Release:        0
Summary:        An OBS source service: Recompress files
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{name}-%{version}.tar.gz
BuildRequires:  bzip2
BuildRequires:  gzip
BuildRequires:  xz
BuildRequires:  perl(Test::More)
Requires:       %{_bindir}/gzip
Requires:       bzip2
Requires:       xz
BuildArch:      noarch
# Enable zstd on all supported distributions
%if 0%{?suse_version} >= 1500 || 0%{?fedora_version} > 25
BuildRequires:  zstd
Requires:       zstd
%endif

%description
This is a source service for openSUSE Build Service.

It supports to compress, uncompress or recompress files from or to

 none : No Compression
 gz   : Gzip Compression
 bz2  : Bzip2 Compression
 xz   : XZ Compression
 zstd : Zstd Compression

%prep
%setup -q

%build

%install
%make_install

%check
%make_build test

%files
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
