#
# spec file for package redminecli
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           redminecli
Version:        1.3.0
Release:        0
Summary:        Command line interface for Redmine
License:        CECILL-B
Group:          Development/Tools/Other
URL:            https://github.com/egegunes/redmine-cli
Source:         https://github.com/egegunes/redmine-cli/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-click
Requires:       python3-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-click
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
# /SECTION

%description
A command line interface for Redmine.

%package -n redminecli-bash-completion
Summary:        Bash completion for redminecli
Group:          Development/Tools/Other
BuildRequires:  bash-completion
Requires:       bash-completion
Requires:       redminecli
Supplements:    (%{name} and bash-completion)

%description -n redminecli-bash-completion
This package contains the bash completion command for redminecli.

%prep
%setup -q -n redmine-cli-%{version}

%build
%python3_build

%install
%python3_install
# Don't install testsuite to the sitelib
rm -rf %{buildroot}%{python3_sitelib}/tests
%fdupes %{buildroot}%{python3_sitelib}
install -Dpm 0644 bash-completion.sh %{buildroot}%{_datadir}/bash-completion/completions/redminecli

%check
python3 -m pytest

%files
%license LICENSE
%doc README.md
%{_bindir}/redmine
%{python3_sitelib}/*

%files -n redminecli-bash-completion
%{_datadir}/bash-completion/completions/redminecli

%changelog
