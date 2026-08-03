#
# spec file for package disorderfs
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


Name:           disorderfs
Version:        0.7.0
Release:        0
Summary:        FUSE filesystem that introduces non-determinism
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://salsa.debian.org/reproducible-builds/disorderfs
Source0:        https://reproducible-builds.org/_lfs/releases/disorderfs/disorderfs-%{version}.tar.gz
Source1:        https://reproducible-builds.org/_lfs/releases/disorderfs/disorderfs-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(fuse3)
Requires:       fuse3

%description
disorderfs is an overlay FUSE filesystem that introduces non-determinism into
filesystem metadata. For example, it can randomize the order in which
directory entries are read. This is useful for detecting non-determinism
in the build process.

%prep
%setup -q -c

%build
export CXXFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
