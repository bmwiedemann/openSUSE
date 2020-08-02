#
# spec file for package rhino
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


%define scm_version 1_7_7_1
Name:           rhino
Version:        1.7.7.1
Release:        0
Summary:        JavaScript for Java
License:        MPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.mozilla.org/rhino/
Source0:        https://github.com/mozilla/rhino/archive/Rhino%{scm_version}_RELEASE.tar.gz
Source1:        https://repo1.maven.org/maven2/org/mozilla/rhino/%{version}/rhino-%{version}.pom
Source2:        rhino.script
Source3:        rhino-debugger.script
Source4:        rhino-idswitch.script
Source5:        rhino-jsc.script
Patch0:         rhino-build.patch
# Add OSGi metadata from Eclipse Orbit project
Patch1:         rhino-addOrbitManifest.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-local
Requires:       javapackages-tools
Requires:       jline1
BuildArch:      noarch

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%package demo
Summary:        Examples for %{name}
Group:          Development/Libraries/Java

%description demo
Examples for %{name}

%prep
%setup -q -n %{name}-Rhino%{scm_version}_RELEASE
%patch0 -b .build
%patch1 -b .fixManifest
cp %{SOURCE1} pom.xml
%pom_remove_parent

# Fix manifest
sed -i -e '/^Class-Path:.*$/d' src/manifest

# Add jpp release info to version
sed -i -e 's|^implementation.version: Rhino .* release .* \${implementation.date}|implementation.version: Rhino %{version} release %{release} \${implementation.date}|' build.properties

%build
%{ant} \
    -Dtarget-jvm=6 -Dsource-level=6 \
    deepclean jar copy-all

pushd examples

export CLASSPATH=../build/%{name}%{version}/js.jar
SOURCEPATH=../build/%{name}%{version}/src
%javac -sourcepath ${SOURCEPATH} -source 6 -target 6 *.java
%jar cvf ../build/%{name}%{version}/%{name}-examples.jar *.class

popd

%install

# man page
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# jars
mkdir -p %{buildroot}%{_javadir}
cp -a build/%{name}%{version}/js.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/js.jar

# pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp -a pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a "rhino:js"

# scripts
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
install -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-debugger
install -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}-idswitch
install -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/%{name}-jsc

# examples
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a examples/* %{buildroot}%{_datadir}/%{name}
cp -a build/%{name}%{version}/%{name}-examples.jar %{buildroot}%{_javadir}/%{name}-examples.jar

find %{buildroot}%{_datadir}/%{name} -name '*.build' -delete

%files -f .mfiles
%license LICENSE.txt
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}-debugger
%attr(0755,root,root) %{_bindir}/%{name}-idswitch
%attr(0755,root,root) %{_bindir}/%{name}-jsc
%{_javadir}/js.jar
%{_javadir}/%{name}-examples.jar
%{_mandir}/man1/%{name}.1%{?ext_man}

%files demo
%{_datadir}/%{name}

%changelog
