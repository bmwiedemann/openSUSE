#
# spec file for package paradise
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


%global bootstrap_version 2.0.0~M5
%global scala_version 2.10.7
%global scala_short_version 2.10
Name:           paradise
Version:        2.1.0
Release:        0
Summary:        Macros for Scala
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/scalamacros/paradise
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-%{bootstrap_version}.tar.xz
Source100:      http://central.maven.org/maven2/org/scalamacros/%{name}_%{scala_version}/%{version}/%{name}_%{scala_version}-%{version}.pom
Source101:      http://central.maven.org/maven2/org/scalamacros/quasiquotes_%{scala_short_version}/%{version}/quasiquotes_%{scala_short_version}-%{version}.pom
BuildRequires:  javapackages-local xmvn-resolve xmvn-install
BuildRequires:  scala

%description
Empowers production Scala compiler with latest macro developments

%package -n quasiquotes
Summary: Notation to manipulate Scala syntax trees

%description -n quasiquotes
Quasiquotes are a notation that allows to manipulate Scala syntax trees.

%prep
%setup -q -a1

%mvn_package :quasiquotes{*} quasiquotes

%mvn_file :%{name}_%{scala_version} %{name}/%{name}_%{scala_version} %{name}/%{name}_%{scala_short_version}

%build
# First build a bootstrap paradise scala plugin with the milestone that does not have circular dependencies
pushd %{name}-%{bootstrap_version}/plugin
  mkdir -p target/classes
  scalac -d target/classes \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -nobootcp \
%endif
    -classpath $(build-classpath scala/scala-library scala/scala-reflect):target/classes \
	$(find src/main/scala -name \*.scala | xargs)
  find src/main/scala -name scalac-plugin.xml -exec cp {} target/classes/ \;
  jar cf ../../boot-plug.jar -C target/classes .
popd

# Now we use this plugin to build the quasiquotes and plugin  
pushd quasiquotes
  mkdir -p target/classes
  javac -d target/classes -source 6 -target 6 \
    -cp $(build-classpath scala/scala-library scala/scala-reflect) \
    $(find src/main/java -name \*.java | xargs)
  scalac -d target/classes -Xplugin:../boot-plug.jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -nobootcp \
%endif
    -classpath $(build-classpath scala/scala-library scala/scala-reflect):target/classes \
	$(find src/main/scala -name \*.scala | xargs)
  jar cf ../quasiquotes.jar -C target/classes .
popd
%mvn_artifact %{SOURCE101} quasiquotes.jar
pushd plugin
  mkdir -p target/classes
  scalac -d target/classes \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -nobootcp \
%endif
    -classpath $(build-classpath scala/scala-library scala/scala-reflect):target/classes:../quasiquotes.jar \
	$(find src/main/scala -name \*.scala | xargs)
  find src/main/scala -name scalac-plugin.xml -exec cp {} target/classes/ \;
  jar cf ../plugin.jar -C target/classes .
popd

# Due to how the scala plugins work, we need to create an uberjar
jar uf plugin.jar -C quasiquotes/target/classes .
%mvn_artifact %{SOURCE100} plugin.jar

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md
%doc README.md

%files -n quasiquotes -f .mfiles-quasiquotes

%changelog
