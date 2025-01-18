#
# spec file for package wl-screenrec
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


Name:           wl-screenrec
Version:        0.1.6
License:        Apache-2.0
Release:        0
Summary:        High performance hardware accelerated wlroots screen recorder
Group:          Productivity/Graphics/Other
URL:            https://github.com/russelltg/wl-screenrec
Source0:        https://github.com/russelltg/wl-screenrec/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  ffmpeg-devel
BuildRequires:  libdrm-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name}
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name}
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name}
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%description
High performance screen recorder for wlroots Wayland.

Uses dma-buf transfers to get surface, and uses the GPU to do both the pixel
format conversion and the encoding, meaning the raw video data never touches the
CPU, leaving it free to run your applications.

%prep
%autosetup -a1

%build
%{cargo_build} --all-features

%install
%{cargo_install} --all-features

export PATH="%{buildroot}%{_bindir}:${PATH}"
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
wl-screenrec --generate-completions bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
wl-screenrec --generate-completions fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
wl-screenrec --generate-completions zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%{_bindir}/wl-screenrec
%license LICENSE
%doc *.md

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
