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


%global parent xmvn
%global subname connector-ivy
%bcond_with tests
Name:           %{parent}-%{subname}
Version:        4.0.0~20220623.8da91ea
Release:        0
Summary:        XMvn Connector for Apache Ivy
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
BuildRequires:  %{parent}-api >= 4.0.0
BuildRequires:  ant
BuildRequires:  apache-ivy
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  slf4j
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit5
BuildRequires:  apiguardian
BuildRequires:  cglib
BuildRequires:  easymock
BuildRequires:  objectweb-asm
BuildRequires:  objenesis
%endif

%description
This package provides XMvn MOJO, which is a Maven plugin that consists
of several MOJOs.  Some goals of these MOJOs are intended to be
attached to default Maven lifecycle when building packages, others can
be called directly from Maven command line.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%{mvn_file} :%{name} %{parent}/%{name}

%build
mkdir -p lib
build-jar-repository -s lib \
%if %{with tests}
    easymock junit5 junit \
    apiguardian opentest4j \
    objenesis cglib objectweb-asm \
%endif
    ivy slf4j %{parent}

%{ant} \
%if %{without tests}
    -Dtest.skip=true \
%endif
    package javadoc

%{mvn_artifact} pom.xml target/%{name}-*.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE
%doc AUTHORS README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
