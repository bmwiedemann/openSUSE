#
# spec file for package patterns-devel-java
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           patterns-devel-java
Version:        20170319
Release:        0
Summary:        Patterns for Installation (java devel)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

This particular package contains the Java Development patterns.

%package devel_java
%pattern_development
Summary:        Java Development
Group:          Metapackages
Provides:       pattern() = devel_java
Provides:       pattern-icon() = pattern-java-devel
Provides:       pattern-order() = 3300
Provides:       pattern-visible()
Recommends:     ant
Recommends:     ant-antlr
Recommends:     ant-junit
Recommends:     antlr
Recommends:     java-devel
Recommends:     javapackages-tools
Recommends:     junit
Recommends:     log4j
Recommends:     xalan-j2
Recommends:     xerces-j2

%description devel_java
Tools and libraries for software development using the Java programming language.

%prep
:

%build
:

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern devel_java to be installed.' >%{buildroot}/%{_defaultdocdir}/patterns/devel_java.txt

%files devel_java
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/devel_java.txt

%changelog
