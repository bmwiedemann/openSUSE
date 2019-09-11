#
# spec file for package imgp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           imgp
Version:        2.6
Release:        0
Summary:        Image resizer and rotator
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Convertors
Url:            https://github.com/jarun/imgp
Source0:        https://github.com/jarun/imgp/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
Requires:       python3-Pillow
Requires:       python3-base
BuildArch:      noarch

%description
A command line image resizer and rotator for JPEG and PNG images
based on python-Pillow.

%package        bash-completion
Version:        %{version}
Release:        0
Summary:        Bash Completion for %{name}
Group:          Productivity/Graphics/Convertors
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(imgp:bash)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %{name}.

%package        fish-completion
Version:        %{version}
Release:        0
Summary:        Fish Completion for %{name}
Group:          Productivity/Graphics/Convertors
Requires:       %{name} = %{version}
Supplements:    packageand(imgp:fish)
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %{name}.

%package        zsh-completion
Summary:        ZSH Completion for %{name}
Group:          Productivity/Graphics/Convertors
Requires:       %{name} = %{version}
Supplements:    packageand(imgp:zsh)
BuildArch:      noarch

%description    zsh-completion
ZSH command line completion support for %{name}.

%prep
%setup -q

%build
# not required

%install
%make_install PREFIX=%{_prefix} DOCDIR=%{buildroot}%{_defaultdocdir}/%{name}
mkdir -pv %{buildroot}%{_datadir}/bash-completion/completions \
          %{buildroot}%{_datadir}/fish/completions \
          %{buildroot}%{_datadir}/zsh/site-functions
install -m0644 auto-completion/bash/%{name}-completion.bash -t %{buildroot}%{_datadir}/bash-completion/completions
install -m0644 auto-completion/fish/%{name}.fish -t %{buildroot}%{_datadir}/fish/completions
install -m0644 auto-completion/zsh/_%{name} -t %{buildroot}%{_datadir}/zsh/site-functions

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}-completion.bash

%files fish-completion
%{_datadir}/fish/completions/%{name}.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%changelog
