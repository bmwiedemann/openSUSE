#
# spec file for package uima-parent-pom
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


Name:           uima-parent-pom
Version:        18
Release:        0
Summary:        Apache UIMA Parent POM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://uima.apache.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildArch:      noarch

%description
UIMA (Unstructured Information Management Architecture).
UIMA promotes community development and reuse of annotators
that extract meta-data from unstructured information (text,
audio, video, etc.); it provides for externalized declaration of
type systems, component configuration, aggregation, and more,
supports scalablity, and provides tooling.

This package provides Parent for Apache UIMA Projects.

%prep
%setup -q
# Unavailable deps
%pom_xpath_remove "pom:project/pom:profiles"

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-release-plugin

%build
%{mvn_build} -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%changelog
