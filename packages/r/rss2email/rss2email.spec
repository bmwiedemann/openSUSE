#
# spec file for package rss2email
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        3.14
Release:        0
Summary:        Receive RSS feeds by email
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/rss2email/rss2email
Source:         https://github.com/rss2email/rss2email/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-tests.patch
# PATCH-FEATURE-UPSTREAM 213-http-header-config.patch gh#rss2email/rss2email!213 mcepl@suse.com
# add http-header config option to pass custom HTTP headers
Patch1:         213-http-header-config.patch
# PATCH-FEATURE-UPSTREAM dynamic-version-number.patch gh#rss2email/rss2email!284 mcepl@suse.com
# pyproject.toml should use dynamic version number derived from rss2email/ __version__
Patch2:         dynamic-version-number.patch
Patch3:         https://patch-diff.githubusercontent.com/raw/rss2email/rss2email/pull/279.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros
BuildRequires:  python3-feedparser >= 6.0.0
BuildRequires:  python3-html2text >= 2025.4.15
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-feedparser >= 6.0.0
Requires:       python3-html2text >= 2025.4.15
Provides:       python3-rss2email = %version-%release
Obsoletes:      python3-rss2email < %version-%release
BuildArch:      noarch
%{?python_enable_dependency_generator}

%description
Lets users receive news from RSS feeds in email. Intended to be run from
a crontab, watches RSS feeds and sends formatted email messages for new
items.

%prep
%autosetup -p1

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
install -Dm644 r2e.1 %{buildroot}%{_mandir}/man1/r2e.1
%fdupes %{buildroot}%{python3_sitelib}

%check
pushd test
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONDONTWRITEBYTECODE=1
python3 -m unittest discover -v
popd

%files
%license COPYING
%doc AUTHORS CHANGELOG README.rst
%{_bindir}/r2e
%{_mandir}/man1/r2e.1%{?ext_man}
%{python3_sitelib}/rss2email
%{python3_sitelib}/rss2email-%{version}*-info

%changelog
