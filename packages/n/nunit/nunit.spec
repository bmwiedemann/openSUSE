#
# spec file for package nunit
#
# Copyright (c) 2020 SUSE LLC
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


%global __requires_exclude_from ^%{_prefix}/lib/nunit/tests/.*$
%global __requires_exclude ^.*pnunit.framework.*$
Name:           nunit
Version:        2.6.4
Release:        0
Summary:        Unit-testing framework for all .NET languages
License:        Zlib
Group:          Development/Libraries/Mono
URL:            http://www.nunit.org/
Source:         https://github.com/nunit/nunitv2/archive/%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/akoeplinger/mono/c3c8ee26f70e77a6ff2b72acbd6c900ce06db5f9/mcs/nunit24/nunit.pub
Patch1:         csc-pub-sign.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  libgdiplus0
BuildRequires:  mono-devel
BuildRequires:  strace
Provides:       mono-nunit = 5.20.2
Obsoletes:      mono-nunit <= 5.20.1
%if 0%{?fedora_version}
BuildRequires:  xorg-x11-fonts-truetype
%endif
%if 0%{?suse_version}
BuildRequires:  xorg-x11-fonts-core
%endif

%description
NUnit is a unit testing framework for all .NET languages. It serves the
same purpose as JUnit does in the Java world. It supports test
categories, testing for exceptions and writing test results in plain
text or XML.

%package devel
Summary:        Development files for NUnit
Group:          Development/Languages/Mono
Requires:       nunit = %{version}
Provides:       mono-nunit-devel = 5.20.2
Obsoletes:      mono-nunit-devel <= 5.20.1

%description devel
This package contains development files for NUnit integration.

%prep
%setup -q -n nunitv2-%{version}
#if [[ ! -z `2>/dev/null csc /version` ]]; then
%patch1 -p1
#fi

%build
# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;
cp %{S:1} .
xbuild nunit.sln /t:Rebuild /p:Configuration=Debug

%install
mkdir -p "%{buildroot}%{_prefix}/lib/nunit"
cp -a bin/Debug/* "%{buildroot}%{_prefix}/lib/nunit"
mkdir -p "%{buildroot}%{_docdir}/%{name}"
cp -a license.txt "%{buildroot}%{_docdir}/%{name}/"
cp -a doc "%{buildroot}%{_docdir}/%{name}/"
cp -a samples "%{buildroot}%{_docdir}/%{name}/"

#fake binaries
mkdir -p "%{buildroot}%{_bindir}"
for i in nunit nunit26; do
echo '#!/bin/sh
exec %{_bindir}/mono %{_prefix}/lib/nunit/nunit.exe "$@"' > "%{buildroot}%{_bindir}/${i}"
chmod +x "%{buildroot}%{_bindir}/${i}"
done
for i in nunit-console nunit-console2 nunit-console4 nunit-console26; do
echo '#!/bin/sh
exec %{_bindir}/mono %{_prefix}/lib/nunit/nunit-console.exe "$@"' > "%{buildroot}%{_bindir}/${i}"
chmod +x "%{buildroot}%{_bindir}/${i}"
done

find "%{buildroot}%{_docdir}/%{name}" -type f -exec dos2unix {} \;

#manually sign delay-signed assemblies
find "%{buildroot}%{_prefix}" \( -name "*.dll" -o -name "*.exe" \) -print0 | while IFS= read -r -d $'\0' target; do
  sn -v "$target" || if [[ $? = 1 ]]; then
    echo "manually signing assembly: $target"
    sn -R "$target" nunit.snk
  fi
done

mkdir -p %{buildroot}%{_prefix}/lib/mono/4.5
for i in nunit.core.dll nunit.core.interfaces.dll nunit.framework.dll nunit.util.dll lib/nunit-console-runner.dll lib/nunit-gui-runner.dll lib/nunit.uiexception.dll lib/nunit.uikit.dll framework/nunit.mocks.dll ; do
	gacutil -i %{buildroot}%{_prefix}/lib/nunit/$i -package nunit -root %{buildroot}%{_prefix}/lib
    name=$(echo $i | sed 's/\.dll//;s/.*\///')
    echo ${name}
    dir=$(echo %{buildroot}%{_prefix}/lib/mono/gac/${name}/* | sed 's|%{buildroot}||')
    echo ${dir}
    rm -rf %{buildroot}%{_prefix}/lib/nunit/$i
    ln -sf ${dir}/${name}.dll %{buildroot}%{_prefix}/lib/mono/4.5/${name}.dll
done

#pkgconfig
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/nunit.pc << EOF
prefix=%{_prefix}
exec_prefix=\${prefix}
libdir=\${exec_prefix}/lib
pkglibdir=\${prefix}/lib/mono/nunit

Name: NUnit
Description: Testing framework for .NET
Version: %{version}
Libs: -r:\${pkglibdir}/nunit.core.dll -r:\${pkglibdir}/nunit.core.interfaces.dll -r:\${pkglibdir}/nunit.framework.dll -r:\${pkglibdir}/nunit.util.dll -r:\${pkglibdir}/nunit-console-runner.dll -r:\${pkglibdir}/nunit-gui-runner.dll -r:\${pkglibdir}/nunit.uiexception.dll -r:\${pkglibdir}/nunit.uikit.dll -r:\${pkglibdir}/nunit.mocks.dll
EOF
cp -r %{buildroot}%{_libdir}/pkgconfig/nunit.pc %{buildroot}%{_libdir}/pkgconfig/mono-nunit.pc
sed -i 's/mono\/nunit/mono\/4\.5/' %{buildroot}%{_libdir}/pkgconfig/mono-nunit.pc
%fdupes %{buildroot}%{_prefix}

%files
%{_prefix}/lib/nunit
%{_prefix}/lib/mono/nunit
%{_prefix}/lib/mono/gac/nunit*
%{_prefix}/lib/mono/4.5/nunit*
%{_bindir}/nunit
%{_bindir}/nunit26
%{_bindir}/nunit-console
%{_bindir}/nunit-console2
%{_bindir}/nunit-console26
%{_bindir}/nunit-console4
%{_docdir}/nunit

%files devel
%{_libdir}/pkgconfig/nunit.pc
%{_libdir}/pkgconfig/mono-nunit.pc

%changelog
