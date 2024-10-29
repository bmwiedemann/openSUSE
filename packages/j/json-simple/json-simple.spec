#
# spec file for package json-simple
#
# Copyright (c) 2020 SUSE LLC
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


Name:           json-simple
Version:        1.1.1
Release:        0
Summary:        Simple Java toolkit for JSON
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://code.google.com/p/json-simple/
# svn export http://json-simple.googlecode.com/svn/tags/tag_release_1_1_1/ json-simple-1.1.1
# tar czf json-simple-1.1.1-src-svn.tar.gz json-simple-1.1.1
Source0:        json-simple-1.1.1-src-svn.tar.gz
#https://code.google.com/p/json-simple/issues/detail?id=97
Patch0:         json-simple-hash-java-1.8.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
JSON.simple is a simple Java toolkit for JSON. You can use JSON.simple
to encode or decode JSON text.
  * Full compliance with JSON specification (RFC4627) and reliable
  * Provides multiple functionalities such as encode, decode/parse
    and escape JSON text while keeping the library lightweight
  * Flexible, simple and easy to use by reusing Map and List interfaces
  * Supports streaming output of JSON text
  * Stoppable SAX-like interface for streaming input of JSON text
  * Heap based parser
  * High performance (see performance testing)
  * No dependency on external libraries
  * Both of the source code and the binary are JDK1.2 compatible

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n json-simple-%{version}
find . -name '*.jar' -exec rm -f '{}' \;
# All the files have dos line endings, remove them.
find . -type f -exec sed -i 's/\r//' {} \;

%patch -P 0 -p1

# Remove hard-coded compiler settings
%pom_remove_plugin :maven-compiler-plugin

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%fdupes %{buildroot}%{datadir}/javadoc

%files -f .mfiles
%license LICENSE.txt
%doc AUTHORS.txt ChangeLog.txt README.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
