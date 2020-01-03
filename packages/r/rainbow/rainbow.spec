#
# spec file for package rainbow
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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

Name:           rainbow
Version:        2.7.1
Release:        0
Summary:        Colorize commands output or STDIN using patterns
License:        GPL-3.0-only
Group:          System/Console
URL:            https://github.com/nicoulaj/rainbow
Source:         https://github.com/nicoulaj/rainbow/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Jinja2
BuildRequires:  python3-setuptools
BuildArch:      noarch

%description
Easily colorize logs or commands output using patterns.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Console
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%package zsh-completion
Summary:        ZSH completion for %{name}
Group:          System/Console
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -q
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|g' scripts/rainbow

%build
%python3_build

%install
%python3_install
install -Dm0644 build/completion/rainbow %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm0644 build/completion/_rainbow %{buildroot}%{_sysconfdir}/zsh_completion.d/%{name}
install -Dm0644 build/man/rainbow.1 %{buildroot}%{_mandir}/man1/%{name}.1
%fdupes %{buildroot}%{python3_sitelib}

%files
%license COPYING
%doc README.rst
%{_bindir}/rainbow
%{python3_sitelib}/*
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_sysconfdir}/zsh_completion.d
%config %{_sysconfdir}/zsh_completion.d/%{name}

%changelog
