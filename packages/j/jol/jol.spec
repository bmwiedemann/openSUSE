#
# spec file for package jol
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


%global _desc %{expand:
JOL (Java Object Layout) is a tiny toolbox to analyze Java object
layouts.  These tools use Unsafe, JVMTI, and Serviceability Agent (SA)
heavily to decode the actual object layout, footprint, and references.
This makes JOL much more accurate than other tools relying on heap dumps,
specification assumptions, etc.}
Name:           jol
Version:        0.17
Release:        0
Summary:        Java Object Layout
License:        GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://openjdk.java.net/projects/code-tools/jol/
Source0:        https://github.com/openjdk/jol/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(net.sf.jopt-simple:jopt-simple)
BuildArch:      noarch

%description %{_desc}

%package        core
Summary:        Java Object Layout core classes
Group:          Development/Libraries/Java

%description    core %{_desc}

This package contains the core classes for JOL.

%package        cli
Summary:        Java Object Layout command line interface
Group:          Development/Libraries/Java
Requires:       %{name}-core = %{version}-%{release}

%description    cli %{_desc}

This package contains a command line interface to JOL.

%package javadoc
Summary:        Javadoc for Java Object Layout
Group:          Documentation/HTML

%description javadoc %{_desc}

This package contains the API documentation for JOL.

%prep
%autosetup

# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-source-plugin

# We do not need benchmarks or samples
%pom_disable_module jol-benchmarks
%pom_disable_module jol-samples

%{mvn_package} :jol-parent __noinstall

%build
%{mvn_build} -s -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files core -f .mfiles-jol-core
%doc README.md
%license LICENSE

%files cli -f .mfiles-jol-cli

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
