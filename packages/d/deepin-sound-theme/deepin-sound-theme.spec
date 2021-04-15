#
# spec file for package deepin-sound-theme
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 PERLUR Group
# Copyright (c) 2018 Mark Stopka <mark.stopka@perlur.cloud>
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
#

Name:           deepin-sound-theme
Version:        15.10.3
Release:        0
Summary:        Deepin sound theme
License:        GPL-3.0
URL:            https://github.com/linuxdeepin/deepin-sound-theme
Group:          System/GUI/Other
Source0:        https://github.com/linuxdeepin/deepin-sound-theme/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Sound files for the Deeping Desktop Environment.

%prep
%setup -q

%build

%install
%make_install

%files
%defattr(-,root,root,-)
%doc README.md LICENSE CHANGELOG.md
%dir %{_datadir}/sounds/deepin/
%dir %{_datadir}/sounds/deepin/stereo/
%{_datadir}/sounds/deepin/index.theme
%{_datadir}/sounds/deepin/stereo/*.wav

%changelog
