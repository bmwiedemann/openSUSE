#
# spec file for package astyle
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


Name:           astyle
Version:        3.1
Release:        0
Summary:        Source Code Indenter, Formatter, and Beautifier for C, C++, C# and Java
License:        MIT
Url:            http://astyle.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}%20%{version}/%{name}_%{version}_linux.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  java-devel

%description
Artistic Style is a source code indenter, formatter, and beautifier for the C,
C++, C# and Java programming languages. It automatically re-indents and
re-formats C / C++ / C# / Java source files. It can be used from a command
line, or it can be incorporated as classes in another C++ program.

%package -n lib%{name}j3
Summary:        Java bindings for %{name}

%description -n lib%{name}j3
This package contains Java bindings for %{name}.

%prep
%setup -q -n %{name}

%build
if [ \! -x $JAVA_HOME/bin/javac ] && echo $JAVA_HOME | grep jre ; then
  echo WTF IS SETTING \$JAVA_HOME TO JRE \!?
  JAVA_HOME=$(echo $JAVA_HOME | sed -e s/jre/java/g)
fi
export CFLAGS="%{optflags} -I $JAVA_HOME/include/linux"
export CXXFLAGS="%{optflags}"
make -C build/gcc astyled %{?_smp_mflags}
# javaall = java + javadebug
make -C build/gcc java %{?_smp_mflags}

%install
install -Dpm 0755 build/gcc/bin/%{name}d \
  %{buildroot}%{_bindir}/%{name}
chmod -x doc/* *.md
install -d -m 0755 %{buildroot}%{_libdir}
install -m 0644 build/gcc/bin/libastylej.so.* %{buildroot}%{_libdir}
(cd %{buildroot}%{_libdir}; ln -s libastylej.so.* libastylej.so)

%files
%defattr(-,root,root)
%doc LICENSE.md README.md doc/
%{_bindir}/%{name}

%files -n lib%{name}j3
%{_libdir}/*.so*

%changelog
