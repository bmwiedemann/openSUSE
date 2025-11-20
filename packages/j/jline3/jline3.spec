#
# spec file for package jline3
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global desc JLine is a Java library for handling console input. It is similar in\
functionality to BSD editline and GNU readline but with additional features\
that bring it in par with ZSH line editor. People familiar with the\
readline/editline capabilities for modern shells (such as bash and tcsh) will\
find most of the command editing features of JLine to be familiar.\
\
JLine 3.x is an evolution of JLine 2.x.
# Requires java >= 22
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 22}%{!?pkg_vcmp:0}
%bcond_without ffm
%else
%bcond_with ffm
%endif
%bcond_with ssh
Name:           jline3
Version:        3.30.6
Release:        0
Summary:        Java library for handling console input
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/jline/jline3
Source0:        %{url}/archive/refs/tags/jline-%{version}.tar.gz
Source1:        %{name}-build.tar.xz
Source100:      Load-native-library-system-wide-place.patch.in
Patch0:         0001-Remove-optional-dependency-on-universalchardet.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jansi
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  jna
BuildRequires:  jsr-305
%if %{with ssh}
BuildRequires:  apache-sshd
BuildRequires:  slf4j
%endif
%if %{with ffm}
BuildRequires:  java-devel >= 22
BuildConflicts: java <= 21
BuildConflicts: java-devel <= 21
BuildConflicts: java-headless <= 21
%endif

%description
JLine is a Java library for handling console input. It is similar in
functionality to BSD editline and GNU readline but with additional features
that bring it in par with ZSH line editor. People familiar with the
readline/editline capabilities for modern shells (such as bash and tcsh) will
find most of the command editing features of JLine to be familiar.

JLine 3.x is an evolution of JLine 2.x.

%package builtins
Summary:        JLine Builtins
BuildArch:      noarch

%description builtins
%{desc}

This package contains several high level tools: less pager, nano editor, screen
multiplexer, etc…

%package console
Summary:        JLine Console
BuildArch:      noarch

%description console
%{desc}

This package contains the command registry, object printer and widget
implementations.

%package console-ui
Summary:        JLine Console UI
BuildArch:      noarch

%description console-ui
%{desc}

This package contains the command registry, object printer and widget
implementations.

%package curses
Summary:        JLine Curses
BuildArch:      noarch

%description curses
%{desc}

%package jansi
Summary:        Jansi Bundle

%description jansi
%{desc}

%package jansi-core
Summary:        Jansi Core
BuildArch:      noarch

%description jansi-core
%{desc}

%package native
Summary:        JLine Native Library

%description native
%{desc}

This package contains the native library.

%package reader
Summary:        JLine Reader
BuildArch:      noarch

%description reader
%{desc}

This package contains the line reader (including completion, history, etc…).

%package remote-telnet
Summary:        JLine Remote Telnet
BuildArch:      noarch

%description remote-telnet
%{desc}

This package contains the helpers for using jline over telnet (including
a telnet server implementation).

%if %{with ssh}
%package remote-ssh
Summary:        JLine Remote SSH
Recommends:     mvn(org.apache.sshd:scp-core)
Recommends:     mvn(org.apache.sshd:sftp-core)
Recommends:     mvn(org.apache.sshd:sshd-core)
BuildArch:      noarch

%description remote-ssh
%{desc}

This package contains the helpers for using jline with Mina SSHD.
%endif

%if %{with ffm}
%package terminal-ffm
Summary:        JLine FFM Terminal
BuildArch:      noarch

%description terminal-ffm
%{desc}
%endif

%package style
Summary:        JLine Style
BuildArch:      noarch

%description style
%{desc}

This package contains the styling api.

%package terminal-jna
Summary:        JLine JNA Terminal
BuildArch:      noarch

%description terminal-jna
%{desc}

This package contains terminal implementations leveraging the JNA library.

%package terminal-jni
Summary:        JLine JNI Terminal
BuildArch:      noarch

