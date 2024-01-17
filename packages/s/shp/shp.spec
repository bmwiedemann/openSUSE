#
# shp - Like PHP except you write your script in shell script
# 
# Copyright 2011 Archie L. Cobbs <archie@dellroad.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

%define name        shp
%define pkgdir      %{_datadir}/%{name}

Name:           %{name}
Version:        1.0.2
Release:        1
Summary:        Like PHP except you write your script in shell script
Group:          Development/Languages/Other
License:        Apache-2.0
BuildRoot:      %{_tmppath}/%{name}-root
Buildarch:      noarch
Source:         %{name}-%{version}.tar.gz
URL:            http://shp.googlecode.com/
BuildRequires:  bash
BuildRequires:  gawk
BuildRequires:  openssl
BuildRequires:  coreutils
Requires:       bash
Requires:       gawk
Requires:       openssl
Requires:       coreutils

%description
%{name} parses and executes SHP scripts in the manner of PHP, except nested
scripts are written in shell scripting language instead of the PHP language.
%{name} outputs its script file, with nested <?shp ... ?> blocks executed
as shell scripts.

%clean
rm -rf ${RPM_BUILD_ROOT}

%prep
%setup

%build
%configure
%__make

%install
%makeinstall

%files
%attr(755,root,root) %{_bindir}/%{name}
%defattr(644,root,root,0755)
%{_mandir}/man?/*
%doc %{_datadir}/doc/packages/%{name}
%{pkgdir}

