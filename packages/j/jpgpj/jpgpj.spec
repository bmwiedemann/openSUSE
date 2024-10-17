#
# spec file for package jpgpj
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


Name:           jpgpj
Version:        1.3
Release:        0
Summary:        Java Pretty Good Privacy Jig
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/justinludwig/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/c02e/jpgpj/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
JPGPJ provides a simple API on top of the Bouncy Castle Java OpenPGP
implementation (which is full and robust implementation of RFC 4880, and
compatible with other popular PGP implementations such as GnuPG, GPGTools, and
Gpg4win). The JPGPJ API is limited to file encryption, signing, decryption, and
verification; it does not include the ability to generate, update, or sign
keys, or to do clearsigning or detached signatures.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}

%prep
%autosetup

cp %{SOURCE1} pom.xml

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
