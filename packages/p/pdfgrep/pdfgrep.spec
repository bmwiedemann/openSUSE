#
# spec file for package pdfgrep
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           pdfgrep
Version:        2.2.0
Release:        0
Summary:        Search in pdf files for strings matching a regular expression
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://pdfgrep.org/
Source:         https://pdfgrep.org/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel >= 1.0.0
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(poppler-cpp) >= 0.36.0

%description
Pdfgrep is a tool to search text in PDF files. It works similar to `grep'.

Features:
- search for regular expressions.
- support for some important grep options, including:
+ filename output.
+ page number output.
+ optional case insensitivity.
+ count occurrences.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%package zsh-completion
Summary:        ZSH completion for %{name}
Group:          Productivity/Networking/Security
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for %{name}.

%prep
%autosetup -p1

%build
%configure \
  --with-bash-completion
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%license COPYING
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%license COPYING
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
