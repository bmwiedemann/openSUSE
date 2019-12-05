#
# spec file for package python-click-man
#
# Copyright (c) 2019 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-click-man
Version:        0.3.0
Release:        0
Summary:        Automate generation of man pages for python click applications
License:        MIT
URL:            https://github.com/click-contrib/click-man
Source:         https://github.com/click-contrib/click-man/archive/v%{version}.tar.gz
Patch1:         get-short-help.patch
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sure}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
BuildArch:      noarch
%python_subpackages

%description
Automate generation of man pages for Python Click applications.

%prep
%setup -q -n click-man-%{version}
%patch1 -p1

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/click-man

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative click-man

%postun
%python_uninstall_alternative click-man

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/click-man
%{python_sitelib}/*

%changelog
