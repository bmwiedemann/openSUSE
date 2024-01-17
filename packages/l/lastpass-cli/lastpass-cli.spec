#
# spec file for package lastpass-cli
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


Name:           lastpass-cli
Version:        1.3.4
Release:        0
Summary:        LastPass command line interface tool
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://github.com/LastPass/lastpass-cli
Source:         https://github.com/lastpass/lastpass-cli/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-Mark-global-variable-as-extern.patch gh#lastpass/lastpass-cli#532
Patch0:         0001-Mark-global-variable-as-extern.patch
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
Recommends:     bash-completion
Recommends:     pinentry
Recommends:     xclip

%description
LastPass is a freemium password management service which stores encrypted
passwords in the cloud. This package provided it's command line interface
tool.

%prep
%autosetup -p 1

%build
%cmake \
  -DTEST_BUILD=ON
%make_jobs all doc-man

%install
%cmake_install install-doc
install -Dpm  0644 contrib/lpass_bash_completion \
  %{buildroot}%{_datadir}/bash-completion/completions/lpass
install -Dpm 0644 contrib/lpass_zsh_completion \
  %{buildroot}%{_datadir}/zsh/site-functions/_lpass
install -Dpm 0644 contrib/completions-lpass.fish \
  %{buildroot}%{_datadir}/fish/completions/completions-lpass.fish

%check
%make_build test

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/lpass
%{_mandir}/man1/lpass.1%{?ext_man}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/lpass
%dir %{_datadir}/fish
%dir %{_datadir}/fish/completions
%{_datadir}/fish/completions/completions-lpass.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_lpass

%changelog
