#
# spec file for package urh
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           urh
Version:        2.8.8
Release:        0
Summary:        Tool for investigating unknown wireless protocols
License:        GPL-3.0-only
Group:          Productivity/Hamradio/Other
URL:            https://github.com/jopohl/urh
Source:         https://github.com/jopohl/urh/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  limesuite-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-numpy
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-qt5
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(libairspy)
BuildRequires:  pkgconfig(libbladeRF)
BuildRequires:  pkgconfig(libhackrf)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(uhd)
Requires:       hicolor-icon-theme
Requires:       python3-Cython
Requires:       python3-numpy
Requires:       python3-psutil
Requires:       python3-pyzmq
Requires:       python3-qt5
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
Recommends:     inspectrum
Recommends:     rfcat
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-PyAudio
%endif
%if 0%{?suse_version} >= 1500
Requires:       python3-PyAudio
%endif

%description
The Universal Radio Hacker is a software for investigating unknown wireless
protocols.

%prep
%setup -q

%build
%python3_build \
  --with-airspy \
  --with-bladerf \
  --with-hackrf \
  --with-limesdr \
  --with-rtlsdr \
  --with-usrp

%install
%python3_install
%fdupes %{buildroot}%{python3_sitearch}
install -Dpm 0644 data/icons/appicon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/urh.svg
%suse_update_desktop_file -i -r urh "Network;HamRadio"

%files
%license LICENSE
%doc README.md
%{_bindir}/urh
%{_bindir}/urh_cli
%{_datadir}/icons/hicolor/scalable/apps/urh.svg
%{_datadir}/applications/urh.desktop
%{python3_sitearch}/urh
%{python3_sitearch}/urh-%{version}-py%{py3_ver}.egg-info

%changelog
