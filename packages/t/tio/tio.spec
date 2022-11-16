#
# spec file for package tio
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


Name:           tio
Version:        2.3
Release:        0
Summary:        Simple TTY terminal I/O application
License:        GPL-2.0-or-later
Group:          Hardware/Modem
URL:            https://tio.github.io/
Source:         https://github.com/tio/tio/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig(inih)

%description
Tio is a simple TTY terminal application which features a straightforward
commandline interface to easily connect to TTY devices for basic input/output.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Hardware/Modem
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q

%build
%meson -Dbashcompletiondir=%{_datadir}/bash-completion/completions/
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
