#
# spec file for package flac2all
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           flac2all
Version:        5.1
Release:        0
Summary:        A multithreaded FLAC to MP3/OGG/FLAC batch converter
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://github.com/ZivaVatra/flac2all
Source:         https://github.com/ZivaVatra/flac2all/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-Bugfix-for-summary.patch
Patch1:         0002-Copy-logic-fixes.patch
Patch2:         0003-Fixed-to-logfile-output.patch
Patch3:         0004-Updated-clustered-mode-to-match-new-summary-logic.patch
Patch4:         0005-Copy-logic-fix-for-legacy-mode.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-curses
Recommends:     vorbis-tools
Suggests:       fdkaac
Suggests:       lame
Suggests:       opus-tools >= 0.1.7
BuildArch:      noarch

%description
Flac2All is a multi-threaded script that will convert your collection of
FLAC files into either Ogg Vorbis, MP3 (with the Lame encoder), or FLAC,
complete with any tags and identical file/folder structure.

%prep
%setup -q
%autopatch -p1

%build
## drop shebang
sed -i -e '/^#!\//, 1d' flac2all_pkg/*.py
echo %{version} > flac2all_pkg/version
%python3_build

%install
%python3_install
%fdupes %{buildroot}/%{python3_sitelib}

%check
# disabled for now since test needs sample FLAC files and encoders which are not available on OBS
#python3 setup.py test

%files
%license LICENCE
%doc CHANGES.md README.md USAGE.md USAGE-CLUSTERED.md
%{_bindir}/flac2all
%{python3_sitelib}/flac2all*

%changelog
