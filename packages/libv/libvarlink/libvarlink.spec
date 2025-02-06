#
# spec file for package libvarlink
#
# Copyright (c) 2025 SUSE LLC
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


%global _lto_cflags %nil
%global _somajor 0
Name:           libvarlink
Version:        24
Release:        0
Summary:        A C implementation of Varlink, a protocol for creating APIs
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/varlink/libvarlink
Source0:        https://github.com/varlink/libvarlink/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  gcc
BuildRequires:  glibc-locale
BuildRequires:  glibc-locale-base
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkg-config
BuildRequires:  python3-base
%{?suse_build_hwcaps_libs}

%description
Varlink is an interface description format and protocol for creating APIs.

A varlink interface combines the classic UNIX command line options,
STDIN/OUT/ERROR text formats, man pages, service metadata and provides the
equivalent over a single file descriptor, a.k.a. “FD3”.

Varlink is plain-text, type-safe, discoverable, self-documenting and remotable.

%package devel
Summary:        Varlink C development files
Group:          Development/Languages/C and C++
Requires:       %{name}%{_somajor} = %{version}
Recommends:     varlink-util = %{version}

%description devel
Varlink is an interface description format and protocol for creating APIs.
This package contains headers for the library.

%package -n %{name}%{_somajor}
Summary:        A C implementation of Varlink, a protocol for creating APIs
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n %{name}%{_somajor}
Varlink is an interface description format and protocol for creating APIs.

A varlink interface combines the classic UNIX command line options,
STDIN/OUT/ERROR text formats, man pages, service metadata and provides the
equivalent over a single file descriptor, a.k.a. “FD3”.

Varlink is plain-text, type-safe, discoverable, self-documenting and remotable.

%package     -n varlink-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Requires:       varlink-util = %{version}
Supplements:    (varlink-util and bash-completion)
BuildArch:      noarch

%description -n varlink-bash-completion
Bash command-line completion support for %{name}.

%package    -n  varlink-vim
Summary:        Vim support for %{name}
Group:          System/Shells
Requires:       vim
BuildArch:      noarch

%description -n varlink-vim
Varlink is an interface description format and protocol for creating APIs.

%package -n     varlink-util
Summary:        Varlink command line tools
Requires:       varlink-vim = %{version}

%description -n varlink-util
This contains command-line tools and vim editor support for varlink.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
export LC_CTYPE=C.UTF-8
export LC_NUMERIC=de_DE.UTF-8
# https://github.com/varlink/libvarlink/issues/63
%ifarch ppc64le
test_list=$(%meson_test --list) 2> /dev/null
test_list=${test_list//test-symbols}
%meson_test $test_list
%else
%meson_test
%endif

%ldconfig_scriptlets -n %{name}%{_somajor}

%files -n %{name}%{_somajor}
%{_libdir}/libvarlink.so.0
%license LICENSE
%doc README.md

%files -n varlink-util
%{_bindir}/varlink
%license LICENSE
%doc README.md

%files devel
%{_includedir}/varlink.h
%{_libdir}/libvarlink.so
%{_libdir}/pkgconfig/libvarlink.pc
%license LICENSE
%doc README.md

%files -n varlink-bash-completion
%{_datadir}/bash-completion/completions/varlink
%license LICENSE
%doc README.md

%files -n varlink-vim
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/after
%dir %{_datadir}/vim/vimfiles/after/ftdetect
%dir %{_datadir}/vim/vimfiles/after/ftplugin
%dir %{_datadir}/vim/vimfiles/after/syntax
%{_datadir}/vim/vimfiles/after/ftdetect/varlink.vim
%{_datadir}/vim/vimfiles/after/ftplugin/varlink.vim
%{_datadir}/vim/vimfiles/after/syntax/varlink.vim
%license LICENSE
%doc README.md

%changelog
