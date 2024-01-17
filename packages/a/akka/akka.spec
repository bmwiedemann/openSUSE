#
# spec file for package akka
#
# Copyright (c) 2023 SUSE LLC
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


%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global scala_short_version 2.13
Name:           akka
Version:        2.8.5
Release:        0
Summary:        Scalable real-time transaction processing
License:        Apache-2.0
URL:            https://akka.io/
Source0:        %{name}-%{version}.tar.xz
# Default use sbt
Source1:        akka-build.xml
# Build only these sub-modules, cause: unavailable build deps
# TODO  akka-camel akka-contrib akka-durable-mailboxes akka-persistence akka-samples akka-zeromq
Source2:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-actor_%{scala_short_version}/%{namedversion}/akka-actor_%{scala_short_version}-%{namedversion}.pom
Source3:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-cluster_%{scala_short_version}/%{namedversion}/akka-cluster_%{scala_short_version}-%{namedversion}.pom
Source4:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-remote_%{scala_short_version}/%{namedversion}/akka-remote_%{scala_short_version}-%{namedversion}.pom
Source5:        https://repo1.maven.org/maven2/com/typesafe/akka/akka-slf4j_%{scala_short_version}/%{namedversion}/akka-slf4j_%{scala_short_version}-%{namedversion}.pom
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  scala-ant
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
# typesafe-config
BuildRequires:  mvn(com.typesafe:config)
BuildRequires:  mvn(io.netty:netty)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.scala-lang:scala-compiler)
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-stm:scala-stm_%{scala_short_version})
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.uncommons.maths:uncommons-maths)
# requires for akka-remote
BuildRequires:  protobuf-devel scala-java8-compat
BuildRequires:  sbt-boilerplate
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Akka is a toolkit and run-time for building highly concurrent,
distributed, and fault tolerant event-driven applications on
the JVM.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

cp -p %{SOURCE1} build.xml
sed -i "s|@VERSION@|%{namedversion}|" build.xml

rm -rf */src/main/scala-3 */src/main/scala-2.12

# spurious-executable-perm
chmod 644 LICENSE

%build

pushd akka-actor
mkdir -p src/main/gen-scala
for i in $(find src/main/boilerplate -name \*.scala.template); do
   sbt-boilerplate $i >src/main/gen-scala/$(basename $i .template);
done
cat <<EOF >src/main/gen-scala/Version.scala
package akka

object Version {
  val current: String = "%{vesion}"
}
EOF
echo "akka.version = \"%{version}\"" >src/main/resources/version.conf

mkdir -p target/classes
scalac -nobootcp -d target/classes -cp $(build-classpath scala typesafe-config) -target:8 \
    $(find src/main -name \*.scala -o -name \*.java | xargs)
javac -d target/classes -cp $(build-classpath scala typesafe-config):target/classes \
    -source 8 -target 8 -encoding utf-8 \
    $(find src/main -name \*.java | xargs)
jar -cf target/%{name}-actor.jar -C target/classes . -C src/main/resources .
mkdir -p target/apidocs
scaladoc -nobootcp -d target/apidocs -cp $(build-classpath scala typesafe-config) -target:8 \
    $(find src/main -name \*.scala -o -name \*.java | xargs)
popd

%{mvn_artifact} %{SOURCE2} akka-actor/target/%{name}-actor.jar

%install
%mvn_install -J akka-actor/target/apidocs

%files -f .mfiles
%license LICENSE
%doc CONTRIBUTING.md README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
