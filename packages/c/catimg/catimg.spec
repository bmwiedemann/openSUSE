#
# spec file for package catimg
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           catimg
Version:        2.8.0
Release:        0
Summary:        Insanely fast image printing in your terminal
License:        MIT
Group:          Productivity/Graphics/Viewers
URL:            https://posva.net/shell/retro/bash/2013/05/27/catimg
Source:         https://github.com/posva/catimg/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/posva/catimg/pull/76
Patch0:         catimg-gcc15.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
Requires:       ImageMagick

%description
catimg is a little program written in C with no dependencies that prints images in terminal. It supports JPEG, PNG and GIF formats. This program was originally a script that did the same by using ImageMagick convert.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for catimg.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm 0644 completion/_%{name}  %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/catimg
%{_mandir}/man1/catimg.1%{?ext_man}

%files zsh-completion
%license LICENSE
%{_datadir}/zsh

%changelog
