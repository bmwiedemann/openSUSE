#
# spec file for package frugally-deep
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
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


%bcond_with test

# Header only package
%global debug_package %{nil}

Summary:        Header-only library for using Keras (TensorFlow) models in C++
Name:           frugally-deep
License:        MIT
# Main license is MIT
# BSD-2-Clause is only for cmake/HunterGate.cmake and that is not distributed
Version:        0.15.30
Release:        12%{?dist}

URL:            https://github.com/Dobiasd/frugally-deep
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  fplus-devel
%if 0%{?suse_version}
BuildRequires:  nlohmann_json-devel
%else
BuildRequires:  json-devel
%endif
BuildRequires:  gcc-c++

%description
Would you like to build/train a model using Keras/Python? And would
you like to run the prediction (forward pass) on your model in C++
without linking your application against TensorFlow? Then
frugally-deep is exactly for you.

frugally-deep

* is a small header-only library written in modern and pure C++.
* is very easy to integrate and use.
* depends only on FunctionalPlus, Eigen and json - also header-only
  libraries.
* supports inference (model.predict) not only for sequential models
  but also for computational graphs with a more complex topology,
  created with the functional API.
* re-implements a (small) subset of TensorFlow, i.e., the operations
  needed to support prediction.
* results in a much smaller binary size than linking against TensorFlow.
* works out-of-the-box also when compiled into a 32-bit executable.
  (Of course, 64 bit is fine too.)
* avoids temporarily allocating (potentially large chunks of)
  additional RAM during convolutions (by not materializing the im2col
  input matrix).
* utterly ignores even the most powerful GPU in your system and uses
  only one CPU core per prediction. ;-)
* but is quite fast on one CPU core, and you can run multiple
  predictions in parallel, thus utilizing as many CPUs as you like
  to improve the overall prediction throughput of your
  application/pipeline.

%package devel

Summary:        Header-only library for using Keras (TensorFlow) models in C++
Provides:       %{name}-static = %{version}-%{release}

%description devel
Would you like to build/train a model using Keras/Python? And would
you like to run the prediction (forward pass) on your model in C++
without linking your application against TensorFlow? Then
frugally-deep is exactly for you.

frugally-deep

* is a small header-only library written in modern and pure C++.
* is very easy to integrate and use.
* depends only on FunctionalPlus, Eigen and json - also header-only
  libraries.
* supports inference (model.predict) not only for sequential models
  but also for computational graphs with a more complex topology,
  created with the functional API.
* re-implements a (small) subset of TensorFlow, i.e., the operations
  needed to support prediction.
* results in a much smaller binary size than linking against TensorFlow.
* works out-of-the-box also when compiled into a 32-bit executable.
  (Of course, 64 bit is fine too.)
* avoids temporarily allocating (potentially large chunks of)
  additional RAM during convolutions (by not materializing the im2col
  input matrix).
* utterly ignores even the most powerful GPU in your system and uses
  only one CPU core per prediction. ;-)
* but is quite fast on one CPU core, and you can run multiple
  predictions in parallel, thus utilizing as many CPUs as you like
  to improve the overall prediction throughput of your
  application/pipeline.

%prep
%autosetup -p1 -n %{name}-%{version}

# cmake changed
sed -i -e 's@cmake_minimum_required(VERSION 3.2)@cmake_minimum_required(VERSION 3.5)@' CMakeLists.txt

%build
%cmake
%cmake_build

%if %{with test}
%check
%ctest
%endif

%install
%cmake_install

%files devel
%dir %_includedir/fdeep
%dir %_libdir/cmake/%{name}
%license LICENSE
%doc README.md
%_includedir/fdeep/*
%_libdir/cmake/%{name}/*

%changelog