%description terminal-jni
%{desc}

This package contains terminal implementations leveraging the JNI library.

%package terminal
Summary:        JLine Terminal
BuildArch:      noarch

%description terminal
%{desc}

This package contains the Terminal api and implementations.

%package terminal-jansi
Summary:        JLine JANSI Terminal
BuildArch:      noarch

%description terminal-jansi
%{desc}

This package contains terminal implementations leveraging the Jansi library.

%package javadoc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-jline-%{version} -p1 -a1

sed "s;@SYSTEMLIBRARYPATH@;%{_libdir}/%{name}/;g" < %{SOURCE100} | patch -p1

cp -p console-ui/LICENSE.txt LICENSE-APACHE.txt

# Remove prebuilt native objects
rm -r native/src/main/resources/org/jline/nativ/*/

# -Werror is considered harmful for downstream packaging
sed -i /-Werror/d $(find -name pom.xml)

# Optional dependency on juniversalchardet was removed via a patch
%pom_remove_dep -r :juniversalchardet . jline

%if %{without ffm}
%pom_disable_module terminal-ffm
%pom_remove_dep :jline-terminal-ffm jline
%pom_xpath_remove "pom:executions/pom:execution[pom:id='jdk22']" jline
%endif

# Disable unwanted modules
%pom_disable_module groovy
%pom_disable_module demo
%pom_disable_module graal
%if %{without ssh}
%pom_disable_module remote-ssh
%endif

# Unnecessary plugins for an rpm build
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :spotless-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :native-image-maven-plugin
%pom_remove_plugin :maven-source-plugin

# There is no need to re-generate jni-config.json for GraalVM
# as is already present under native/src/main/resources/
%pom_remove_plugin :exec-maven-plugin native
%pom_remove_dep :picocli-codegen native

# Superfluos dependency
%pom_remove_dep org.apache.sshd: remote-telnet
%if %{without ssh}
%pom_remove_dep org.apache.sshd: jline
%endif

%pom_remove_plugin :maven-dependency-plugin console-ui jansi jline
%pom_remove_plugin :build-helper-maven-plugin jansi jline
# This replaces the action of the two removed plugins
mkdir -p jline/src/main/java
mkdir -p jline/src/main/resources
for module in \
    jansi-core \
    builtins \
    console \
    native \
    reader \
%if %{with ssh}
    remote-ssh \
%endif
    remote-telnet \
    style \
    terminal \
%if %{with ffm}
    terminal-ffm \
%endif
    terminal-jansi \
    terminal-jna \
    terminal-jni; do
  if [ -d ${module}/src/main/java ]; then
    cp -r ${module}/src/main/java/* jline/src/main/java/
  fi
  if [ -d ${module}/src/main/resources ]; then
    cp -r ${module}/src/main/resources/* jline/src/main/resources/
  fi
done

mkdir -p jansi/src/main/java
mkdir -p jansi/src/main/resources
for module in \
    jansi-core \
    native \
    terminal \
    terminal-jni; do
  if [ -d ${module}/src/main/java ]; then
    cp -r ${module}/src/main/java/* jansi/src/main/java/
  fi
  if [ -d ${module}/src/main/resources ]; then
    cp -r ${module}/src/main/resources/* jansi/src/main/resources/
  fi
done

%build
mkdir -p lib
build-jar-repository -s lib \
    jansi/jansi \
    jna/jna \
    jsr-305
%if %{with ssh}
  build-jar-repository -s lib \
    apache-sshd/sshd-common \
    apache-sshd/sshd-core \
    apache-sshd/sshd-scp \
    apache-sshd/sshd-sftp \
    slf4j/api
%endif

# Build a native object
gcc -Wall %{?build_cflags} %{?optflags} -fPIC -fvisibility=hidden -shared \
  -I native/src/main/native -I %{_jvmdir}/java/include \
  -I %{_jvmdir}/java/include/linux %{?build_ldflags} \
  -o libjlinenative.so native/src/main/native/{jlinenative,clibrary}.c

ant package javadoc
%if %{with ssh}
  ant -f remote-ssh package javadoc
%endif
%if %{with ffm}
  ant -f terminal-ffm package javadoc
%endif

%install
# jars
install -dm 0755 %{buildroot}%{_jnidir}/%{name}
install -pm 0644 jansi/target/jansi-%{version}.jar %{buildroot}%{_jnidir}/%{name}/jansi.jar
install -pm 0644 jline/target/jline-%{version}.jar %{buildroot}%{_jnidir}/%{name}/jline.jar
install -pm 0644 native/target/jline-native-%{version}.jar %{buildroot}%{_jnidir}/%{name}/jline-native.jar

install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 jansi-core/target/jansi-core-%{version}.jar %{buildroot}%{_javadir}/%{name}/jansi-core.jar
for i in \
  builtins \
  console \
  console-ui \
  curses reader \
%if %{with ssh}
  remote-ssh \
%endif
  remote-telnet \
  style \
  terminal \
%if %{with ffm}
  terminal-ffm \
%endif
  terminal-jansi \
  terminal-jna \
  terminal-jni; do
    install -pm 0644 ${i}/target/jline-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/jline-${i}.jar
done

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
for i in \
  jansi \
  jansi-core \
  jline; do
    %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
    %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f ${i}
done

for i in \
  builtins \
  console \
  console-ui \
  curses reader \
  native \
%if %{with ssh}
  remote-ssh \
%endif
  remote-telnet \
  style \
  terminal \
%if %{with ffm}
  terminal-ffm \
%endif
  terminal-jansi \
  terminal-jna \
  terminal-jni; do
    %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/jline-${i}.pom
    %add_maven_depmap %{name}/jline-${i}.pom %{name}/jline-${i}.jar -f ${i}
done

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in \
  builtins \
  console \
  console-ui \
  curses reader \
  jansi \
  jansi-core \
  jline \
  native \
%if %{with ssh}
  remote-ssh \
%endif
  remote-telnet \
  style \
  terminal \
%if %{with ffm}
  terminal-ffm \
%endif
  terminal-jansi \
  terminal-jna \
  terminal-jni; do
    cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
done
%fdupes %{buildroot}%{_javadocdir}/%{name}

# native library
install -d -m 755 %{buildroot}%{_libdir}/%{name}/
install -p -m 755 libjlinenative.so %{buildroot}%{_libdir}/%{name}/

%files -f .mfiles-jline
%doc README.md
%license LICENSE.txt

%files jansi -f .mfiles-jansi
%license LICENSE.txt

%files jansi-core -f .mfiles-jansi-core
%license LICENSE.txt

%files builtins -f .mfiles-builtins
%license LICENSE.txt

%files console -f .mfiles-console
%license LICENSE.txt

%files console-ui -f .mfiles-console-ui
%license LICENSE.txt

%files curses -f .mfiles-curses
%license LICENSE.txt

%files native -f .mfiles-native
%{_libdir}/%{name}
%license LICENSE.txt

%files reader -f .mfiles-reader
%license LICENSE.txt

%if %{with ssh}
%files remote-ssh -f .mfiles-remote-ssh
%license LICENSE.txt
%endif

%if %{with ffm}
%files terminal-ffm -f .mfiles-terminal-ffm
%license LICENSE.txt
%endif

%files remote-telnet -f .mfiles-remote-telnet
%license LICENSE.txt

%files style -f .mfiles-style
%license LICENSE.txt

%files terminal -f .mfiles-terminal
%license LICENSE.txt

%files terminal-jansi -f .mfiles-terminal-jansi
%license LICENSE.txt

%files terminal-jna -f .mfiles-terminal-jna
%license LICENSE.txt

%files terminal-jni -f .mfiles-terminal-jni
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
