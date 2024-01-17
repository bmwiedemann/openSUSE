#
# spec file for package newtonsoft-json
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


%global libname Newtonsoft.Json

%bcond_with tests

Name:           newtonsoft-json
Version:        7.0.1
Release:        0
Summary:        JSON framework for C#
License:        MIT and BSD-3-Clause
Group:          Development/Libraries/Other
Url:            http://www.newtonsoft.com/json
Source:         https://github.com/JamesNK/%{libname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-MISSING-TAG
Patch0:         %{name}-sign.patch
# PATCH-MISSING-TAG
Patch1:         %{name}-tests-skip-samples.patch
# PATCH-FIX-OPENSUSE
Patch2:         csc-delay-sign.patch
BuildArch:      noarch
BuildRequires:  mono-devel
%if %{with tests}
# versioned binary enforces nunit version
BuildRequires:  nunit = 2.6.4
%endif

%description
%{libname} aka Json.NET is a JSON framework.

%package devel
Summary:        Development files for JSON.net
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}

%description devel
%{libname} aka Json.NET is a JSON framework.

%prep
%setup -qn%{libname}-%{version}

# sign the assembly to get a strong name, https://msdn.microsoft.com/en-us/library/xc31ft41.aspx
%patch0
sn -k myKey.snk # this make no sense, package is signed with Dynamic.snk keyfile
sed -i /InternalsVisibleTo/d Src/%{libname}/Properties/AssemblyInfo.cs

%if %{with tests}
# skip files with unmet dependencies (FSharp etc.), FIXME use nuget
%patch1
sed -i /DiscriminatedUnionConverterTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
sed -i /Serialization.DependencyInjectionTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
sed -i /Serialization.FSharpTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
sed -i /Serialization.ImmutableCollectionsTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
sed -i /TestObjects.Currency.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
sed -i /TestObjects.Shape.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
sed -i /Schema.JsonSchemaBuilderTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
sed -i /Schema.JsonSchemaNodeTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
sed -i /Utilities.StringUtilsTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.csproj
%endif

if [[ ! -z `2>/dev/null csc /version` ]]; then
%patch2 -p1
fi

%build
pushd Src/%{libname}
xbuild %{libname}.csproj

#manually sign delay-signed assemblies
find "bin" \( -name "*.dll" -o -name "*.exe" \) -print0 | while IFS= read -r -d $'\0' target; do
  sn -v "$target" || if [[ $? = 1 ]]; then
    echo "manually signing assembly: $target"
    sn -R "$target" Dynamic.snk
  fi
done

%install
mkdir -p %{buildroot}/%{_prefix}/lib/mono/gac/
gacutil -i Src/%{libname}/bin/Debug/Net45/%{libname}.dll -f -package %{name} -root %{buildroot}/%{_prefix}/lib
# pkgconfig
mkdir -p %{buildroot}/%{_datadir}/pkgconfig

echo "Name: %{libname}" > %{buildroot}/%{_datadir}/pkgconfig/%{name}.pc
echo "Description: %{summary}" >> %{buildroot}/%{_datadir}/pkgconfig/%{name}.pc
echo "Version: %{version}" >> %{buildroot}/%{_datadir}/pkgconfig/%{name}.pc
echo "Requires:" >> %{buildroot}/%{_datadir}/pkgconfig/%{name}.pc
echo "Libs: -r:%{_monodir}/%{name}/%{libname}.dll" >> %{buildroot}/%{_datadir}/pkgconfig/%{name}.pc
echo "Libraries=%{_monodir}/%{name}/%{libname}.dll" >> %{buildroot}/%{_datadir}/pkgconfig/%{name}.pc

%check
%if %{with tests}
pushd Src/%{libname}.Tests
# FIXME unmet dependencies prevent many tests (Linq, Utilities etc.)
xbuild %{libname}.Tests.csproj
nunit-console26 -labels -stoponerror bin\Debug\Net45\*.dll
#rm -r obj bin
%endif

%files
%defattr(-,root,root,-)
%doc *.md Doc/readme.txt Doc/license.txt
%{_prefix}/lib/mono/gac/%{libname}
%{_prefix}/lib/mono/%{name}/

%files devel
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/%{name}.pc

%changelog
