#
# spec file for package premake4
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} > 1320
%define luapkg lua5.1
%else
%define luapkg lua
%endif

Name:           premake4
Version:        4.4beta4
Release:        0
Summary:        Powerfully simple build configuration
License:        BSD-3-Clause
Group:          Development/Tools/Building
Url:            http://industriousone.com/premake
Source:         http://downloads.sourceforge.net/project/premake/Premake/4.4/premake-4.4-beta4-src.zip
# PATCH-FIX-OPENSUSE premake-4.4.patch mailaender@opensuse.org -- use shared lua;
Patch0:         premake-4.4.patch
BuildRequires:  lua51-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip

%description
Premake is a build configuration tool. Describe your C, C++, or C# software project
using a simple, easy to read syntax and let Premake generate the project files for:
 * Microsoft Visual Studio including the Express editions
 * GNU Make, including Cygwin and MinGW
 * Apple Xcode
 * Code::Blocks
 * CodeLite
 * IC#Code SharpDevelop
 * MonoDevelop

%prep
%setup -q -n premake-4.4-beta4
%patch0 -p1
rm -rf src/host/lua-5.1.4

%build
pushd build/gmake.unix
make \
  Premake4 \
  config=debug \
  DEFINES="-DNDEBUG" \
  INCLUDES="" \
  CFLAGS="`pkg-config %{luapkg} --cflags` \$(CPPFLAGS) %{optflags}" \
  LDFLAGS="-rdynamic" \
  LIBS="`pkg-config %{luapkg} --libs`" \
  verbose=1 \
  %{?_smp_mflags}
popd

%install
install -D -m 0755 bin/debug/premake4 %{buildroot}%{_bindir}/%{name}

%files
%doc CHANGES.txt LICENSE.txt README.txt
%{_bindir}/%{name}

%changelog
