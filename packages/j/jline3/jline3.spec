#
# spec file for package jline3
#
# Copyright (c) 2024 SUSE LLC
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
Name:           jline3
Version:        3.22.0
Release:        0
Summary:        Java library for handling console input
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/jline/jline3
Source0:        %{url}/archive/refs/tags/jline-parent-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.googlecode.juniversalchardet:juniversalchardet)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.sshd:sshd-core)
BuildRequires:  mvn(org.apache.sshd:sshd-scp)
BuildRequires:  mvn(org.apache.sshd:sshd-sftp)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
JLine is a Java library for handling console input. It is similar in
functionality to BSD editline and GNU readline but with additional features
that bring it in par with ZSH line editor. People familiar with the
readline/editline capabilities for modern shells (such as bash and tcsh) will
find most of the command editing features of JLine to be familiar.

JLine 3.x is an evolution of JLine 2.x.

%package parent
Summary:        JLine Parent

%description parent
%{desc}

%package builtins
Summary:        JLine Builtins

%description builtins
%{desc}

This package contains several high level tools: less pager, nano editor, screen
multiplexer, etc…

%package console
Summary:        JLine Console

%description console
%{desc}

This package contains the command registry, object printer and widget
implementations.

%package reader
Summary:        JLine Reader

%description reader
%{desc}

This package contains the line reader (including completion, history, etc…).

%package remote-telnet
Summary:        JLine Remote Telnet

%description remote-telnet
%{desc}

This package contains the helpers for using jline over telnet (including
a telnet server implementation).

%package remote-ssh
Summary:        JLine Remote SSH
Recommends:     mvn(org.apache.sshd:scp-core)
Recommends:     mvn(org.apache.sshd:sftp-core)
Recommends:     mvn(org.apache.sshd:sshd-core)

%description remote-ssh
%{desc}

This package contains the helpers for using jline with Mina SSHD.

%package style
Summary:        JLine Style

%description style
%{desc}

This package contains the styling api.

%package terminal-jna
Summary:        JLine JNA Terminal

%description terminal-jna
%{desc}

This package contains terminal implementations leveraging the JNA library.

%package terminal
Summary:        JLine Terminal

%description terminal
%{desc}

This package contains the Terminal api and implementations.

%package terminal-jansi
Summary:        JLine JANSI Terminal

%description terminal-jansi
%{desc}

This package contains terminal implementations leveraging the Jansi library.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-jline-parent-%{version}
%pom_disable_module demo
%pom_disable_module groovy
%pom_disable_module graal

%pom_remove_plugin org.graalvm.nativeimage:native-image-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_remove -r "pom:arg[text()='-Werror']" . jline
%pom_remove_plugin :maven-dependency-plugin jline
%pom_remove_plugin :build-helper-maven-plugin jline
# This replaces the action of the two removed plugins
mkdir -p jline/src/main/java
mkdir -p jline/src/main/resources
for module in  \
    terminal \
    terminal-jansi \
    terminal-jna \
    reader \
    builtins \
    console \
    remote-ssh \
    remote-telnet \
    style; do
  if [ -d ${module}/src/main/java ]; then
    cp -r ${module}/src/main/java/* jline/src/main/java/
  fi
  if [ -d ${module}/src/main/resources ]; then
    cp -r ${module}/src/main/resources/* jline/src/main/resources/
  fi
done

%build
%{mvn_build} -f -s -- -Dnojavadoc=true

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles-jline
%doc README.md
%license LICENSE.txt

%files builtins -f .mfiles-jline-builtins
%license LICENSE.txt

%files console -f .mfiles-jline-console
%license LICENSE.txt

%files reader -f .mfiles-jline-reader
%license LICENSE.txt

%files remote-telnet -f .mfiles-jline-remote-telnet
%license LICENSE.txt

%files style -f .mfiles-jline-style
%license LICENSE.txt

%files terminal -f .mfiles-jline-terminal
%license LICENSE.txt

%files terminal-jna -f .mfiles-jline-terminal-jna
%license LICENSE.txt

%files terminal-jansi -f .mfiles-jline-terminal-jansi
%license LICENSE.txt

%files remote-ssh -f .mfiles-jline-remote-ssh
%license LICENSE.txt

%files parent -f .mfiles-jline-parent
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
