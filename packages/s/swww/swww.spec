#
# spec file for package swww
#
# Copyright (c) 2023 SUSE LLC
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


Name:           swww
Version:        0.7.0
Release:        0
Summary:        Wallpaper daemon for Wayland
License:        GPL-3.0-only
URL:            https://github.com/Horus645/swww
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust+cargo
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(xkbcommon)

%description
swww is a wallpaper daemon for Wayland that is controlled
at runtime. It uses LZ4 compression for frame animations
for animated wallpapers.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -Dm644 -T completions/swww.bash  %{buildroot}%{_datadir}/bash-completion/completions/swww
install -Dm644 -T completions/swww.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/swww.fish
install -Dm644 -T completions/_swww %{buildroot}%{_datadir}/zsh/site-functions/_swww
%{cargo_install}

%files
%{_bindir}/swww
%{_bindir}/swww-daemon
%license LICENSE
%doc CHANGELOG.md README.md

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/swww

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/swww.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_swww

%changelog
