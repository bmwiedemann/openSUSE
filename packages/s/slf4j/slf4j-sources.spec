#
# spec file for package slf4j-sources
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2000-2009, JPackage Project
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


%global base_name slf4j
Name:           %{base_name}-sources
Version:        1.7.30
Release:        0
Summary:        SLF4J Source JARs
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:        MIT AND Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.slf4j.org/
Source0:        https://github.com/qos-ch/%{base_name}/archive/v_%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch2:         slf4j-commons-lang3.patch
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
SLF4J Source JARs.

%prep
%setup -q -n %{base_name}-v_%{version}
%patch2 -p1
find . -name "*.jar" | xargs rm
cp -p %{SOURCE1} APACHE-LICENSE

# Compat symlinks
%{mvn_file} ':{*}' %{base_name}/@1
%{mvn_package} :::sources:

%build
rm -f */src/main/resources/META-INF/MANIFEST.MF
for i in api ext jcl jdk14 log4j12 nop simple; do
  mkdir -p %{base_name}-${i}/target
  jar cf %{base_name}-${i}/target/%{base_name}-${i}-%{version}-sources.jar -C %{base_name}-${i}/src/main/java .
  jar uf %{base_name}-${i}/target/%{base_name}-${i}-%{version}-sources.jar -C %{base_name}-${i}/src/main/resources .
#  %{mvn_artifact} org.slf4j:%{base_name}-${i}:jar:sources:%{version} %{base_name}-${i}/target/%{base_name}-${i}-%{version}-sources.jar
done
for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  mkdir -p ${i}/target
  jar cf ${i}/target/${i}-%{version}-sources.jar -C ${i}/src/main/java .
  jar uf ${i}/target/${i}-%{version}-sources.jar -C ${i}/src/main/resources .
#  %{mvn_artifact} org.slf4j:${i}:jar:sources:%{version} ${i}/target/${i}-%{version}-sources.jar
done

%install
install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
for i in api ext jcl jdk14 log4j12 nop simple; do
  install -pm 0644 %{base_name}-${i}/target/%{base_name}-${i}-%{version}-sources.jar \
    %{buildroot}%{_javadir}/%{base_name}/%{base_name}-${i}-sources.jar
  %add_maven_depmap org.slf4j:%{base_name}-${i}:jar:sources:%{version} %{base_name}/%{base_name}-${i}-sources.jar
done
for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  install -pm 0644 ${i}/target/${i}-%{version}-sources.jar \
    %{buildroot}%{_javadir}/%{base_name}/${i}-sources.jar
  %add_maven_depmap org.slf4j:${i}:jar:sources:%{version} %{base_name}/${i}-sources.jar
done

%files -f .mfiles
%license LICENSE.txt APACHE-LICENSE

%changelog
