#
# spec file for package clojure
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


Name:           clojure
Version:        1.10.1.727
Release:        0
Summary:        A dynamic programming language that targets the JVM
License:        EPL-1.0
Group:          Development/Languages/Other
URL:            https://clojure.org/
Source0:        https://download.clojure.org/install/clojure-tools-%{version}.tar.gz
BuildRequires:  fdupes
Requires:       java >= 1.8.0
BuildArch:      noarch

%description
Clojure is a dynamic programming language that targets the Java
Virtual Machine (and the CLR, and JavaScript). It is designed to be a
general-purpose language, combining the approachability and
interactive development of a scripting language with an
infrastructure for multithreaded programming. Clojure is a
compiled language - it compiles directly to JVM bytecode, yet remains
completely dynamic. Every feature supported by Clojure is supported at
runtime. Clojure provides access to the Java frameworks, with
optional type hints and type inference, to ensure that calls to Java
can avoid reflection.

%prep
%setup -q -n clojure-tools
sed -i "s/#!\/usr\/bin\/env bash/#!\/bin\/bash/" clj
sed -i "s/#!\/usr\/bin\/env bash/#!\/bin\/bash/" clojure
sed -i "s|PREFIX|%{_datadir}/clojure|" clojure

%build

%install
install -Dm644 deps.edn "%{buildroot}/%{_datadir}/clojure/deps.edn"
install -Dm644 example-deps.edn "%{buildroot}/%{_datadir}/clojure/example-deps.edn"
install -Dm644 exec.jar "%{buildroot}/%{_datadir}/clojure/libexec/exec.jar"
install -Dm644 clojure-tools-%{version}.jar "%{buildroot}/%{_datadir}/clojure/libexec/clojure-tools-%{version}.jar"
install -Dm755 clojure "%{buildroot}/%{_bindir}/clojure"
install -Dm755 clj "%{buildroot}/%{_bindir}/clj"
install -Dm644 clojure.1 "%{buildroot}%{_mandir}/man1/clojure.1"
install -Dm644 clj.1 "%{buildroot}%{_mandir}/man1/clj.1"

%fdupes %{buildroot}/%{_prefix}

%files
%dir %{_datadir}/clojure
%dir %{_datadir}/clojure/libexec
%{_bindir}/clj
%{_bindir}/clojure
%{_datadir}/clojure/deps.edn
%{_datadir}/clojure/example-deps.edn
%{_datadir}/clojure/libexec/exec.jar
%{_datadir}/clojure/libexec/clojure-tools-%{version}.jar
%{_mandir}/man1/*

%changelog
