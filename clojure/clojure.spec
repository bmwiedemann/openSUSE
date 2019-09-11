#
# spec file for package clojure
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

%define         toolsver 447
Name:           clojure
Version:        1.10.1
Release:        0
Summary:        A dynamic programming language that targets the JVM
License:        EPL-1.0
Group:          Development/Languages/Other
URL:            http://clojure.org/
Source0:        https://download.clojure.org/install/clojure-tools-%{version}.%{toolsver}.tar.gz
Requires:       java >= 1.8.0
BuildRequires:  fdupes
BuildArch:      noarch

%description
Clojure is a dynamic programming language that targets the Java
Virtual Machine (and the CLR, and JavaScript). It is designed to be a
general-purpose language, combining the approachability and
interactive development of a scripting language with an efficient and
robust infrastructure for multithreaded programming. Clojure is a
compiled language - it compiles directly to JVM bytecode, yet remains
completely dynamic. Every feature supported by Clojure is supported at
runtime. Clojure provides easy access to the Java frameworks, with
optional type hints and type inference, to ensure that calls to Java
can avoid reflection.

%prep
%setup -q -n clojure-tools
sed -i "s/#!\/usr\/bin\/env bash/#!\/bin\/bash/" clj
sed -i "s/#!\/usr\/bin\/env bash/#!\/bin\/bash/" clojure
#sed -i "s|PREFIX|%{_prefix}|" clojure
sed -i "s|PREFIX|/usr/share/clojure|" clojure

%build

%install

install -Dm644 deps.edn "%{buildroot}/usr/share/clojure/deps.edn"
install -Dm644 example-deps.edn "%{buildroot}/usr/share/clojure/example-deps.edn"
install -Dm644 clojure-tools-%{version}.%{toolsver}.jar "%{buildroot}/usr/share/clojure/libexec/clojure-tools-%{version}.%{toolsver}.jar"
install -Dm755 clojure "%{buildroot}/usr/bin/clojure"
install -Dm755 clj "%{buildroot}/usr/bin/clj"
install -Dm644 clojure.1 "%{buildroot}/usr/share/man/man1/clojure.1"
install -Dm644 clj.1 "%{buildroot}/usr/share/man/man1/clj.1"

%fdupes %{buildroot}

%files
%dir /usr/share/clojure
%dir /usr/share/clojure/libexec
/usr/bin/clj
/usr/bin/clojure
/usr/share/clojure/deps.edn
/usr/share/clojure/example-deps.edn
/usr/share/clojure/libexec/clojure-tools-1.10.1.447.jar
/usr/share/man/man1/clj.1.gz
/usr/share/man/man1/clojure.1.gz

%changelog
