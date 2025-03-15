#
# spec file for package jline3
#
# Copyright (c) 2025 SUSE LLC
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
%bcond_with ssh
%bcond_with ffm
Name:           jline3
Version:        3.29.0
Release:        0
Summary:        Java library for handling console input
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/jline/jline3
Source0:        %{url}/archive/refs/tags/jline-%{version}.tar.gz
Source1:        Load-native-library-system-wide-place.patch.in
Patch0:         0001-Remove-optional-dependency-on-universalchardet.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 11
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
%if %{with ssh}
BuildRequires:  mvn(org.apache.sshd:sshd-core)
BuildRequires:  mvn(org.apache.sshd:sshd-scp)
BuildRequires:  mvn(org.apache.sshd:sshd-sftp)
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

%package parent
Summary:        JLine Parent
BuildArch:      noarch

%description parent
%{desc}

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
%autosetup -n %{name}-jline-%{version} -p1

sed "s;@SYSTEMLIBRARYPATH@;%{_libdir}/%{name}/;g" < %{SOURCE1} | patch -p1

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
%pom_remove_plugin :central-publishing-maven-plugin
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
# Build a native object
gcc -Wall %{?build_cflags} %{?optflags} -fPIC -fvisibility=hidden -shared \
  -I native/src/main/native -I %{_jvmdir}/java/include \
  -I %{_jvmdir}/java/include/linux %{?build_ldflags} \
  -o libjlinenative.so native/src/main/native/{jlinenative,clibrary}.c

%{mvn_build} -f -s -- -Dnojavadoc=true

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}
install -d -m 755 %{buildroot}%{_libdir}/%{name}/
install -p -m 755 libjlinenative.so %{buildroot}%{_libdir}/%{name}/

%files -f .mfiles-jline
%doc README.md
%license LICENSE.txt

%files jansi -f .mfiles-jansi
%license LICENSE.txt

%files jansi-core -f .mfiles-jansi-core
%license LICENSE.txt

%files builtins -f .mfiles-jline-builtins
%license LICENSE.txt

%files console -f .mfiles-jline-console
%license LICENSE.txt

%files console-ui -f .mfiles-jline-console-ui
%license LICENSE.txt

%files curses -f .mfiles-jline-curses
%license LICENSE.txt

%files native -f .mfiles-jline-native
%{_libdir}/%{name}
%license LICENSE.txt

%files reader -f .mfiles-jline-reader
%license LICENSE.txt

%if %{with ssh}
%files remote-ssh -f .mfiles-jline-remote-ssh
%license LICENSE.txt
%endif

%if %{with ffm}
%files terminal-ffm -f .mfiles-jline-terminal-ffm
%license LICENSE.txt
%endif

%files remote-telnet -f .mfiles-jline-remote-telnet
%license LICENSE.txt

%files style -f .mfiles-jline-style
%license LICENSE.txt

%files terminal -f .mfiles-jline-terminal
%license LICENSE.txt

%files terminal-jansi -f .mfiles-jline-terminal-jansi
%license LICENSE.txt

%files terminal-jna -f .mfiles-jline-terminal-jna
%license LICENSE.txt

%files terminal-jni -f .mfiles-jline-terminal-jni
%license LICENSE.txt

%files parent -f .mfiles-jline-parent
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
