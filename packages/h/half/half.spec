#
# spec file for package half
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


%global debug_package %{nil}

Name:           half
Version:        2.2.0
Release:        11%{?dist}
Summary:        A C++ half-precision floating point type
License:        MIT

URL:            http://sourceforge.net/projects/half
Source0:        %{url}/files/%{name}/%{version}/%{name}-%{version}.zip
BuildArch:      noarch

BuildRequires:  unzip

%description
This is a C++ header-only library to provide an IEEE-754 conformant
half-precision floating point type along with corresponding arithmetic
operators, type conversions and common mathematical functions. It aims
for both efficiency and ease of use, trying to accurately mimic the
behaviour of the builtin floating point types at the best performance
possible. It automatically uses and provides C++11 features when
possible, but stays completely C++98-compatible when neccessary.

%package devel
Summary:        A C++ half-precision floating point type
Provides:       %{name}-static = %{version}-%{release}

%description devel
This is a C++ header-only library to provide an IEEE-754 conformant
half-precision floating point type along with corresponding arithmetic
operators, type conversions and common mathematical functions. It aims
for both efficiency and ease of use, trying to accurately mimic the
behaviour of the builtin floating point types at the best performance
possible. It automatically uses and provides C++11 features when
possible, but stays completely C++98-compatible when neccessary.

%prep
rm -rf %{name}-%{version}
unzip -d %{name}-%{version} %{SOURCE0}
cd %{name}-%{version}
# change dos endings to unix
sed -i "s|\r||g" include/half.hpp
sed -i "s|\r||g" LICENSE.txt
sed -i "s|\r||g" README.txt

%install
cd %{name}-%{version}
mkdir -p %{buildroot}%{_includedir}
install -m 644 include/half.hpp %{buildroot}%{_includedir}

mkdir -p %{buildroot}%{_docdir}/%{name}/
install -m 644 LICENSE.txt %{buildroot}%{_docdir}/%{name}/
install -m 644 README.txt %{buildroot}%{_docdir}/%{name}/

%files devel
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.txt
%license %{_docdir}/%{name}/LICENSE.txt
%{_includedir}/half.hpp

%changelog
