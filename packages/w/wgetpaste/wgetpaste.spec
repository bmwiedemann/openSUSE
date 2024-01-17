#
# spec file for package wgetpaste
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


Name:           wgetpaste
Version:        2.33
Release:        0
Summary:        Command-line interface to various pastebins
License:        MIT
Group:          Productivity/Other
URL:            https://github.com/zlin/wgetpaste
Source0:        https://github.com/zlin/wgetpaste/releases/download/%{version}/wgetpaste-%{version}.tar.xz
Source1:        https://github.com/zlin/wgetpaste/releases/download/%{version}/wgetpaste-%{version}.tar.xz.sig
Source2:        services.conf
Source3:        wgetpaste.keyring
Requires:       bash
Requires:       coreutils
Requires:       wget
Recommends:     xclip
BuildArch:      noarch

%description
Command-line interface to communicate with various pastebin services.

%prep
%setup -q

%build
# do nothing

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.d/services.conf
install -D -m 0644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%dir %{_sysconfdir}/%{name}.d/
%dir %{_datadir}/zsh/site-functions/
%dir %{_datadir}/zsh/
%{_datadir}/zsh/site-functions/_%{name}
%config %{_sysconfdir}/%{name}.d/services.conf
%{_bindir}/%{name}

%changelog
