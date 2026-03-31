#
# spec file for package python-lastversion
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-lastversion
Version:        3.6.10
Release:        0
Summary:        Find the latest stable release version of an arbitrary project
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/dvershinin/lastversion
Source:         https://github.com/dvershinin/lastversion/archive/v%{version}.tar.gz#/lastversion-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-CacheControl
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-beautifulsoup4
Requires:       python-distro
Requires:       python-feedparser
Requires:       python-packaging
Requires:       python-python-dateutil
Requires:       python-requests >= 2.16.0
Requires:       python-tqdm
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module CacheControl}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module feedparser}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest >= 4.4.0}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests >= 2.16.0}
BuildRequires:  %{python_module tqdm}
# /SECTION
%python_subpackages

%description
lastversion is a command-line tool and Python library to find the latest
stable release version of an arbitrary project. It supports GitHub, GitLab,
Bitbucket, PyPI, Mercurial, SourceForge, WordPress and more, handling
inconsistent versioning schemes, pre-release detection, and asset filtering.

%prep
%setup -q -n lastversion-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lastversion
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative lastversion

%postun
%python_uninstall_alternative lastversion

%check
# Mosts tests require network connection
%pytest -k "test_version_parse"

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/lastversion
%{python_sitelib}/lastversion
%{python_sitelib}/lastversion-%{version}*

%changelog
