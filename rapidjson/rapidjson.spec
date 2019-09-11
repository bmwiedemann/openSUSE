#
# spec file for package rapidjson
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rapidjson
Version:        1.1.0+git20190517.4b3d7c2f
Release:        0
Summary:        JSON parser and generator for C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://rapidjson.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
RapidJSON is a JSON parser and generator for C++. It was inspired by RapidXml.

* It supports both SAX and DOM style API. The SAX parser is only a
  half thousand lines of code.
* It optionally supports SSE2/SSE4.2 for acceleration.
* Header-only implementation. It does not depend on STL.
* Each JSON value occupies exactly 16/20 bytes for most 32/64-bit
  machines (excluding text string). By default, it uses a memory
  allocator, and the parser allocates memory compactly during
  parsing.
* It supports UTF-8, UTF-16, UTF-32 (LE & BE), and their detection,
  validation and transcoding internally. For example, you can read a
  UTF-8 file and let RapidJSON transcode the JSON strings into UTF-16
  in the DOM. It also supports surrogates and "\u0000" (null
  character).

%package devel
Summary:        Header files for rapidjson, a JSON parser and generator for C++
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}

%description devel
RapidJSON is a header-only JSON parser and generator for C++.
This package contains development headers and examples.

%prep
%setup -q
sed -i -e 's:-Werror::g' CMakeLists.txt

%build
%cmake \
  -DDOC_INSTALL_DIR=%{_docdir}/%{name}-devel \
  -DRAPIDJSON_BUILD_TESTS=ON \
  -DRAPIDJSON_ENABLE_INSTRUMENTATION_OPT=OFF
%cmake_build

%install
%cmake_install

%files devel
%doc CHANGELOG.md readme.md
%license license.txt
%dir %{_docdir}/%{name}-devel
%{_docdir}/%{name}-devel/*
%{_includedir}/rapidjson/
%{_libdir}/cmake/RapidJSON/
%{_libdir}/pkgconfig/*.pc

%changelog
