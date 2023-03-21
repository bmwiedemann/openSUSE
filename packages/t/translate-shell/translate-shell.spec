#
# spec file for package translate-shell
#
# Copyright (c) 2023 SUSE LLC
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


Name:           translate-shell
Version:        0.9.7.1
Release:        0
Summary:        Command line translator using various online services as backends
License:        Unlicense
Group:          Productivity/Networking/Web/Frontends
URL:            https://www.soimort.org/translate-shell
Source:         https://github.com/soimort/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  emacs-nox
BuildRequires:  gawk >= 4.0
BuildRequires:  rlwrap
Requires:       bash
Requires:       gawk >= 4.0
Recommends:     curl
Recommends:     fribidi
Recommends:     less
Recommends:     rlwrap
Suggests:       emacs-nox
Suggests:       mpv
BuildArch:      noarch

%description
Translate Shell is a command-line translator powered by
Google Translate, Bing Translator, Yandex.Translate and DeepL
traslator. It gives access to online translation services
from a terminal.

%prep
%setup -q

%build
%make_build

%install
%make_install PREFIX=%{_prefix}
chmod -x %{buildroot}%{_mandir}/man1/trans.1
sed -i 's|%{_bindir}/env bash|/bin/bash|' %{buildroot}%{_bindir}/trans

%files
%license LICENSE
%doc CONTRIBUTING.md README.md WAIVER
%{_bindir}/trans
%{_mandir}/man1/trans.1%{?ext_man}

%changelog
