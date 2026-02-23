#
# spec file for package yt-dlp
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


%if %{defined primary_python}
%define pythons %primary_python
%else
%if 0%{?sle_version} == 150700
%global pythons python313
%else
%global pythons python312
%endif
%endif

Name:           yt-dlp
Version:        2026.02.21
%define ejsver  0.5.0
Release:        0
Summary:        Enhanced fork of youtube-dl, a video site downloader for offline watching
License:        CC-BY-SA-3.0 AND SUSE-Public-Domain
Group:          Productivity/Networking/Web/Utilities
URL:            https://github.com/yt-dlp/yt-dlp
Source:         https://github.com/yt-dlp/yt-dlp/releases/download/%version/yt-dlp.tar.gz
Source2:        https://github.com/yt-dlp/ejs/releases/download/%ejsver/yt_dlp_ejs-%ejsver-py3-none-any.whl
Source9:        yt-dlp-rpmlintrc
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  make >= 4
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  zip
BuildArch:      noarch
Obsoletes:      yt-dlp-bash-completion < %version-%release
Provides:       yt-dlp-bash-completion = %version-%release
Obsoletes:      yt-dlp-fish-completion < %version-%release
Provides:       yt-dlp-fish-completion = %version-%release
Obsoletes:      yt-dlp-zsh-completion < %version-%release
Provides:       yt-dlp-zsh-completion = %version-%release
Requires:       %pythons-yt-dlp = %version
%define python_subpackage_only 1
%python_subpackages

%description
yt-dlp is a command-line program to retrieve videos from
YouTube.com and other video sites for later watching.

%package -n yt-dlp-youtube-dl
Summary:        Compat symlinks for youtube-dl
Requires:       yt-dlp
Provides:       youtube-dl
Conflicts:      youtube-dl

%description -n yt-dlp-youtube-dl
This package installs "youtube-dl" as a symlink to yt-dlp.

%package -n python-yt-dlp
Summary:        yt-dlp Python library
Group:          Development/Languages/Python
Requires:       ffmpeg
Recommends:     (deno or nodejs >= 20 or quickjs >= 20250913)
Suggests:       python-Brotli
Suggests:       python-certifi
Suggests:       python-mutagen
Suggests:       python-pycryptodomex
Suggests:       python-websockets

%description -n python-yt-dlp
The direct Python interface into yt-dlp.

%prep
%autosetup -p1 -n %name

# remove shebang
find . -type f -name "*.py" -exec sed -i '/^#!/d' {} +

# fix Leap 15.6 build w.r.t. python-hatchling
sed -e '/3\.14/d' -e '/^license\-files/d' \
    -i pyproject.toml

%build
rm -f youtube-dl yt-dlp
#
# A self-decompressing yt-dlp is built only when python_build is not
# exercised; else yt-dlp is a loader.
#
export PYTHON=$(type -P "%_bindir/python%{python_bin_suffix}" | xargs --no-run-if-empty readlink -f)
%pyproject_wheel
%make_build yt-dlp

%install
b="%buildroot"
%pyproject_install
ln -s yt-dlp "$b/%_bindir/youtube-dl"
rm -Rf "$b/%_datadir/doc"
# if you leave everything as-is, rpmlint complains about
# 	python312-yt-dlp.noarch: W: files-duplicate
# 	/usr/lib/python3.12/site-packages/yt_dlp/utils/__pycache__/progress.cpython-312.pyc
# 	/usr/lib/python3.12/site-packages/yt_dlp/utils/__pycache__/progress.cpython-312.opt-1.pyc
# if you add fdupes, rpmlint complains about
# 	python312-yt-dlp.noarch: E: python-bytecode-inconsistent-mtime
# 	/usr/lib/python3.12/site-packages/yt_dlp/extractor/__pycache__/screencastomatic.cpython-312.pyc
# 	2024-09-29T18:11:02
# 	/usr/lib/python3.12/site-packages/yt_dlp/extractor/screencastomatic.py
# 	2024-09-29T18:11:01

ejs="$(grep ^EJS_VERSION Makefile | perl -pe 's{^.*?=\s+(.*)}{$1}')"
%{python_expand #
d="$b/%$python_sitelib/"
mkdir -p "$d"
cd "$d"
unzip "%_sourcedir/yt_dlp_ejs-$ejs-py3-none-any.whl"
}

%files -n yt-dlp
%license LICENSE
%doc README.md
%_bindir/%name
%_mandir/man1/%name.1%ext_man
%_datadir/bash-completion/
%_datadir/fish/
%_datadir/zsh/

%files -n yt-dlp-youtube-dl
%_bindir/youtube-dl

%files %{python_files yt-dlp}
%python_sitelib/y*

%changelog
