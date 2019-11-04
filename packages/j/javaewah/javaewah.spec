#
# spec file for package javaewah
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           javaewah
Version:        1.1.6
Release:        0
Summary:        A word-aligned compressed variant of the Java bitset class
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/lemire/javaewah
Source0:        https://github.com/lemire/javaewah/archive/JavaEWAH-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
JavaEWAH is a word-aligned compressed variant of the Java bitset class.
It uses a 64-bit run-length encoding (RLE) compression scheme.

The goal of word-aligned compression is not to achieve the best
compression, but rather to improve query processing time. Hence, we try
to save CPU cycles, maybe at the expense of storage. However, the EWAH
scheme we implemented is always more efficient storage-wise than an
uncompressed bitmap (implemented in Java as the BitSet class). Unlike
some alternatives, javaewah does not rely on a patented scheme.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n javaewah-JavaEWAH-%{version}

# Plugins that are unnecessary for RPM build
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-source-plugin

# Avoids JVM startup error when jacoco-maven-plugin is not in use
%pom_xpath_inject "pom:project/pom:properties" "<argLine/>"

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGELOG README.md
%license LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt

%changelog
