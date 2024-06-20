#
# spec file for package openscap-report
#
# Copyright (c) 2024 SUSE LLC
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


Name:           openscap-report
Version:        0.2.6
Release:        0
Summary:        A tool for generating human-readable reports from (SCAP) XCCDF and ARF results
# The entire source code is LGPL-2.1+ and GPL-2.0+ and MIT except schemas/ and assets/, which are Public Domain
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND SUSE-Public-Domain
URL:            https://github.com/OpenSCAP/%{name}
Source0:        https://github.com/OpenSCAP/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx_rtd_theme
Requires:       python3-Jinja2
Requires:       python3-lxml
Provides:       bundled(patternfly) = 4
BuildArch:      noarch

%description
This package provides a command-line tool for generating
human-readable reports from SCAP XCCDF and ARF results.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
python3 setup.py build
sphinx-build -b man docs _build_docs

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -m 0644 -Dt %{buildroot}%{_mandir}/man1 _build_docs/oscap-report.1

# not sure how to do that:
#check
#tox

%files
%{_mandir}/man1/oscap-report.*
%{_bindir}/oscap-report
%exclude %{python3_sitelib}/tests/
%{python3_sitelib}/openscap_report/
%{python3_sitelib}/openscap_report-%{version}-py%{python3_bin_suffix}.egg-info/
%license LICENSE

%changelog
