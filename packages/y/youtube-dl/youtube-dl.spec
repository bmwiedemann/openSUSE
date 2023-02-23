#
# spec file for package youtube-dl
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2021.12.17
Release:        0
Summary:        A tool for downloading from video sites for offline watching
License:        CC-BY-SA-3.0 AND SUSE-Public-Domain
Group:          Productivity/Networking/Web/Utilities
URL:            https://yt-dl.org/
#Git-Clone:     https://github.com/ytdl-org/youtube-dl
Source:         https://yt-dl.org/downloads/%version/%name-%version.tar.gz
Source2:        https://yt-dl.org/downloads/%version/%name-%version.tar.gz.sig
Source3:        %name.keyring
# Generate with
# python3 devscripts/prepare_manpage.py youtube-dl.1.temp.md
# pandoc -f markdown -t rst -o youtube-dl.1.temp.rst youtube-dl.1.temp.md
# and hand editing until rst2man youtube-dl.1.temp.rst youtube.1 runs
Source4:        youtube-dl.1.temp.rst
# PATCH-FIX-UPSTREAM 30713-new-ceskatelevize.patch gh#ytdl-org/youtube-dl#30713 mcepl@suse.com
# Rewrite of the support for https://www.ceskatelevize.cz/
Patch0:         30713-new-ceskatelevize.patch
# PATCH-FEATURE-OPENSUSE no-pandoc-32bit.patch mcepl@suse.com
# 32bit architectures don't have pandoc
Patch1:         no-pandoc-32bit.patch
# PATCH-FIX-UPSTREAM fix-uploader-id-extraction.patch gh#ytdl-org/youtube-dl#31530 mcepl@suse.com
# Patch from gh#yt-dlp/yt-dlp@149eb0bbf34f
# Fix uploader_id extraction regexp
Patch2:         fix-uploader-id-extraction.patch
BuildRequires:  make >= 4
BuildRequires:  python3-devel
BuildRequires:  python3-xml
# For documentation
BuildRequires:  python3-docutils
BuildRequires:  python3-Pygments
BuildRequires:  zip
Requires:       ffmpeg
Requires:       python3
Requires:       python3-xml
BuildArch:      noarch

%description
youtube-dl is a command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

%package        bash-completion
Summary:        Bash completion for %name
Group:          System/Shells
Requires:       bash-completion
Supplements:    (youtube-dl and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %name.

%package        fish-completion
Summary:        Fish completion for %name
Group:          System/Shells
Requires:       fish
Supplements:    (youtube-dl and fish)
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %name.

%package        zsh-completion
Summary:        Zsh Completion for %name
Group:          System/Shells
Requires:       zsh
Supplements:    (youtube-dl and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %name.

%prep
%autosetup -p1 -n %name

cp --no-preserve=timestamps %{SOURCE4} .

%build
rm -f youtube-dl
PYTHON="%_bindir/python3" %make_build

%install
install -Dm 755 youtube-dl %buildroot/%_bindir/%name
install -Dm 644 youtube-dl.bash-completion %buildroot/%_datadir/bash-completion/completions/%name
install -Dm 644 youtube-dl.zsh %buildroot/%_datadir/zsh/site-functions/_%name
install -Dm 644 youtube-dl.fish %buildroot/%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 youtube-dl.1 %buildroot/%_mandir/man1/%name.1

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
