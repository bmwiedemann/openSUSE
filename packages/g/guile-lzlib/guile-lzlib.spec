#
# spec file for package guile-lzlib
#
# Copyright (c) 2020 SUSE LLC
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


Name:           guile-lzlib
Version:        0.0.2
Release:        0
Summary:        Guile bindings to lzlib
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://notabug.org/guile-lzlib/guile-lzlib
Source0:        https://notabug.org/guile-lzlib/guile-lzlib/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-devel
BuildRequires:  lzlib-devel
BuildRequires:  pkg-config
Requires:       guile
Requires:       lzlib-devel

%description
This package provides Guile bindings to lzlib, a data compression library
providing in-memory LZMA compression and decompression.

%prep
%setup -q -n %{name}

%build
autoreconf -vfi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{_datadir}/guile/*
%{_libdir}/guile/*

%changelog
