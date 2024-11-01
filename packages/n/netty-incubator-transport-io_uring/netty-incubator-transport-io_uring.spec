#
# spec file for package netty-incubator-transport-io_uring
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


%global group_name netty-incubator-transport
%global module_name io_uring
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           %{group_name}-%{module_name}
Version:        0.0.25
Release:        0
Summary:        Netty/Incubator/Transport/Parent/io_uring
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/netty/netty-incubator-transport-io_uring
Source0:        https://github.com/netty/%{name}/archive/%{group_name}-parent-%{module_name}-%{namedversion}.tar.gz
Patch0:         no-werror.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(io.netty:netty-buffer)
BuildRequires:  mvn(io.netty:netty-common)
BuildRequires:  mvn(io.netty:netty-transport)
BuildRequires:  mvn(io.netty:netty-transport-native-unix-common)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-commons-net)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
Netty is an asynchronous event-driven network application framework for
rapid development of maintainable high performance protocol servers and
clients.
The new io_uring interface added to the Linux Kernel 5.1 is a high I/O
performance scalable interface for fully asynchronous Linux syscalls.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{group_name}-parent-%{module_name}-%{namedversion}
%patch -P 0 -p 1

%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-source-plugin

%{mvn_package} ":::linux*:"

%{mvn_package} ":{*}-parent" __noinstall

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
