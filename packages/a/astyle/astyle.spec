#
# spec file for package astyle
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        3.6.13
Release:        0
Summary:        Source Code Indenter, Formatter, and Beautifier for C, C++, C# and Java
License:        MIT
URL:            https://astyle.sourceforge.net/
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        libastylej.rpmlintrc
BuildRequires:  dos2unix
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
%autosetup -p2
dos2unix -v README.md doc/styles.css

%build
%set_build_flags
%make_build -C build/gcc astyled
%make_build -C build/gcc java

%install
install -Dpm 0755 build/gcc/bin/%{name}d %{buildroot}%{_bindir}/%{name}
chmod -x doc/* *.md
install -d -m 0755 %{buildroot}%{_libdir}
cp --preserve=links build/gcc/bin/libastylej.so.* %{buildroot}%{_libdir}
## libastylej is a native library used/loaded by java
## the java loader seems to only look for <libname>.so, so libastylej.so.3
## is totally useless AFAICT => let's provide the useful symlink, too -- seife
ln -s libastylej.so.3 %{buildroot}%{_libdir}/libastylej.so
install -D -m 0644 man/%{name}.1 -t %{buildroot}%{_mandir}/man1/

## ldconfig is most likely totally useless here...
%ldconfig_scriptlets -n lib%{name}j3

%files
%license LICENSE.md
%doc README.md doc/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n lib%{name}j3
%{_libdir}/libastylej.so*

%changelog
