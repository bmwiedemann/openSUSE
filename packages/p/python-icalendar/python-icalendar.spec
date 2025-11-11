#
# spec file for package python-icalendar
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2011 open-slx GmbH <Sascha.Manns@open-slx.de>
# Copyright (c) 2009 - 7/2011 Sascha Manns <saigkill@opensuse.org>
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


%define	modname icalendar
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        6.3.2
Release:        0
Summary:        Python parser/generator of iCalendar files package
License:        BSD-2-Clause
URL:            https://github.com/collective/icalendar
Source0:        https://files.pythonhosted.org/packages/source/i/icalendar/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module tzdata}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-tzdata
Suggests:       python-pytz
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}
BuildArch:      noarch
%python_subpackages

%description
The iCalendar package is a parser/generator of iCalendar files for use
with Python. It follows the RFC 2445 (iCalendar) specification.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/icalendar
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# some dependencies are too old in Leap
%if 0%{?suse_version} >= 1550
donttest="(test_timezone_names_are_known and tzp_0-America/Coyhaique)"
donttest+=" or (test_timezone_names_are_known and tzp_0-Asia/Beijing)"
%pytest -k "not ($donttest)" src
%endif

%post
%python_install_alternative icalendar

%postun
%python_uninstall_alternative icalendar

%files %{python_files}
%license LICENSE.rst
%doc README.rst docs/changelog.rst
%python_alternative %{_bindir}/icalendar
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info

%changelog
