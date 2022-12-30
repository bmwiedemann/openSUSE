#
# spec file for package python-isoduration
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


Name:           python-isoduration
Version:        20.11.0
Release:        0
Summary:        Operations with ISO 8601 durations
License:        ISC
URL:            https://github.com/bolsote/isoduration
Source:         https://github.com/bolsote/isoduration/archive/refs/tags/%{version}.tar.gz#/isoduration-%{version}-gh.tar.gz
BuildRequires:  %{python_module arrow >= 0.15.0}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
# SECTION test
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-arrow >= 0.15.0
BuildArch:      noarch
%python_subpackages

%description
ISO 8601 is most commonly known as a way to exchange datetimes in textual format.
A lesser known aspect of the standard is the representation of durations. They
have a shape similar to this:

    P3Y6M4DT12H30M5S

This string represents a duration of 3 years, 6 months, 4 days, 12 hours,
30 minutes, and 5 seconds.

The state of the art of ISO 8601 duration handling in Python is more or less
limited to what's offered by isodate. What we are trying to achieve here is to
address the shortcomings of isodate (as described in their own Limitations section),
and a few of our own annoyances with their interface, such as the lack of uniformity
in their handling of types, and the use of regular expressions for parsing.

%prep
%setup -q -n isoduration-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%{python_sitelib}/isoduration
%{python_sitelib}/isoduration-%{version}.dist-info

%changelog
