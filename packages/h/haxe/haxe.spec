#
# spec file for package haxe
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global commit_haxelib 4b27f91d8a4ff279d9903091680fee2c93a0d574
%global commit_hx3compat f1f18201e5c0479cb5adf5f6028788b37f37b730

Name:           haxe
Version:        4.1.1
Release:        0
Summary:        Multiplatform programming language
License:        GPL-2.0+ and MIT
Group:          Development/Languages/Other
# As described in http://haxe.org/foundation/open-source.html:
#   * The Haxe Compiler - GPLv2+
#   * The Haxe Standard Library - MIT
Url:            https://haxe.org/
Source0:        https://github.com/HaxeFoundation/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/HaxeFoundation/haxelib/archive/%{commit_haxelib}.tar.gz#/haxelib-%{commit_haxelib}.tar.gz
Source2:        https://github.com/HaxeFoundation/hx3compat/archive/%{commit_hx3compat}.tar.gz#/hx3compat-%{commit_hx3compat}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  help2man
BuildRequires:  neko-devel >= 2.3.0
BuildRequires:  neko >= 2.3.0
BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-sedlex-devel >= 2.0
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-ptmap-devel
BuildRequires:  ocaml-sha-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pcre-devel-static
BuildRequires:  mbedtls-devel
BuildRequires:  cmake
Requires:       neko >= 2.3.0

%description
Haxe is a high-level multiplatform programming language and compiler
that can produce applications and source code for many different
platforms from a single code-base. The Haxe compiler can compile Haxe
source code to Adobe Flash SWF files, ActionScript 3, JavaScript,
C++, PHP, C#, Java, Python, Lua, and Neko VM binary files.

%prep
%autosetup -p1

%build
pushd extra/haxelib_src && tar -xf %{SOURCE1} --strip-components=1 && popd
pushd extra/haxelib_src/hx3compat && tar -xf %{SOURCE2} --strip-components=1 && popd

# note that the Makefile does not support parallel building
make haxe

# Compile haxelib
pushd extra/haxelib_src && \
%cmake && \
make %{?_smp_mflags} && \
cp haxelib ../../../haxelib
popd

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}

cp -p haxe %{buildroot}%{_bindir}
cp -p haxelib %{buildroot}%{_bindir}
cp -rfp std %{buildroot}%{_datadir}/%{name}

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
help2man ./haxe --version-option=-version --no-discard-stderr --no-info --output=%{buildroot}%{_mandir}/man1/haxe.1
help2man ./haxelib --help-option=help --version-option=version --no-info --output=%{buildroot}%{_mandir}/man1/haxelib.1

%check
%{buildroot}%{_bindir}/haxe -version
%{buildroot}%{_bindir}/haxelib version

%files
%defattr(-,root,root)
%doc README.md extra/LICENSE.txt extra/CHANGES.txt extra/CONTRIB.txt
%{_bindir}/haxe
%{_bindir}/haxelib
%{_mandir}/man1/haxe.1*
%{_mandir}/man1/haxelib.1*
%{_datadir}/%{name}/

%changelog
