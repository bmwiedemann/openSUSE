#
# spec file for package rhino
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define scm_version 1_7_15_1
Name:           rhino
Version:        1.7.15.1
Release:        0
Summary:        JavaScript for Java
License:        MPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.mozilla.org/rhino/
Source0:        https://github.com/mozilla/rhino/archive/Rhino%{scm_version}_Release.tar.gz
Source1:        https://repo1.maven.org/maven2/org/mozilla/rhino/%{version}/rhino-%{version}.pom
Source2:        https://repo1.maven.org/maven2/org/mozilla/rhino-engine/%{version}/rhino-engine-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/mozilla/rhino-runtime/%{version}/rhino-runtime-%{version}.pom
Source10:       %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
Requires:       javapackages-tools
BuildArch:      noarch

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%package engine
Summary:        Rhino Engine
Requires:       %{name} = %{version}

%description engine
Rhino Javascript JSR-223 Script Engine wrapper.

%package runtime
Summary:        Rhino Runtime

%description runtime
Rhino JavaScript runtime jar, excludes tools & JSR-223 Script Engine wrapper.

%package demo
Summary:        Examples for %{name}
Group:          Development/Libraries/Java

%description demo
Examples for %{name}

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-Rhino%{scm_version}_Release
cp %{SOURCE10} build.xml

%build
%{ant} jar javadoc

pushd examples

export CLASSPATH=../target/%{name}-%{version}.jar
SOURCEPATH=../src
javac -sourcepath ${SOURCEPATH} -source 8 -target 8 *.java
jar --create --verbose \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --file=../target/%{name}-examples-%{version}.jar *.class

popd

%install

# man page
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/js.jar
install -pm 0644 target/%{name}-engine-%{version}.jar %{buildroot}%{_javadir}/%{name}-engine.jar
install -pm 0644 target/%{name}-runtime-%{version}.jar %{buildroot}%{_javadir}/%{name}-runtime.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a "rhino:js"
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}-engine.pom
%add_maven_depmap %{name}-engine.pom %{name}-engine.jar -f engine
%{mvn_install_pom} %{SOURCE3} %{buildroot}%{_mavenpomdir}/%{name}-runtime.pom
%add_maven_depmap %{name}-runtime.pom %{name}-runtime.jar -f runtime

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

# scripts
%jpackage_script org.mozilla.javascript.tools.shell.Main "" "" rhino rhino true
%jpackage_script org.mozilla.javascript.tools.debugger.Main "" "" rhino rhino-debugger true
%jpackage_script org.mozilla.javascript.tools.jsc.Main "" "" rhino rhino-jsc true

# examples
install -dm 0755 %{buildroot}%{_datadir}/%{name}
cp -a examples/* %{buildroot}%{_datadir}/%{name}
install -pm 0644 target/%{name}-examples-%{version}.jar %{buildroot}%{_javadir}/%{name}-examples.jar
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}-debugger
%attr(0755,root,root) %{_bindir}/%{name}-jsc
%{_javadir}/js.jar
%{_javadir}/%{name}-examples.jar
%{_mandir}/man1/%{name}.1%{?ext_man}
%license LICENSE.txt NOTICE.txt NOTICE-tools.txt
%doc README.md CODE_OF_CONDUCT.md RELEASE-NOTES.md

%files engine -f .mfiles-engine
%license LICENSE.txt
%doc README.md CODE_OF_CONDUCT.md RELEASE-NOTES.md

%files runtime -f .mfiles-runtime
%license LICENSE.txt NOTICE.txt
%doc README.md CODE_OF_CONDUCT.md RELEASE-NOTES.md

%files demo
%{_datadir}/%{name}

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
