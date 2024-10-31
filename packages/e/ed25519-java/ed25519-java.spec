#
# spec file for package ed25519-java
#
# Copyright (c) 2024 SUSE LLC
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


%global artifactId eddsa
Name:           ed25519-java
Version:        0.3.0
Release:        0
Summary:        Implementation of EdDSA (Ed25519) in Java
License:        CC0-1.0
URL:            https://github.com/str4d/ed25519-java
Source0:        https://github.com/str4d/ed25519-java/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
Patch0:         0001-EdDSAEngine.initVerify-Handle-any-non-EdDSAPublicKey.patch
Patch1:         0002-Disable-test-that-relies-on-internal-sun-JDK-classes.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
This is an implementation of EdDSA in Java. Structurally, it
is based on the ref10 implementation in SUPERCOP (see
http://ed25519.cr.yp.to/software.html).

There are two internal implementations:

* A port of the radix-2^51 operations in ref10
  - fast and constant-time, but only useful for Ed25519.
* A generic version using BigIntegers for calculation
  - a bit slower and not constant-time, but compatible
    with any EdDSA parameter specification.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml
%patch -P 0 -p1
%patch -P 1 -p1

%build
ant jar javadoc

%install

# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{artifactId}-%{version}.jar %{buildroot}%{_javadir}/%{artifactId}.jar
ln -sf %{_javadir}/%{artifactId}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%mvn_install_pom pom.xml %{buildroot}%{_mavenpomdir}/%{artifactId}.pom
%add_maven_depmap %{artifactId}.pom %{artifactId}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/%{name}.jar
%doc README.md
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
