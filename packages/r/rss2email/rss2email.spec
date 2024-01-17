#
# spec file for package rss2email
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           rss2email
Version:        3.14
Release:        0
Summary:        Receive RSS feeds by email
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/rss2email/rss2email
Source:         https://github.com/rss2email/rss2email/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module feedparser >= 6.0.0}
BuildRequires:  %{python_module html2text >= 3.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros
Requires:       python-feedparser >= 6.0.0
Requires:       python-html2text >= 3.0.1
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%{?python_enable_dependency_generator}
%python_subpackages

%description
Lets users receive news from RSS feeds in email. Intended to be run from
a crontab, watches RSS feeds and sends formatted email messages for new
items.

%prep
%autosetup

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/r2e
install -Dm644 r2e.1 %{buildroot}%{_mandir}/man1/r2e.1
%python_clone -a %{buildroot}%{_mandir}/man1/r2e.1

%check
pushd test
%pyunittest --verbose
popd

%post
%python_install_alternative r2e r2e.1

%postun
%python_uninstall_alternative r2e r2e.1

%files %{python_files}
%license COPYING
%doc AUTHORS CHANGELOG README.rst
%dir %{python_sitelib}/rss2email
%dir %{python_sitelib}/rss2email/__pycache__
%dir %{python_sitelib}/rss2email/post_process
%dir %{python_sitelib}/rss2email/post_process/__pycache__
%{python_sitelib}/rss2email/*py
%{python_sitelib}/rss2email/post_process/*py
%{python_sitelib}/rss2email-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/rss2email/__pycache__/*
%pycache_only %{python_sitelib}/rss2email/post_process/__pycache__/*
%python_alternative %{_bindir}/r2e
%python_alternative %{_mandir}/man1/r2e.1%{?ext_man}

%changelog
