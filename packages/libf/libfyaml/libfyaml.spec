#
# spec file for package libfyaml
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lib_name libfyaml0

Name:           libfyaml
Version:        0.9.5
Release:        0
Summary:        YAML 1.2 parser and emitter
License:        MIT
URL:            https://github.com/pantoniou/libfyaml
Source:         https://github.com/pantoniou/libfyaml/releases/download/v%{version}/libfyaml-%{version}.tar.gz
%if 0%{?suse_version} == 1500
BuildRequires:  gcc14
BuildRequires:  gcc14-c++
BuildRequires:  gcc14-PIE
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  m4
BuildRequires:  pkgconfig

%description
A YAML 1.2 parser and emitter, featuring a no-copy paradigm.
Some YAML 1.3 is supported.

%package -n %{lib_name}
Summary:        YAML 1.2 parser and emitter

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
Requires:       %{lib_name} = %{version}

%description devel
This package holds the development files for libfyaml,
a YAML parser and emitter written in C.

%package fy-tool
Summary:        Command line tools for libfyaml
Requires:       %{lib_name} = %{version}
# Merged manpages in the 0.9.3 update
Provides:       libfyaml = 0.9.3
Obsoletes:      libfyaml < 0.9.3

%description fy-tool
This package provides a couple of command line tools for processing
YAML using libfyaml.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} == 1500
export CC=gcc-14 CXX=g++-14
%endif
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
%doc AUTHORS README.md
%{_libdir}/libfyaml.so.0
%{_libdir}/libfyaml.so.0.0.0

%files devel
%{_includedir}/libfyaml.h
%{_libdir}/libfyaml.so
%{_libdir}/pkgconfig/libfyaml.pc

%files fy-tool
%license LICENSE
%{_bindir}/fy-compose
%{_bindir}/fy-dump
%{_bindir}/fy-filter
%{_bindir}/fy-join
%{_bindir}/fy-testsuite
%{_bindir}/fy-tool
%{_bindir}/fy-ypath
%doc %{_mandir}/man1/fy-*.1%{?ext_man}

%changelog
