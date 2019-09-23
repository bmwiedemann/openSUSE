#
# spec file for package stringtemplate
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           stringtemplate
Version:        3.2.1
Release:        0
Summary:        A Java template engine
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.stringtemplate.org/
Source0:        http://www.stringtemplate.org/download/stringtemplate-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0:         stringtemplate-3.1-build-junit.patch
Patch1:         stringtemplate-3.2.1-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  ant-antlr
BuildRequires:  ant-junit
BuildRequires:  antlr
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
Requires:       mvn(antlr:antlr)
BuildArch:      noarch

%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
Requires:       java-javadoc

%description    javadoc
API documentation for package %{name}.

%prep
%setup -q
%patch0
%patch1 -p1

%build
rm -rf lib target
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    jar
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
	-Dpackages= -Djavadocs.additionalparam= \
	javadocs

%install
install -D build/stringtemplate.jar %{buildroot}%{_datadir}/java/stringtemplate.jar
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pR docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom stringtemplate.jar

%files -f .mfiles
%license LICENSE.txt
%doc README.txt

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
