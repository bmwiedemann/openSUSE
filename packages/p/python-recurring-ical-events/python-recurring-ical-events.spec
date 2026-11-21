#
# spec file for package python-recurring-ical-events
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2026 LISA GmbH, Bingen, Germany
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

%define distname recurring_ical_events

Name:           python-recurring-ical-events
Version:        3.8.2
Release:        0
Summary:        Recurring ICal events
License:        LGPL-3.0-or-later
URL:            https://github.com/niccokunzmann/python-recurring-ical-events
Source:         https://files.pythonhosted.org/packages/source/r/%{distname}/%{distname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling >= 1.27.0}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module icalendar >= 6.1.0}
BuildRequires:  %{python_module python-dateutil >= 2.8.1}
BuildRequires:  %{python_module tzdata}
BuildRequires:  %{python_module x-wr-timezone >= 1.0.0}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytz >= 2023.3}
BuildRequires:  %{python_module restructuredtext_lint}
BuildRequires:  %{python_module x-wr-timezone}
# /SECTION
BuildRequires:  fdupes
Requires:       python-icalendar >= 6.1.0
Requires:       python-python-dateutil >= 2.8.1
Requires:       python-tzdata
Requires:       python-x-wr-timezone >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
Events, TODOs, Journal entries and Alarms can be repeated, removed from the feed and edited later on.

%prep
%autosetup -p1 -n %{distname}-%{version}
find . -name .gitignore -delete

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v -rs

%files %{python_files}
%license LICENSE
%{python_sitelib}/%{distname}
%{python_sitelib}/%{distname}-%{version}.dist-info

%changelog
