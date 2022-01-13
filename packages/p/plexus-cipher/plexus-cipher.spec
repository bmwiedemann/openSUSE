#
# spec file for package plexus-cipher
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


Name:           plexus-cipher
Version:        2.0
Release:        0
Summary:        Plexus Cipher: encryption/decryption Component
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/%{name}
Source0:        https://github.com/codehaus-plexus/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-local
BuildRequires:  sisu-inject
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
Plexus Cipher: encryption/decryption Component

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} build.xml

# replace %{version}-SNAPSHOT with %{version}
%pom_xpath_set pom:project/pom:version %{version}

%pom_remove_parent .
%pom_xpath_inject pom:project "<groupId>org.codehaus.plexus</groupId>"
%pom_change_dep -r -f ::::: :::::

%mvn_file : plexus/%{name}

%build
mkdir -p lib
build-jar-repository -s lib atinject org.eclipse.sisu.inject

%ant compile
%ant jar javadoc

%mvn_artifact pom.xml target/%{name}-%{version}.jar
%mvn_alias :{*} org.sonatype.plexus:@1

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
