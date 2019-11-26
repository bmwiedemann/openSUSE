#
# spec file for package ezmorph
#
# Copyright (c) 2019 SUSE LLC
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


Name:           ezmorph
Version:        1.0.6
Release:        0
Summary:        Object transformation library for Java
License:        Apache-2.0
URL:            https://sourceforge.net/projects/ezmorph/
# cvs -d:pserver:anonymous@ezmorph.cvs.sourceforge.net:/cvsroot/ezmorph login
# cvs -z3 -d:pserver:anonymous@ezmorph.cvs.sourceforge.net:/cvsroot/ezmorph co -r REL_1_0_6 -d ezmorph-1.0.6 -P ezmorph
# tar cJf ezmorph-1.0.6.tar.xz --exclude CVS ezmorph-1.0.6
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:12)
BuildArch:      noarch

%description
EZMorph is simple java library for transforming an Object to another
Object. It supports transformations for primitives and Objects and
multidimensional arrays.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

cp -p %{SOURCE1} LICENSE.txt

%pom_change_dep :log4j ::12

%pom_xpath_remove "pom:plugins"

%{mvn_file} : %{name}

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
