#
# spec file for package gnu-crypto
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnu-crypto
Version:        2.0.1
Release:        0
Summary:        GNU Crypto
License:        GPL-2.0-or-later
Group:          Development/Languages/Java
Url:            http://www.gnu.org/software/gnu-crypto/
Source:         ftp://ftp.gnu.org/gnu/%{name}/releases/%{name}-%{version}.tar.bz2
Patch0:         sasl-functions.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  unzip
Provides:       jce
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
GNU Crypto provides implementations of cryptographic primitives and
tools in the Java programming language for use by programmers and
end-users.

%prep
%setup -q
%patch0

%build
export CLASSPATH=$(build-classpath glibj)
ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 jar

%install
mkdir -p %{buildroot}/%{_javadir}
cp lib/*.jar %{buildroot}/%{_javadir}

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
