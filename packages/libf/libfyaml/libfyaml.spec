#
# spec file for package libfyaml
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           libfyaml
Version:        0.9
Release:        0
Summary:        YAML 1.2 parser and emitter
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/pantoniou/libfyaml
Source:         https://github.com/pantoniou/libfyaml/releases/download/v%{version}/libfyaml-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  m4
BuildRequires:  pkgconfig
Suggests:       libyaml-0-2

%description
A YAML 1.2 parser and emitter, featuring a no-copy paradigm.
Some YAML 1.3 is supported.

%define lib_name libfyaml0

%package -n %{lib_name}
Summary:        YAML 1.2 parser and emitter
Group:          System/Libraries

%description -n %{lib_name}
A YAML parser and emitter.

* Support for YAML version 1.2, some support for 1.3.
* Zero content copy operation; content is never copied to internal
  structures.
* Parser may be used in event mode (like libyaml) or in document
  generating mode.
* Programmable API for manipulating parsed YAML documents or
  creating them from scratch.
* YAML emitter with programmable options, supporting colored output.
* printf/scanf-based YAML creation and data extraction API.

%package devel
Summary:        Development files for libfyaml
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description devel
This package holds the development files for libfyaml,
a YAML parser and emitter written in C.

%package fy-tool
Summary:        Command line tools for libfyaml
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description fy-tool
This package provides a couple of command line tools for processing
YAML using libfyaml.

%prep
%setup -q -n libfyaml-%{version}

%build
./bootstrap.sh
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{lib_name}

%files -n %{lib_name}
%license LICENSE
%{_libdir}/libfyaml.so.0
%{_libdir}/libfyaml.so.0.0.0

%files devel
%{_includedir}/libfyaml.h
%{_libdir}/libfyaml.so
%{_libdir}/pkgconfig/libfyaml.pc

%files fy-tool
%{_bindir}/fy-compose
%{_bindir}/fy-dump
%{_bindir}/fy-filter
%{_bindir}/fy-join
%{_bindir}/fy-testsuite
%{_bindir}/fy-tool
%{_bindir}/fy-ypath

%files
%{_mandir}/man1/fy-*.1%{?ext_man}
%license LICENSE

%changelog
