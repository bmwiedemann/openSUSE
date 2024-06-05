#
# spec file for package ugrep
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           ugrep
Version:        6.1.0
Release:        0
Summary:        Universal grep: a feature-rich grep implementation with focus on speed
License:        BSD-3-Clause
Group:          Productivity/File utilities
URL:            https://github.com/Genivia/ugrep
Source:         https://github.com/Genivia/ugrep/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Provides:       ugrep-indexer = 1.0.0
Obsoletes:      ugrep-indexer < 1.0.0
# the bzip3 version seems to old, the tests break with decompression errors
%if 0%{?suse_version} > 1599
BuildRequires:  pkgconfig(bzip3)
%endif
# lib/matcher_avx2.cpp is selected based on a runtime AVX2 check
# lib/matcher_avx512bw.cpp is selected based on runtime AVX512BW check
# Make OBS select an x86_64-v3 build host to reproducibly enable usage
# without cross-compiling
%ifarch x86_64
#!BuildConstraint: hardware:cpu:flag x86-64-v3
%endif

%description
Ugrep supports an interactive query UI and can search file systems, source
code, text, binary files, archives, compressed files, documents and use
fuzzy search.

%package bash-completion
Summary:        Bash completion for ugrep
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion

This package contains the bash completion for ugrep.

%package zsh-completion
Summary:        Zsh completion for ugrep
BuildRequires:  zsh
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion

This package contains the zsh completion for ugrep.

%package fish-completion
Summary:        Fish completion for ugrep
BuildRequires:  fish
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion

This package contains the fish completion for ugrep.

%prep
%autosetup -p1

%build
%configure \
	--enable-color \
%if 0%{?suse_version} > 1599
	--with-bzip3 \
%endif
	%{nil}
%make_build

%install
%make_install
%fdupes %{buildroot}%{_datadir}/%{name}

%check
%make_build test

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/ugrep

%files bash-completion
%license LICENSE.txt
%{_datadir}/bash-completion/completions/*

%files zsh-completion
%license LICENSE.txt
%{_datadir}/zsh/site-functions/*

%files fish-completion
%license LICENSE.txt
%{_datadir}/fish/vendor_completions.d/*.fish

%changelog
