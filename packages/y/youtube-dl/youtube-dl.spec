#
# spec file for package youtube-dl
#
# Copyright (c) 2020 SUSE LLC
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


Name:           youtube-dl
Version:        2020.11.01.1
Release:        0
Summary:        A tool for downloading from video sites for offline watching
License:        SUSE-Public-Domain AND CC-BY-SA-3.0
Group:          Productivity/Networking/Web/Utilities
URL:            https://yt-dl.org/
#Git-Clone:     https://github.com/ytdl-org/youtube-dl
Source:         https://yt-dl.org/downloads/%version/%name-%version.tar.gz
Source2:        https://yt-dl.org/downloads/%version/%name-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  make >= 4
BuildRequires:  python3-devel
BuildRequires:  python3-xml
BuildRequires:  zip
Requires:       ffmpeg
Requires:       python3
Requires:       python3-xml
BuildArch:      noarch

%description
youtube-dl is a small command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

%package        bash-completion
Summary:        Bash completion for %name
Group:          System/Shells
Requires:       bash-completion
Supplements:    packageand(%name:bash)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %name.

%package        fish-completion
Summary:        Fish completion for %name
Group:          System/Shells
Requires:       fish
Supplements:    packageand(%name:fish)
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %name.

%package        zsh-completion
Summary:        Zsh Completion for %name
Group:          System/Shells
Requires:       zsh
Supplements:    packageand(%name:zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %name.

%prep
%autosetup -p1 -n %name

%build
rm -f youtube-dl
PYTHON="%_bindir/python3" make %{?_smp_mflags}

%install
install -D -m 755 youtube-dl %buildroot/%_bindir/%name
install -D -m 644 youtube-dl.bash-completion %buildroot/%_datadir/bash-completion/completions/%name
install -D -m 644 youtube-dl.zsh %buildroot/%_datadir/zsh/site-functions/_%name
install -D -m 644 youtube-dl.fish %buildroot/%_datadir/fish/completions/%name.fish
install -D -m 644 youtube-dl.1 %buildroot/%_mandir/man1/%name.1

%files
%license LICENSE
%doc README.txt
%_bindir/%name
%_mandir/man1/%name.1%{?ext_man}

%files bash-completion
%_datadir/bash-completion/

%files fish-completion
%_datadir/fish/

%files zsh-completion
%_datadir/zsh/

%changelog
