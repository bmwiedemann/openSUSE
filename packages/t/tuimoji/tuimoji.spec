#
# spec file for package tuimoji
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


%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
Name:           tuimoji
Version:        1.0.0
Release:        0
Summary:        Terminal based emoji chooser
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/Fingel/tuimoji
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python3-setuptools
Requires:       python3-urwid
Requires:       xclip
BuildArch:      noarch

%description
moji is a terminal based emoji chooser for *nix. With tuimoji you can search and browse emojis and copy them to your clipboard without ever leaving the comfort of your terminal.

%prep
%setup -q

%build
%python3_build

%install
%python3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/tuimoji
%{python_sitelib}/*

%changelog
