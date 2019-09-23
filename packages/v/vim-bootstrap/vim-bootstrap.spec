#
# spec file for package vim-bootstrap
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

%global provider        github
%global provider_tld    com
%global project         avelino
%global repo            vim-bootstrap
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           %{repo}
Version:        1.0+git7b40d33
Release:        0
Summary:        Vim Bootstrap is a vimrc generator
License:        MIT
Group:          Development/Tools/Other
Url:            https://github.com/avelino/vim-bootstrap
Source:         %{name}-%{version}.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  git
BuildRequires:  sudo
BuildRequires:  xz
Requires:       git
Requires:       curl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%{go_nostrip}
%{go_provides}

%description
Vim Bootstrap is generator provides a simple method of generating a .vimrc configuration for vim, NeoVim, NeoVim-Qt, MacVim and GVim.

%prep
%autosetup -n %{name}-%{version}

%build
%goprep %{import_path}
%gobuild ...

%install
%{goinstall}
%{gosrc}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_bindir}/vim-bootstrap
%{go_contribsrcdir}
%{go_contribdir}


%changelog
