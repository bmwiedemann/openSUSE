#
# spec file for package grml-zsh-config
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


Name:           grml-zsh-config
Version:        0.19.5
Release:        0
Summary:        Zsh config used by grml
License:        GPL-2.0-only
URL:            https://grml.org/zsh/
Source:         https://deb.grml.org/pool/main/g/grml-etc-core/grml-etc-core_%{version}.tar.gz
BuildRequires:  python38-txt2tags
Requires:       grep
Requires:       procps
Requires:       sed
Requires:       zsh
BuildArch:      noarch

%description
Zsh configuration files used by grml.

%prep
ls
%setup -q -n grml-etc-core-%{version}

%build
cd doc
%make_build

%install
install -D -m644 etc/skel/.zshrc "%{buildroot}%{_sysconfdir}/skel/.zshrc"
install -D -m644 etc/zsh/keephack "%{buildroot}%{_sysconfdir}/zsh/keephack"
install -D -m644 etc/zsh/zshrc "%{buildroot}%{_sysconfdir}/zsh/zshrc"
install -D -m644 doc/grmlzshrc.5 "%{buildroot}%{_mandir}/man5/grmlzshrc.5"

%files
%doc README.md
%doc %{_sysconfdir}/zsh
%config %{_sysconfdir}/skel/.zshrc
%config %{_sysconfdir}/zsh/keephack
%config %{_sysconfdir}/zsh/zshrc
%{_mandir}/man5/grmlzshrc.5%{?ext_man}

%changelog
