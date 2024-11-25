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


%if 0%{?amzn}
%bcond_with fish
%else
%bcond_without fish
%endif
Name:           ugrep
Version:        7.1.0
Release:        0
Summary:        Universal grep: a feature-rich grep implementation with focus on speed
License:        BSD-3-Clause
Group:          Productivity/File utilities
URL:            https://github.com/Genivia/ugrep
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
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

%if %{with fish}
%package fish-completion
Summary:        Fish completion for ugrep
BuildRequires:  fish
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion

This package contains the fish completion for ugrep.
%endif

%prep
%autosetup -p1

%build
%configure \
	--disable-avx2 \
	--enable-color \
%if 0%{?suse_version} > 1599
	--with-bzip3 \
%endif
%if !%{with fish}
	--with-fish-completion-dir=no \
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

%if %{with fish}
%files fish-completion
%license LICENSE.txt
%{_datadir}/fish/vendor_completions.d/*.fish
%endif

%changelog
