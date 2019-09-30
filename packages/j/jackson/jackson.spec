#
# spec file for package jackson
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


Name:           jackson
Version:        1.9.13
Release:        0
Summary:        Jackson Java JSON-processor
License:        Apache-2.0 OR LGPL-2.0-only
Group:          Development/Libraries/Java
URL:            http://jackson.codehaus.org
# No upstream tag for this version, check out using source service
# from revision 3225405abf68a318b6f21e9ccf7d5c00e80e4df4
Source0:        jackson-1.9.13.tar.xz
# Build plain jar files instead of OSGi bundles in order to avoid depending on
# BND:
Patch0:         %{name}-build-plain-jars-instead-of-osgi-bundles.patch
# Don't require a repackaged version of ASM:
Patch1:         %{name}-dont-require-repackaged-asm.patch
# Don't bundle the ASM classes:
Patch2:         %{name}-dont-bundle-asm.patch
# Fix javadoc build
Patch4:         %{name}-1.9.11-javadoc.patch
Patch5:         jackson-sourcetarget.patch
Patch6:         jackson-module.patch
BuildRequires:  ant >= 1.8.2
BuildRequires:  asm3 >= 3.3
BuildRequires:  cglib >= 2.2
BuildRequires:  fdupes
BuildRequires:  groovy18 >= 1.8.5
BuildRequires:  javapackages-local
BuildRequires:  joda-time >= 1.6.2
BuildRequires:  jsr-311 >= 1.1.1
BuildRequires:  stax2-api >= 3.1.1
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
Requires:       asm3 >= 3.3
Requires:       joda-time >= 1.6.2
Requires:       jsr-311 >= 1.1.1
Requires:       stax2-api >= 3.1.1
BuildArch:      noarch

%description
JSON processor (JSON parser + JSON generator) written in Java. Beyond basic
JSON reading/writing (parsing, generating), it also offers full node-based Tree
Model, as well as full OJM (Object/Json Mapper) data binding functionality.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4
%patch5 -p1
%patch6 -p1

# Remove all the binary jar files, as the packaging policies
# forbids using them:
find . -type f -name '*.jar' -exec rm {} \;

# Remove some tests to avoid additional dependencies:
rm src/test/org/codehaus/jackson/map/interop/TestHibernate.java
rm src/perf/perf/TestJsonPerf.java
rm src/test/org/codehaus/jackson/map/interop/TestGoogleCollections.java

# Make symbolic links to the jar files expected by the ant build
# scripts:
ln -s $(build-classpath joda-time) lib/ext/joda-time.jar
mkdir -p lib/xml
ln -s $(build-classpath stax2-api) lib/xml/sta2-api.jar
ln -s $(build-classpath jsr-311) lib/jaxrs/jsr-311.jar
ln -s $(build-classpath asm3/asm) lib/ext/asm/asm.jar
ln -s $(build-classpath asm3/asm) lib/repackaged/jackson-asm.jar
ln -s $(build-classpath cglib/cglib) lib/ext/cglib/cglib-nodep.jar
ln -s $(build-classpath groovy18-1.8) lib/ext/groovy/groovy.jar
ln -s $(build-classpath junit) lib/junit/junit.jar

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," \
 release-notes/lgpl/LGPL2.1

iconv -f UTF-8 -t ASCII//TRANSLIT -o tmp src/test/org/codehaus/jackson/jaxrs/TestUntouchables.java \
 && mv tmp src/test/org/codehaus/jackson/jaxrs/TestUntouchables.java

%build

ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 dist

%install

# For each jar file install it and its pom:
jars='
jackson-core-asl
jackson-mapper-asl
jackson-xc
jackson-smile
jackson-mrbean
jackson-jaxrs
'
for jar in ${jars}
do
  %{mvn_artifact} dist/${jar}-%{version}.pom dist/${jar}-%{version}.jar
done

%mvn_install -J dist/javadoc/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.txt
%doc release-notes

%files javadoc -f .mfiles-javadoc
%doc README.txt
%doc release-notes

%changelog
