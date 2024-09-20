#
# spec file for package scdl
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


%define pythons python3
Name:           scdl
Version:        2.12.1
Release:        0
Summary:        Souncloud Music Downloader
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Other
URL:            https://github.com/scdl-org/scdl
Source:         https://files.pythonhosted.org/packages/source/s/scdl/scdl-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       ffmpeg
Requires:       python3-docopt-ng
Requires:       python3-filelock >= 3.0
Requires:       python3-mutagen >= 1.45
Requires:       python3-pathvalidate
Requires:       python3-requests
Requires:       python3-soundcloud-v2 >= 1.5.2
Requires:       python3-termcolor
Requires:       python3-tqdm
BuildArch:      noarch

%description
The program can download music from SoundCloud and set id3tag to the downloaded music.

%prep
%setup -q
sed -i '1s/^#!.*//' scdl/scdl.py
chmod -x README.md

%build
%pyproject_wheel

%install
%pyproject_install
# do not install tests
rm -r %{buildroot}%{python3_sitelib}/tests
%fdupes %{buildroot}%{python3_sitelib}

%check
exit 0

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/scdl
%{python3_sitelib}/scdl-%{version}.dist-info
%{_bindir}/scdl

%changelog
