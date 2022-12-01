#
# spec file for package direnv
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


%define gopackagepath github.com/direnv/direnv
Name:           direnv
Version:        2.32.1
Release:        0
Summary:        Environment switcher for shells
License:        MIT
Group:          Productivity/File utilities
URL:            https://direnv.net/
Source0:        https://github.com/direnv/direnv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  fish
BuildRequires:  go >= 1.6
BuildRequires:  make

%description
direnv knows how to hook into bash, zsh, tcsh and fish shell to load
or unload environment variables depending on the current directory.
This allows to have project-specific environment variables and not
clutter the "~/.profile" file.

%prep
%setup -q -a 1

%build
%make_build PREFIX=%{_prefix} \
%ifnarch ppc64
  GO_BUILD_FLAGS="-buildmode=pie"
%endif

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-stdlib.1%{?ext_man}
%{_mandir}/man1/%{name}.toml.1%{?ext_man}
%{_mandir}/man1/%{name}-fetchurl.1%{?ext_man}
# Fish environment config
%{_datadir}/fish/vendor_conf.d/direnv.fish

%changelog
