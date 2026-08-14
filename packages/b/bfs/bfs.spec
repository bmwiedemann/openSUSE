#
# spec file for package bfs
#
# Copyright (c) 2023 SUSE LLC
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

%if 0%{?suse_version} && 0%{?suse_version} < 1600
%global force_gcc_version 12
%endif

Name:           bfs
Version:        4.1.3
Release:        0
Summary:        A breadth-first version of the UNIX find command
License:        0BSD
URL:            https://tavianator.com/projects/bfs.html
Source:         https://github.com/tavianator/bfs/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fish
BuildRequires:  pkgconfig
BuildRequires:  zsh
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libacl)
%if 0%{?suse_version} >= 1699
BuildRequires:  pkgconfig(libattr)
%else
BuildRequires:  libattr-devel
%endif
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(oniguruma)

BuildRequires:  gcc%{?force_gcc_version}-c++ >= 12
%if 0%{?force_gcc_version}
#!BuildIgnore:  libgcc_s1
%endif

%description
bfs is a variant of the UNIX find command that operates breadth-first rather than depth-first. It is otherwise compatible with many versions of find.

%package completion-bash
Summary:        Bash completion for bfs
BuildArch:      noarch
Requires:       %{name}
Requires:       bash
Supplements:    (bash and bfs)
%description completion-bash
bfs is a variant of the UNIX find command that operates breadth-first rather than depth-first. It is otherwise compatible with many versions of find.

This package holds the bash completion for %{name}.

%package completion-fish
Summary:        Bash completion for bfs
BuildArch:      noarch
Requires:       %{name}
Requires:       fish
Supplements:    (fish and bfs)
%description completion-fish
bfs is a variant of the UNIX find command that operates breadth-first rather than depth-first. It is otherwise compatible with many versions of find.

This package holds the fish completion for %{name}.

%package completion-zsh
Summary:        zsh completion for bfs
BuildArch:      noarch
Requires:       %{name}
Requires:       zsh
Supplements:    (zsh and bfs)
%description completion-zsh
bfs is a variant of the UNIX find command that operates breadth-first rather than depth-first. It is otherwise compatible with many versions of find.

This package holds the zsh completion for %{name}.

%prep
%autosetup -p1

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
./configure           \
  --with-libacl     \
  --with-libcap     \
  --with-libselinux \
  --with-liburing   \
  --with-oniguruma  \
  CFLAGS="%{optflags}"

%make_build

%install
%make_install

%files
%license LICENSE
%doc docs/*.md
%doc README.md
%{_bindir}/bfs
%{_mandir}/man1/bfs.1%{?ext_man}

%files completion-bash
%{_datadir}/bash-completion/completions/bfs

%files completion-fish
%{_datadir}/fish/vendor_completions.d/bfs.fish

%files completion-zsh
%{_datadir}/zsh/site-functions/_bfs

%changelog
