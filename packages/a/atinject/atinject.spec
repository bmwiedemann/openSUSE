#
# spec file for package atinject
#
# Copyright (c) 2022 SUSE LLC
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


Name:           atinject
Version:        1+20160610git1f74ea7
Release:        0
Summary:        Dependency injection specification for Java (JSR-330)
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://javax-inject.github.io/javax-inject/
Source0:        %{name}-%{version}.tar.xz
# These manifests based on the ones shipped by eclipse.org
Source1:        MANIFEST.MF
Source2:        MANIFEST-TCK.MF
Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         atinject-javadoc.patch
BuildRequires:  fdupes
BuildRequires:  java-devel > 1.8
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  xz
BuildArch:      noarch

%description
This package specifies a means for obtaining objects in such a way as
to maximize reusability, testability and maintainability compared to
traditional approaches such as constructors, factories, and service
locators (e.g., JNDI). This process, known as dependency injection, is
beneficial to most nontrivial applications.

%package        tck
Summary:        TCK for testing %{name} compatibility with JSR-330
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}
Requires:       junit

%description    tck
%{summary}.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
cp %{SOURCE3} LICENSE

# Fix dep in TCK pom
sed -i -e 's/pom\.groupId/project.groupId/' tck-pom.xml

%build
rm -rf build
mkdir -p build/classes
mkdir -p build/tck
mkdir -p build/dist
mkdir -p build/tck/classes
mkdir -p build/tck/dist

# Compile classes.
javac -source 8 -target 8 -g -d build/classes `find src -name \*.java`
javac -source 8 -target 8 -g -classpath build/classes:$(build-classpath junit) -d build/tck/classes \
	`find tck -name \*.java`

# Generate Javadocs.
FOOTER="<font size='-1'>Copyright (C) 2009 <a href='https://github.com/javax-inject/javax-inject'>\
The JSR-330 Expert Group</a>. \
Licensed under the <a href='http://www.apache.org/licenses/LICENSE-2.0'>Apache \
License</a>, Version 2.0.</font>"
javadoc -source 8 -protected -bottom "${FOOTER}" \
    -header "<font color='red'><b>This is a DRAFT specification.</b></font>" \
	-sourcepath src -d build/javadoc javax.inject
javadoc -source 8 -classpath build/classes:lib/junit.jar -protected -bottom "$FOOTER" \
	-sourcepath tck -d build/javadoc/tck org.atinject.tck \
	org.atinject.tck.auto org.atinject.tck.auto.accessories

# Generate jars.
jar cmf %{SOURCE1} build/dist/javax.inject.jar -C build/classes .
jar cmf %{SOURCE2} build/tck/dist/javax.inject-tck.jar -C build/tck/classes .

%install
# jars
install -dm 755 %{buildroot}%{_javadir}/javax.inject
install -m 0644 build/dist/javax.inject.jar %{buildroot}%{_javadir}/%{name}.jar
(cd %{buildroot}%{_javadir}/javax.inject && ln -s ../%{name}.jar .)
install -m 0644 build/tck/dist/javax.inject-tck.jar %{buildroot}%{_javadir}/%{name}-tck.jar

# poms
install -dm 755 %{buildroot}%{_mavenpomdir}
install -m 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
install -m 0644 tck-pom.xml %{buildroot}%{_mavenpomdir}/%{name}-tck.pom
%add_maven_depmap %{name}.pom %{name}.jar -a "jakarta.inject:jakarta.inject-api"
%add_maven_depmap %{name}-tck.pom %{name}-tck.jar -f tck

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr  build/javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%license LICENSE
%{_javadir}/javax.inject

%files tck -f .mfiles-tck

%files javadoc
%{_javadocdir}/%{name}

%changelog
