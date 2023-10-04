#
# spec file for package xgboost
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


%global scala_short_version 2.10
%global scala_version %{scala_short_version}.7
%global artifactId xgboost4j
Name:           xgboost
Version:        0.90
Release:        0
Summary:        Gradient Boosting (GBDT, GBRT or GBM) Library
License:        Apache-2.0
URL:            https://github.com/dmlc/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        %{artifactId}-build.xml
Patch0:         xgboost-fix-big-endian.patch
BuildRequires:  akka
BuildRequires:  ant
BuildRequires:  ant-scala
BuildRequires:  apache-commons-logging
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  javapackages-local >= 6
BuildRequires:  kryo
BuildRequires:  objenesis
BuildRequires:  python3
BuildRequires:  scala
BuildRequires:  typesafe-config

%description
Scalable, Portable and Distributed Gradient Boosting (GBDT, GBRT or
GBM) Library, for Python, R, Java, Scala, C++ and more. Runs on
single machine, Hadoop, Spark, Flink and DataFlow

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
%{summary}

%prep
%setup -q
cp %{SOURCE1} jvm-packages/%{artifactId}/build.xml
%ifarch s390x ppc64
%patch0
%endif
pushd jvm-packages
%pom_xpath_set pom:project/pom:properties/pom:scala.version %{scala_version}
%pom_xpath_set pom:project/pom:properties/pom:scala.binary.version %{scala_short_version}
popd

%build
pushd jvm-packages
python3 create_jni.py
popd
pushd jvm-packages/%{artifactId}
mkdir -p lib
build-jar-repository -s lib akka kryo commons-logging scala typesafe-config objenesis/objenesis
%{ant} jar javadoc
popd

%install
pushd jvm-packages/%{artifactId}
install -dm 0755 %{buildroot}%{_jnidir}/%{name}
install -pm 0644 target/%{artifactId}-%{version}.jar %{buildroot}%{_jnidir}/%{name}/%{artifactId}.jar

install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifactId}.pom
%add_maven_depmap %{name}/%{artifactId}.pom %{name}/%{artifactId}.jar

install -dm 0755 %{buildroot}%{_javadocdir}
cp -r target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f jvm-packages/%{artifactId}/.mfiles
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
