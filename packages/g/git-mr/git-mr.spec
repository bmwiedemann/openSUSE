#
# spec file for package git-mr
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Stasiek Michalski <stasiek@michalski.cc>.
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


Name:           git-mr
Version:        1.0.0
Release:        0
Summary:        Checkout GitLab merge requests / GitHub pull requests locally
License:        MIT
URL:            https://gitlab.com/glensc/%{name}
Source0:        https://gitlab.com/glensc/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
Conflicts:      git-extras
Provides:       git-pr
BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup

%build
# Not needed

%install
install -m 755 -Dt %{buildroot}%{_bindir} git-{mr,pr}
%fdupes -s %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/git-mr
%{_bindir}/git-pr

%changelog
