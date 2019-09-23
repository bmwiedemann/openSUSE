#
# spec file for package nunit
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


Name:           nunit
Version:        2.6.4
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Url:            http://www.nunit.org/
Source:         https://github.com/nunit/nunitv2/archive/%{version}.tar.gz
Patch1:         csc-delay-sign.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  libgdiplus0
BuildRequires:  mono-devel
BuildRequires:  strace
%if 0%{?fedora_version}
BuildRequires:  xorg-x11-fonts-truetype
%endif
%if 0%{?suse_version}
BuildRequires:  xorg-x11-fonts-core
%endif
Summary:        Unit-testing framework for all .NET languages
License:        Zlib
Group:          Development/Libraries/Mono

%description
NUnit is a unit testing framework for all .NET languages. It serves the
same purpose as JUnit does in the Java world. It supports test
categories, testing for exceptions and writing test results in plain
text or XML.

%package devel
Summary:        Development files for NUnit
Group:          Development/Languages/Mono
Requires:       nunit = %{version}

%description devel
This package contains development files for NUnit integration.

%prep
%setup -q -n nunitv2-%{version}
if [[ ! -z `2>/dev/null csc /version` ]]; then
%patch1 -p1
fi

%build
xbuild nunit.sln /t:Rebuild /p:Configuration=Debug

%install
mkdir -p "%{buildroot}%{_prefix}/lib/nunit"
cp -a bin/Debug/* "%{buildroot}%{_prefix}/lib/nunit"
mkdir -p "%{buildroot}%{_docdir}/%{name}"
cp -a license.txt "%{buildroot}%{_docdir}/%{name}/"
cp -a doc "%{buildroot}%{_docdir}/%{name}/"
cp -a samples "%{buildroot}%{_docdir}/%{name}/"

mkdir -p "%{buildroot}%{_bindir}"
echo '#!/bin/sh
exec /usr/bin/mono %{_prefix}/lib/nunit/nunit.exe "$@"' > "%{buildroot}%{_bindir}/nunit"
chmod +x "%{buildroot}%{_bindir}/nunit"

find "%{buildroot}%{_docdir}/%{name}" -type f -exec dos2unix {} \;

#manually sign delay-signed assemblies
find "%{buildroot}%{_prefix}" \( -name "*.dll" -o -name "*.exe" \) -print0 | while IFS= read -r -d $'\0' target; do
  sn -v "$target" || if [[ $? = 1 ]]; then
    echo "manually signing assembly: $target"
    sn -R "$target" nunit.snk
  fi
done

for i in nunit.core.dll nunit.core.interfaces.dll nunit.framework.dll nunit.util.dll lib/nunit-console-runner.dll lib/nunit-gui-runner.dll lib/nunit.uiexception.dll lib/nunit.uikit.dll framework/nunit.mocks.dll ; do
	gacutil -i %{buildroot}%{_prefix}/lib/nunit/$i -package nunit -root %{buildroot}%{_prefix}/lib
	rm -f %{buildroot}%{_prefix}/lib/nunit/$i
done

mkdir -p %{buildroot}%{_datadir}/pkgconfig

echo "prefix=%{_prefix}" > %{buildroot}%{_datadir}/pkgconfig/nunit.pc
echo "exec_prefix=\${prefix}" >> %{buildroot}%{_datadir}/pkgconfig/nunit.pc
echo "libdir=\${exec_prefix}/lib" >> %{buildroot}%{_datadir}/pkgconfig/nunit.pc
echo "pkglibdir=\${prefix}/lib/mono/nunit" >> %{buildroot}%{_datadir}/pkgconfig/nunit.pc
echo "Name: NUnit" >> %{buildroot}%{_datadir}/pkgconfig/nunit.pc
echo "Description: Testing framework for .NET" >> %{buildroot}%{_datadir}/pkgconfig/nunit.pc
echo "Version: %{version}" >> %{buildroot}%{_datadir}/pkgconfig/nunit.pc
echo "Libs: -r:\${pkglibdir}/nunit.core.dll -r:\${pkglibdir}/nunit.core.interfaces.dll -r:\${pkglibdir}/nunit.framework.dll -r:\${pkglibdir}/nunit.util.dll -r:\${pkglibdir}/nunit-console-runner.dll -r:\${pkglibdir}/nunit-gui-runner.dll -r:\${pkglibdir}/nunit.uiexception.dll -r:\${pkglibdir}/nunit.uikit.dll -r:\${pkglibdir}/nunit.mocks.dll" >> %{buildroot}%{_datadir}/pkgconfig/nunit.pc

%fdupes %{buildroot}%{_prefix}

%files
%defattr(-,root,root)
%{_prefix}/lib/nunit
%{_prefix}/lib/mono/nunit
%{_prefix}/lib/mono/gac/nunit*
%{_bindir}/nunit
%{_docdir}/nunit

%files devel
%defattr(-, root, root)
%{_datadir}/pkgconfig/nunit.pc

%changelog
