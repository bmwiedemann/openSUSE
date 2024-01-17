#
# spec file for package scdl
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


Name:           scdl
Version:        2.7.3
Release:        0
Summary:        Souncloud Music Downloader
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Other
URL:            https://github.com/flyingrub/scdl
Source:         https://files.pythonhosted.org/packages/source/s/scdl/scdl-%{version}.tar.gz
BuildRequires:  python3-clint
BuildRequires:  python3-docopt
BuildRequires:  python3-mutagen
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-termcolor
Requires:       python3-clint
Requires:       python3-docopt
Requires:       python3-mutagen
Requires:       python3-requests
Requires:       python3-termcolor
BuildArch:      noarch

%description
The program can download music from SoundCloud and set id3tag to the downloaded music.

%prep
%setup -q
sed -i '1s/^#!.*//' scdl/scdl.py
chmod -x README.md

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/scdl

%changelog
