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


%global scala_short_version 2.13
%global scala_version %{scala_short_version}.12
%global groupId ml.dmlc
%global artifactId xgboost4j
Name:           xgboost
Version:        2.0.0
Release:        0
Summary:        Gradient Boosting (GBDT, GBRT or GBM) Library
License:        Apache-2.0
URL:            https://github.com/dmlc/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        %{artifactId}-build.xml
Patch0:         xgboost-fix-big-endian.patch
Patch1:         no-hadoop.patch
Patch2:         xgboost-2.0.0-python34.patch
Patch3:         xgboost-2.0.0-cmake.patch
BuildRequires:  akka
BuildRequires:  ant
BuildRequires:  apache-commons-logging
BuildRequires:  cmake >= 3.5
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  kryo
BuildRequires:  objenesis
BuildRequires:  python3
BuildRequires:  scala
BuildRequires:  scala-ant
BuildRequires:  typesafe-config
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc8-c++ >= 8.1
%else
BuildRequires:  gcc-c++
%endif

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%pom_xpath_set pom:project/pom:properties/pom:scala.version %{scala_version} jvm-packages
%pom_xpath_set pom:project/pom:properties/pom:scala.binary.version %{scala_short_version} jvm-packages
%pom_remove_dep ":scala-collection-compat_\${scala.binary.version}" jvm-packages/%{artifactId}

%{mvn_alias} :{*}_{*} :@1
%{mvn_package} :xgboost-jvm __noinstall

%build
pushd jvm-packages
%if 0%{?suse_version} <= 1500
export CC=gcc-8
export CXX=g++-8
%endif
%ifarch x86_64 aarch64
python3 create_jni.py
%endif
popd
pushd jvm-packages/%{artifactId}
mkdir -p lib
build-jar-repository -s lib akka kryo commons-logging scala typesafe-config objenesis/objenesis
%{ant} jar javadoc
popd

%install
install -dm 0755 %{buildroot}%{_jnidir}/%{name}
install -pm 0644 jvm-packages/%{artifactId}/target/%{artifactId}-%{version}.jar %{buildroot}%{_jnidir}/%{name}/%{artifactId}_%{scala_short_version}.jar

install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} jvm-packages/%{artifactId}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifactId}_%{scala_short_version}.pom
%add_maven_depmap %{name}/%{artifactId}_%{scala_short_version}.pom %{name}/%{artifactId}_%{scala_short_version}.jar -a %{groupId}:%{artifactId}

install -dm 0755 %{buildroot}%{_javadocdir}
cp -r jvm-packages/%{artifactId}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
