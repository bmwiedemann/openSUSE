#
# spec file for package apache-commons-logging
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2000-2007, JPackage Project
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


%define base_name  logging
%define short_name commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.3.5
Release:        0
Summary:        Apache Commons Logging
License:        Apache-2.0
URL:            https://commons.apache.org/%{base_name}
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz.asc
Source2:        %{name}.keyring
Source5:        build.xml
Source6:        build.properties
Patch0:         commons-logging-1.3.3-dependencies.patch
BuildRequires:  ant
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  reload4j
Requires:       java >= 1.8
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}
BuildArch:      noarch

%description
The commons-logging package provides a simple, component oriented
interface (org.apache.commons.logging.Log) together with wrappers for
logging systems. The user can choose at runtime which system they want
to use. In addition, a small number of basic implementations are
provided to allow users to use the package standalone.
commons-logging was heavily influenced by Avalon's Logkit and Log4J. The
commons-logging abstraction is meant to minimize the differences between
the two, and to allow a developer to not tie himself to a particular
logging implementation.

%prep
%autosetup -p1 -n %{short_name}-%{version}-src

cp %{SOURCE5} build.xml
cp %{SOURCE6} build.properties

sed -i 's/\r//' RELEASE-NOTES.txt LICENSE.txt

%pom_remove_parent .

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

export CLASSPATH=$(build-classpath \
                   plexus/ \
                  ):target/classes:target/test-classes
ant \
  -Dmaven.mode.offline=true -lib %{_javadir} \
  -Dlog4j12.jar=$(find-jar reload4j/reload4j) -Dservletapi.jar=$(find-jar glassfish-servlet-api) \
  dist

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 target/%{short_name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
install -p -m 644 target/%{short_name}-adapters-%{version}.jar %{buildroot}%{_javadir}/%{name}-adapters.jar

pushd %{buildroot}%{_javadir}
for jar in %{name}*; do
    ln -sf ${jar} `echo $jar| sed "s|apache-||g"`
done
popd

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}/%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "org.apache.commons:%{short_name}","apache:%{short_name}"
%add_maven_depmap %{short_name}:%{short_name}::api:%{version} %{short_name}-api.jar -a "%{short_name}:%{short_name}-api","org.apache.commons:%{short_name}-api","apache:%{short_name}-api"
%add_maven_depmap %{short_name}:%{short_name}::adapters:%{version} %{short_name}-adapters.jar -a "%{short_name}:%{short_name}-adapters","org.apache.commons:%{short_name}-adapters","apache:%{short_name}-adapters"

%files -f .mfiles
%{_javadir}/%{name}*.jar
%license LICENSE.txt
%doc PROPOSAL.html RELEASE-NOTES.txt NOTICE.txt

%changelog
