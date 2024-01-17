#
# spec file for package catimg
#
# Copyright (c) 2022 SUSE LLC
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
Version:        2.7.0
Release:        0
License:        MIT
Summary:        Insanely fast image printing in your terminal
Group:          Productivity/Graphics/Viewers
URL:            http://posva.net/shell/retro/bash/2013/05/27/catimg
Source:         https://github.com/posva/catimg/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
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
%setup -q -n %{name}-%{version}

%build
%cmake
%make_build

%install
cd build
%make_install

install -Dm 0644 ../completion/_%{name}  %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}


%files
%{_bindir}/*
%_mandir/*/*
%doc README.md
%license LICENSE

%files zsh-completion
%{_datadir}/zsh

%changelog
