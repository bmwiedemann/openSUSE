#
# spec file for package extra166y
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


Name:           extra166y
Version:        1.7.0
Release:        0
Summary:        Concurrency JSR-166 - Collections supporting parallel operations
License:        SUSE-Public-Domain
Group:          Development/Libraries/Java
URL:            http://gee.cs.oswego.edu/dl/concurrency-interest
# generate-tarball.spec
Source0:        jsr166-%{version}.tar.xz
Source1:        http://central.maven.org/maven2/org/codehaus/jsr166-mirror/%{name}/%{version}/%{name}-%{version}.pom
Source2:        extra166y-OSGi.bnd
Source100:      generate-tarball.sh
Patch0:         extra166y-osgi-manifest.patch
BuildRequires:  ant
BuildRequires:  aqute-bnd >= 3.2.0-2
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
Implementation of Java collections supporting parallel operations using
Fork-Join concurrent framework provided by JSR-166.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jsr166
%patch0

# Use JVM jsr166
for s in $(find . -name "*.java");do
  sed -i "s|jsr166y.|java.util.concurrent.|" ${s}
done
sed -i '/configure-compiler, jsr166ycompile/d' build.xml

sed -i '/<compilerarg line="${build.args}"/d' build.xml

sed -i '/ootclasspath/d' build.xml

cp -p %{SOURCE2} extra166y.bnd
sed -i "s|@VERSION@|%{version}|" extra166y.bnd

rm -f src/test/extra166y/ParallelArrayAsListTest.java

%build

%{mvn_file} org.codehaus.jsr166-mirror:%{name} %{name}
export CLASSPATH=$(build-classpath junit)
%ant \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
  extra166yjar extra166ydist-docs
%{mvn_artifact} %{SOURCE1} build/%{name}lib/%{name}.jar

%install
%mvn_install -J dist/%{name}docs
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc src/main/intro.html src/main/readme

%files javadoc -f .mfiles-javadoc
%doc src/main/intro.html src/main/readme

%changelog
