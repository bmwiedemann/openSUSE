#
# spec file for package hax
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           hax
Version:        0.5.0
Release:        0
Summary:        Minimalist terminal-native coding agent written in C
License:        MIT
URL:            https://usehax.dev
Source0:        https://github.com/OleksandrChekhovskyi/hax/releases/download/v%{version}/hax-%{version}.tar.xz
Source1:        hax.1
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(jansson) >= 2.13
BuildRequires:  pkgconfig(libcurl)
Suggests:       fzf
Suggests:       git
Suggests:       less
Suggests:       wl-clipboard
Suggests:       xclip
Suggests:       xsel

%description
hax is a minimalist, terminal-native coding agent written in C. It is a
single small binary that talks to OpenAI, Anthropic, OpenRouter and
compatible providers, or to local models through llama.cpp and ollama.
It keeps native terminal scrollback, uses XDG paths, and extends through
config, markdown files and subprocesses instead of a plugin runtime.

%prep
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install
install -Dm644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hax.1 &&
gzip -9n %{buildroot}%{_mandir}/man1/hax.1

%files
%license LICENSE
%doc README.md CHANGELOG.md docs
%{_mandir}/man1/hax.1%{?ext_man}
%{_bindir}/hax

%changelog
