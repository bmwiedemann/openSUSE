#
# spec file for package ffsb
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ffsb
Version:        6.0_rc2
Release:        0
Summary:        Flexible File System Benchmark
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            http://sourceforge.net/projects/ffsb/
Source:         %{name}-%{version}.tar.bz2

%description
The Flexible Filesystem Benchmark (FFSB) is a filesystem performance
measurement tool.  It uses customizable profiles to measure of different
workloads, and it supports multiple groups of threads across multiple
filesystems.

%prep
%setup -q

%build
%configure
make RPM_OPT_FLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS README examples
%{_bindir}/ffsb

%changelog
