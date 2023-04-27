#
# spec file
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


%global cluster jnr
Name:           %{cluster}-ffi
Version:        2.2.13
Release:        0
Summary:        Java Abstracted Foreign Function Layer
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://github.com/%{cluster}/%{name}/
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jffi)
BuildRequires:  mvn(com.github.jnr:jffi::native:)
BuildRequires:  mvn(com.github.jnr:jnr-a64asm)
BuildRequires:  mvn(com.github.jnr:jnr-x86asm)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
JNR-FFI is a Java library for loading native libraries without writing JNI code
by hand, or using tools such as SWIG.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%if %{?pkg_vcmp:%pkg_vcmp maven-antrun-plugin >= 3}%{!?pkg_vcmp:0}
sed -i -e 's#tasks\>#target\>#g' pom.xml
%endif

%{mvn_file} : %{cluster}/%{name}

# remove all builtin jars
find -name '*.jar' -delete

# Unnecessary for RPM builds
%pom_remove_plugin :maven-javadoc-plugin

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
   -Dmaven.compiler.release=8 \
%endif
   -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
