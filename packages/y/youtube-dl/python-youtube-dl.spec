#
# spec file for package python-youtube-dl
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


%define modname youtube-dl
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-youtube-dl
Version:        2020.11.01.1
Release:        0
Summary:        A Python module for downloading from video sites for offline watching
License:        SUSE-Public-Domain AND CC-BY-SA-3.0
Group:          Development/Languages/Python
URL:            https://yt-dl.org/
#Git-Clone:     https://github.com/ytdl-org/youtube-dl
Source:         http://youtube-dl.org/downloads/%version/%modname-%version.tar.gz
Source2:        http://youtube-dl.org/downloads/%version/%modname-%version.tar.gz.sig
Source3:        %modname.keyring
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       ffmpeg
Requires:       python-xml
BuildArch:      noarch
%python_subpackages

%description
youtube-dl is a python module to retrieve videos from
YouTube.com and other video sites for later watching.

%prep
%autosetup -n %modname

%build
# remove shebang
sed -e '1d' -i youtube_dl/__init__.py youtube_dl/__main__.py \
               youtube_dl/YoutubeDL.py youtube_dl/utils.py
%python_build

%install
%python_install
rm -rf %buildroot/%_bindir/youtube-dl %buildroot/%_bindir \
       %buildroot/%_prefix/%_sysconfdir \
       %buildroot/%_datadir %buildroot/%_mandir
%python_expand %fdupes -s %buildroot/%{$python_sitelib}

%files %python_files
%license LICENSE
%doc README.txt
%python_sitelib/youtube_dl
%python_sitelib/youtube_dl-*-py%python_version.egg-info

%changelog
