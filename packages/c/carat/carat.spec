#
# spec file for package pari
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


Name:           carat
Version:        2.1b1+g132
Release:        0
Summary:        Programs for solving certain tasks in mathematical crystallography
License:        GPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            https://lbfm-rwth.github.io/carat/
Source:         %name-%version.tar.xz
BuildRequires:  automake
BuildRequires:  c_compiler
BuildRequires:  gmp-devel

%description
Carat is a computer package which handles enumeration,
construction, recognition and comparison problems for
crystallographic groups up to dimension 6. The name CARAT itself
is an acronym for Crystallographic AlgoRithms And Tables.

# Utilies invoked from e.g. gap-caratinterface

%prep
%autosetup

%build
autoreconf -fi
%configure --bindir="%_libexecdir/%name"
%make_build

%install
%make_install

%files
%_libexecdir/%name/
%license LICENSE

%changelog
