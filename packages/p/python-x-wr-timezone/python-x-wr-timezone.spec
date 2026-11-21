#
# spec file for package python-x-wr-timezone
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-x-wr-timezone
Version:        2.0.1
Release:        0
Summary:        Convert ICS calendars using X-WR-TIMEZONE to RFC 5545
License:        LGPL-3.0-or-later
URL:            https://github.com/pycalendar/x-wr-timezone
# The PyPI sdist lacks test/conftest.py and the test/calendars fixtures
Source:         https://github.com/pycalendar/x-wr-timezone/archive/refs/tags/v%{version}.tar.gz#/x-wr-timezone-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module icalendar >= 6.1.0}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-click}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module restructuredtext_lint}
BuildRequires:  %{python_module tzdata}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click
Requires:       python-icalendar >= 6.1.0
Requires:       python-tzdata
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Repair Google Calendar - module and program make ICS/iCalendar files using X-WR-TIMEZONE compatible with the RFC 5545 standard.

%prep
%autosetup -p1 -n x-wr-timezone-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/x-wr-timezone
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH=$(pwd):$PATH
%{python_expand ln -sf %{buildroot}%{_bindir}/x-wr-timezone-%{$python_bin_suffix} x-wr-timezone
PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -vv --x-wr-timezone=all
}

%post
%python_install_alternative x-wr-timezone

%postun
%python_uninstall_alternative x-wr-timezone

%files %{python_files}
%python_alternative %{_bindir}/x-wr-timezone
%{python_sitelib}/x_wr_timezone.py
%pycache_only %{python_sitelib}/__pycache__/x_wr_timezone*.pyc
%{python_sitelib}/x_wr_timezone-%{version}.dist-info

%changelog
