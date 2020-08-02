#
# spec file for package jnr-x86asm
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


%global commit_hash 1dead92
%global tag_hash 2a7fb9b
Name:           jnr-x86asm
Version:        1.0.2
Release:        0
Summary:        Pure-java port of asmjit
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz
Source1:        MANIFEST.MF
Patch0:         add-manifest.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Pure-java port of asmjit (http://code.google.com/p/asmjit/)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n jnr-%{name}-%{tag_hash}
%patch0
cp %{SOURCE1} .
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

%pom_xpath_set "pom:project/pom:properties/pom:maven.compiler.source" "1.6"
%pom_xpath_set "pom:project/pom:properties/pom:maven.compiler.target" "1.6"

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
