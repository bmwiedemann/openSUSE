#
# spec file for package brotli-java
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


Name:           brotli-java
Version:        1.2.0
Release:        0
Summary:        Brotli compression format for Java
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/google/brotli
Source0:        brotli-%{version}.tar.xz
Source100:      %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.

The specification of the Brotli Compressed Data Format is defined in RFC 7932.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n brotli-%{version}
cp %{SOURCE100} java/org/brotli/dec/build.xml

%pom_xpath_set pom:project/pom:version %{version} java/org/brotli/dec

%build
pushd java/org/brotli/dec
ant jar javadoc
popd

%install
pushd java/org/brotli/dec
#jar
install -dm 0755 %{buildroot}%{_javadir}/brotli
install -pm 0644 target/org.brotli.dec*.jar %{buildroot}%{_javadir}/brotli/dec.jar
#pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/brotli
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/brotli/dec.pom
%add_maven_depmap brotli/dec.pom brotli/dec.jar
#javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f java/org/brotli/dec/.mfiles
%license LICENSE
%doc README README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
