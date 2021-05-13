#
# spec file for package guile-zlib
#
# Copyright (c) 2021 SUSE LLC
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


Name:           guile-zlib
Version:        0.1.0
Release:        0
Summary:        Guile bindings to zlib
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://notabug.org/guile-zlib/guile-zlib
Source0:        https://notabug.org/guile-zlib/guile-zlib/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
Requires:       guile
Requires:       zlib-devel

%description
This package provides Guile bindings to zlib, a data lossless date-coompression
library.

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
