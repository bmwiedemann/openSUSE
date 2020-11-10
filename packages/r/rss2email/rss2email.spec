#
# spec file for package rss2email
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


Name:           rss2email
Version:        3.12.2
Release:        0
Summary:        Receive RSS feeds by email
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/rss2email/rss2email
Source:         https://github.com/rss2email/rss2email/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         rss2email-3.12.2-feedparser-6.patch
BuildRequires:  %{python_module feedparser >= 6.0.0}
BuildRequires:  %{python_module html2text >= 3.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  python-rpm-generators
BuildArch:      noarch
%{?python_enable_dependency_generator}

%description
Lets users receive news from RSS feeds in email. Intended to be run from
a crontab, watches RSS feeds and sends formatted email messages for new
items.

%prep
%autosetup -p1

%build
%python_build

%install
%python_install
install -Dm644 r2e.1 %{buildroot}/%{_mandir}/man1/r2e.1

%check
pushd test
%pyunittest --verbose
popd

%files
%license COPYING
%doc AUTHORS CHANGELOG README.rst
%{python3_sitelib}/rss2email
%{python3_sitelib}/rss2email-%{version}-py*.egg-info
%{_bindir}/r2e
%{_mandir}/*/r2e.1%{?ext_man}

%changelog
