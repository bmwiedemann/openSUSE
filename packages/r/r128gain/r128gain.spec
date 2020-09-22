#
# spec file for package r128gain
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           r128gain
Version:        1.0.3
Release:        0
Summary:        Fast audio loudness (ReplayGain / R128) scanner & tagger
License:        LGPL-2.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/desbma/r128gain
Source:         https://github.com/desbma/r128gain/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-crcmod >= 1.7
Requires:       python3-ffmpeg-python >= 0.2
Requires:       python3-future
Requires:       python3-mutagen >= 1.43
Requires:       python3-tqdm >= 4.28.1
BuildArch:      noarch

%description
Fast audio loudness (ReplayGain / R128) scanner & tagger.

%prep
%setup -q
sed -i -e '/^#!\//, 1d'  r128gain/__*

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

#%%check
#disable tests since a network connection is required to download mediafiles from wikimedia

%files
%license LICENSE
%doc README.md
%{_bindir}/r128gain
%{python3_sitelib}/r128gain*

%changelog
