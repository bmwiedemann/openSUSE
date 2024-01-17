#
# spec file for package jnr-x86asm
#
# Copyright (c) 2021 SUSE LLC
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


%global cluster jnr
Name:           %{cluster}-x86asm
Version:        1.0.2
Release:        0
Summary:        Pure java x86 and x86_64 assembler
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/%{cluster}/%{name}/
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        MANIFEST.MF
Patch0:         add-manifest.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
This is a pure-java port of asmjit (http://code.google.com/p/asmjit/).

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0
cp %{SOURCE1} .
%{mvn_file} : %{cluster}/%{name}

%build
%{mvn_build} -f -- -Dmaven.compiler.{source,target}=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
