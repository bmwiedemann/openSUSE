#
# spec file for package direnv
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


%define gopackagepath github.com/direnv/direnv
Name:           direnv
Version:        2.23.1
Release:        0
Summary:        Environment switcher for shells
License:        MIT
Group:          Productivity/File utilities
URL:            http://direnv.net/
Source:         https://github.com/direnv/direnv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go >= 1.5
BuildRequires:  make

%description
direnv knows how to hook into bash, zsh, tcsh and fish shell to load
or unload environment variables depending on the current directory.
This allows to have project-specific environment variables and not
clutter the "~/.profile" file.

%prep
%setup -q
mkdir -p "$HOME/go/src/$(dirname "%{gopackagepath}")"
cd ..
ln -sf `pwd`/%{name}-%{version} "$HOME/go/src/%{gopackagepath}"

%build
cd "$HOME/go/src/%{gopackagepath}"
make %{?_smp_mflags}

%install
cd "$HOME/go/src/%{gopackagepath}"
%make_install DESTDIR=%{buildroot}%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man1/%{name}-stdlib.1%{ext_man}
%{_mandir}/man1/%{name}.toml.1%{ext_man}
%{_mandir}/man1/%{name}-fetchurl.1%{ext_man}

%changelog
