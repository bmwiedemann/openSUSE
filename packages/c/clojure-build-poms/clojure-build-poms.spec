#
# spec file for package clojure-build-poms
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           clojure-build-poms
Version:        1.4.3
Release:        0
Summary:        Parent POM for projects contributed to Clojure
License:        EPL-1.0
URL:            https://github.com/clojure/build.poms
Source0:        https://github.com/clojure/build.poms/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(com.theoryinpractise:clojure-maven-plugin)
BuildRequires:  mvn(org.clojure:clojure)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
#!BuildRequires: clojure-spec-alpha-bootstrap clojure-bootstrap clojure-core-specs-alpha-bootstrap
BuildArch:      noarch

%description
This package defines a common Maven Project Object Model (POM) baseline for
libraries contributed to Clojure.

%prep
%setup -q -n build.poms-%{version}

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-release-plugin

%build
%{mvn_build} -jf

%install
%mvn_install

%files -f .mfiles
%doc README.md example-project-pom.xml

%changelog
