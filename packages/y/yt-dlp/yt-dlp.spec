#
# spec file for package yt-dlp
#
# Copyright (c) 2024 SUSE LLC
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


%define skip_python2 1
%define skip_python36 1
%define skip_python37 1
%{?sle15_python_module_pythons}
Name:           yt-dlp
Version:        2024.07.01
Release:        0
Summary:        Enhanced fork of youtube-dl, a video site downloader for offline watching
License:        CC-BY-SA-3.0 AND SUSE-Public-Domain
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/yt-dlp/yt-dlp
Source:         https://github.com/yt-dlp/yt-dlp/releases/download/%version/yt-dlp.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  make >= 4
BuildRequires:  python-rpm-macros
BuildRequires:  zip
BuildArch:      noarch
# %%primary_python not available in Leap yet
Requires:       %(echo %{python_module yt-dlp} | perl -pe 's{.* }{}g')
%define python_subpackage_only 1
%python_subpackages

%description
yt-dlp is a command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

%package -n yt-dlp-bash-completion
Summary:        Bash completion for yt-dlp
Group:          System/Shells
Requires:       bash-completion
Supplements:    (yt-dlp and bash-completion)

%description -n yt-dlp-bash-completion
Bash command line completion support for yt-dlp.

%package -n yt-dlp-fish-completion
Summary:        Fish completion for yt-dlp
Group:          System/Shells
Requires:       fish
Supplements:    (yt-dlp and fish)

%description -n yt-dlp-fish-completion
Fish command line completion support for yt-dlp.

%package -n yt-dlp-zsh-completion
Summary:        Zsh Completion for yt-dlp
Group:          System/Shells
Requires:       zsh
Supplements:    (yt-dlp and zsh)

%description -n yt-dlp-zsh-completion
ZSH command line completion support for yt-dlp.

%package -n python-yt-dlp
Summary:        yt-dlp Python library
Group:          Development/Languages/Python
Requires:       ffmpeg
Suggests:       python-Brotli
Suggests:       python-certifi
Suggests:       python-mutagen
Suggests:       python-pycryptodomex
Suggests:       python-websockets

%description -n python-yt-dlp
The direct Python interface into yt-dlp.

%prep
%autosetup -p1 -n %name

%build
rm -f youtube-dl yt-dlp
#
# A self-decompressing yt-dlp is built only when python_build is not
# exercised; else yt-dlp is a loader.
#
%pyproject_wheel
%make_build yt-dlp

%install
b="%buildroot"
%pyproject_install
%fdupes %buildroot/usr
rm -Rf "$b/%_datadir/doc"

%files -n yt-dlp
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

%files %{python_files yt-dlp}
%python_sitelib/y*

%changelog
