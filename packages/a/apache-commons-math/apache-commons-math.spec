#
# spec file for package apache-commons-math
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


%global base_name       math
%global short_name      commons-%{base_name}
Name:           apache-commons-math
Version:        3.6.1
Release:        0
Summary:        The Apache Commons Mathematics Library
License:        Apache-2.0
URL:            http://commons.apache.org/%{base_name}/
Source:         http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}3-%{version}-src.tar.gz
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
Provides:       apache-commons-math3 = %{version}
Obsoletes:      apache-commons-math3 < %{version}
BuildArch:      noarch

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in
the Java programming language or Commons Lang.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n %{short_name}3-%{version}-src

%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :build-helper-maven-plugin

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt license-header.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
