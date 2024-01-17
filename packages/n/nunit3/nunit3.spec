#
# spec file for package nunit3
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


Name:           nunit3
Version:        3.7.1
Release:        0
Summary:        Unit-testing framework for all .NET languages
License:        MIT
Group:          Development/Languages/Other
URL:            http://www.nunit.org/
Source0:        https://github.com/nunit/nunit/archive/%{version}.tar.gz
Source1:        nunit.pc
Source2:        nunitlite-runner.sh
BuildRequires:  mono-devel
BuildArch:      noarch

%description
NUnit is a unit testing framework for all .NET languages. It serves the
same purpose as JUnit does in the Java world. It supports test
categories, testing for exceptions and writing test results in plain
text or XML.

%package devel
Summary:        Development files for NUnit
Group:          Development/Languages/Other
Requires:       nunit3 = %{version}

%description devel
This package contains development files for NUnit integration.

%prep
%setup -q -n nunit-%{version}

# Remove prebuilt binaries
find . -name "*.dll" -print -delete

%build
xbuild /property:Configuration=Release src/NUnitFramework/framework/nunit.framework-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/nunitlite/nunitlite-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/nunitlite-runner/nunitlite-runner-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/mock-assembly/mock-assembly-4.5.csproj

xbuild /property:Configuration=Release src/NUnitFramework/slow-tests/slow-nunit-tests-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/testdata/nunit.testdata-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/tests/nunit.framework.tests-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/nunitlite.tests/nunitlite.tests-4.5.csproj

%install
mkdir -p %{buildroot}%{_datadir}/pkgconfig
install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pkgconfig/
mkdir -p %{buildroot}%{_bindir}
install -m0755 %{SOURCE2} %{buildroot}%{_bindir}/nunitlite-runner
mkdir -p %{buildroot}%{_prefix}/lib/mono/nunit3
install -m0644 src/NUnitFramework/nunitlite-runner/App.config %{buildroot}%{_prefix}/lib/mono/nunit3/nunitlite-runner.exe.config
find bin -name \*.dll -exec install \-m0755 "{}" "%{buildroot}%{_prefix}/lib/mono/nunit3/" \;
find bin -name \*.exe -exec install \-m0755 "{}" "%{buildroot}%{_prefix}/lib/mono/nunit3/" \;

%files
%license LICENSE.txt
%doc README.md CHANGES.md NOTICES.txt
%{_bindir}/nunitlite-runner
%{_prefix}/lib/mono/nunit3/

%files devel
%doc CONTRIBUTING.md
%{_datadir}/pkgconfig/nunit.pc

%changelog
