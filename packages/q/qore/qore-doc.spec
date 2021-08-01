#
# spec file for package qore-doc
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


Name:           qore-doc
Version:        0.9.15
Release:        0
Summary:        Multithreaded Programming Language
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MIT
Group:          Development/Languages/Other
URL:            https://qore.org
Source0:        https://github.com/qorelanguage/qore/archive/refs/tags/release-%{version}.tar.gz#/qore-release-%{version}.tar.gz
# PATCH-FIX-OPENSUSE bmwiedemann boo#1084909
Patch0:         reproducible.patch
BuildRequires:  bison
BuildRequires:  bzip2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.31
BuildRequires:  gcc-c++ >= 4.8.1
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  mpfr-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  qore = %{version}
BuildRequires:  qore-json-module >= 1.8+qore%{version}
BuildRequires:  qore-linenoise-module >= 1.0.0+qore%{version}
BuildRequires:  qore-yaml-module >= 0.7.0+qore%{version}
BuildRequires:  zlib-devel

%description
Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

%package -n qore-devel-doc
Summary:        Module and library documentation for Qore
Group:          Documentation/HTML

%description -n qore-devel-doc
This package contains the module and library documentation.

Qore is a scripting language supporting threading and embedded logic.
It applies a scripting-based approach to interface development and
can also be used as a general purpose language.

%prep
%autosetup -p1 -n qore-release-%{version}
echo "#define BUILD \"openSUSE\"" > include/qore/intern/git-revision.h

%build
autoreconf -fi
%configure
make html-local

%install

%files
%doc docs/lang/html/*

%files -n qore-devel-doc
%doc docs/library docs/modules

%changelog
