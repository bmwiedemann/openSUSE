#
# spec file for package scrot
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           scrot
Version:        2.0.0
Release:        0
Summary:        Screenshot Capture Utility
License:        SUSE-Scrot
URL:            https://github.com/resurrecting-open-source-projects/scrot
Source:         https://github.com/resurrecting-open-source-projects/scrot/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(imlib2) >= 1.11.0
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite) >= 0.2.0
BuildRequires:  pkgconfig(xfixes) >= 5.0.1
BuildRequires:  pkgconfig(xrandr) >= 1.5
Requires:       imlib2

%description
A nice and straightforward screen capture utility implementing
the dynamic loaders of imlib2.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}

%package zsh-completion
Summary:        ZSH Completion for %{name}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/scrot

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files zsh-completion
%{_datadir}/zsh

%changelog
