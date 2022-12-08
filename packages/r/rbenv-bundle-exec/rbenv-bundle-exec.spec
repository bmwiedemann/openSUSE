#
# spec file for package rbenv-bundle-exec
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


Name:           rbenv-bundle-exec
Version:        1.0.0
Release:        0
BuildArch:      noarch
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/maljub01/rbenv-bundle-exec
Summary:        The one true plugin for rbenv bundler integration
Source0:        https://github.com/maljub01/rbenv-bundle-exec/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  rbenv
Requires:       rbenv

%description
This plugin makes rbenv "bundle exec" your ruby executables so you don't have to.

%prep
%setup -q

%build

%install
install -Dm0644 etc/rbenv.d/exec/bundle-exec.bash %{buildroot}/usr/lib/rbenv/hooks/exec/bundle-exec.bash

%files
%license LICENSE
%doc README.md
/usr/lib/rbenv

%changelog
