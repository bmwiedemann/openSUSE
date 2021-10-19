#
# spec file for package youtube-dl
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2021.10.10
Release:        0
Summary:        A tool for downloading from video sites for offline watching
License:        CC-BY-SA-3.0 AND SUSE-Public-Domain
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/yt-dlp/yt-dlp
Source:         https://github.com/yt-dlp/yt-dlp/releases/download/%version/yt-dlp.tar.gz
BuildRequires:  make >= 4
BuildRequires:  python3-devel
BuildRequires:  python3-xml
BuildRequires:  zip
BuildArch:      noarch

%description
youtube-dl is a command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

youtube-dl is inactive since 2021-07-01; yt-dlp replaces it.

%package -n yt-dlp
Summary:        A tool for downloading from video sites for offline watching
Group:          Productivity/Networking/Web/Utilities
Obsoletes:      youtube-dl <= 2021.06.06
Provides:       youtube-dl = %version-%release
Requires:       ffmpeg
Requires:       python3
Requires:       python3-xml

%description -n yt-dlp
yt-dlp is a command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

%package -n yt-dlp-bash-completion
Summary:        Bash completion for yt-dlp
Group:          System/Shells
Requires:       bash-completion
Supplements:    packageand(yt-dlp:bash)
Obsoletes:      youtube-dl-bash-completion <= 2021.06.06

%description -n yt-dlp-bash-completion
Bash command line completion support for yt-dlp.

%package -n yt-dlp-fish-completion
Summary:        Fish completion for yt-dlp
Group:          System/Shells
Requires:       fish
Supplements:    packageand(yt-dlp:fish)
Obsoletes:      youtube-dl-fish-completion <= 2021.06.06

%description -n yt-dlp-fish-completion
Fish command line completion support for yt-dlp.

%package -n yt-dlp-zsh-completion
Summary:        Zsh Completion for yt-dlp
Group:          System/Shells
Requires:       zsh
Supplements:    packageand(yt-dlp:zsh)

%description -n yt-dlp-zsh-completion
ZSH command line completion support for yt-dlp.

%prep
%autosetup -n yt-dlp

%build
rm -f youtube-dl yt-dlp
PYTHON="%_bindir/python3" %make_build yt-dlp

%install
b="%buildroot"
install -Dvm0755 yt-dlp "$b/%_bindir/yt-dlp"
ln -sv yt-dlp "$b/%_bindir/youtube-dl"
install -Dvm0644 completions/bash/yt-dlp "$b/%_datadir/bash-completion/completions/yt-dlp"
install -Dvm0644 completions/zsh/_yt-dlp "$b/%_datadir/zsh/site-functions/_yt-dlp"
install -Dvm0644 completions/fish/yt-dlp.fish "$b/%_datadir/fish/completions/yt-dlp.fish"
install -Dvm0644 yt-dlp.1 "$b/%_mandir/man1/yt-dlp.1"
echo ".SO yt-dlp.1" >"$b/%_mandir/man1/youtube-dl.1"

%files -n yt-dlp
%license LICENSE
%doc README.md
%_bindir/yt-dlp
%_bindir/youtube-dl
%_mandir/man1/*.1*

%files -n yt-dlp-bash-completion
%_datadir/bash-completion/

%files -n yt-dlp-fish-completion
%_datadir/fish/

%files -n yt-dlp-zsh-completion
%_datadir/zsh/

%changelog
