#
# spec file for package xsom
#
# Copyright (c) 2022 SUSE LLC
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


%global checkout 20140925
Name:           xsom
Version:        0~%{checkout}
Release:        0
Summary:        XML Schema Object Model (XSOM)
License:        CDDL-1.1 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/kohsuke/xsom
Source0:        %{name}-%{checkout}.tar.xz
Patch0:         %{name}-%{checkout}-licenseheader.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  relaxngcc
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildArch:      noarch

%description
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.  The library is a straight-forward implement of "schema components" as
defined in the XML Schema spec part 1.  Refer to this specification of how this
object model works.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{checkout}
%patch0 -p1

pushd lib
  ln -sf `find-jar relaxngcc` relaxngcc.jar
popd

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dproject.build.sourceEncoding=UTF-8 -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
