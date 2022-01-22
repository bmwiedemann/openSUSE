#
# spec file for package yt-dlp
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


Name:           yt-dlp
Version:        2022.01.21
Release:        0
Summary:        Enhanced fork of youtube-dl, a video site downloader for offline watching
License:        CC-BY-SA-3.0 AND SUSE-Public-Domain
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/yt-dlp/yt-dlp
Source:         %url/releases/download/%version/yt-dlp.tar.gz
BuildRequires:  make >= 4
BuildRequires:  python3-devel
BuildRequires:  python3-xml
BuildRequires:  zip
BuildArch:      noarch
Requires:       ffmpeg
Requires:       python3
Requires:       python3-xml

%description
yt-dlp is a command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

%package bash-completion
Summary:        Bash completion for yt-dlp
Group:          System/Shells
Requires:       bash-completion
Supplements:    (yt-dlp and bash-completion)

%description bash-completion
Bash command line completion support for yt-dlp.

%package fish-completion
Summary:        Fish completion for yt-dlp
Group:          System/Shells
Requires:       fish
Supplements:    (yt-dlp and fish)

%description fish-completion
Fish command line completion support for yt-dlp.

%package zsh-completion
Summary:        Zsh Completion for yt-dlp
Group:          System/Shells
Requires:       zsh
Supplements:    (yt-dlp and zsh)

%description zsh-completion
ZSH command line completion support for yt-dlp.

%prep
%autosetup -p1 -n %name

%build
rm -f youtube-dl yt-dlp
PYTHON="%_bindir/python3" %make_build yt-dlp

%install
b="%buildroot"
install -Dvm0755 yt-dlp "$b/%_bindir/yt-dlp"
install -Dvm0644 completions/bash/yt-dlp "$b/%_datadir/bash-completion/completions/yt-dlp"
install -Dvm0644 completions/zsh/_yt-dlp "$b/%_datadir/zsh/site-functions/_yt-dlp"
install -Dvm0644 completions/fish/yt-dlp.fish "$b/%_datadir/fish/completions/yt-dlp.fish"
install -Dvm0644 yt-dlp.1 "$b/%_mandir/man1/yt-dlp.1"

%files
%license LICENSE
%doc README.md
%_bindir/%name
%_mandir/man1/%name.1%ext_man

%files -n yt-dlp-bash-completion
%_datadir/bash-completion/

%files -n yt-dlp-fish-completion
%_datadir/fish/

%files -n yt-dlp-zsh-completion
%_datadir/zsh/

%changelog
