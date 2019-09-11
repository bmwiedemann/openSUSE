#
# spec file for package suru-plus-dark-icon-theme
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
#


Name:           suru-plus-dark-icon-theme
Version:        25.1
Release:        0
Summary:        Suru Plus Dark icon theme
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/gusbemacbe/suru-plus-dark
Source:         https://github.com/gusbemacbe/suru-plus-dark/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
BuildArch:      noarch

%description
A cyberpunkish, elegant, futuristic, Papirus-like icon theme.

%prep
%setup -q -n suru-plus-dark-%{version}

%build
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}%{_datadir}/icons/Suru++-Dark

%files
%license COPYING LICENSE
%doc AUTHORS CREDITS Makefile
%{_datadir}/icons/Suru++-Dark

%changelog
