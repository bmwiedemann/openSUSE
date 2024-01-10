#
# spec file for package spec-cleaner
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2012 Vincent Untz <vuntz@opensuse.org>
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


Name:           spec-cleaner
Version:        1.2.2
Release:        0
Summary:        .spec file cleaner
License:        BSD-3-Clause
URL:            https://github.com/rpm-software-management/spec-cleaner
Source0:        https://github.com/rpm-software-management/spec-cleaner/archive/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: https://github.com/rpm-software-management/spec-cleaner/commit/fd0f64930a399dfcf4ff5d3e22a8ec9afa37043a
Patch0:         fix_tests_needing_web_connection.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-wheel
# For the pkg_resources used in the binary loader
BuildArch:      noarch

%description
This script cleans spec file according to some arbitrary style guide. The
results it produces should always be checked by someone since it is not and
will never be perfect.

%package format_spec_file
Summary:        Binding replacing OBS service format_spec_file
Requires:       %{name} = %{version}
Conflicts:      obs-service-format_spec_file

%description format_spec_file
Alternative provider of format_spec_file functionality in order to allow
user to use spec-cleaner rather than to stick to perl based format_spec_file.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
rm pytest.ini

%build
%if 0%{?mageia}
%py3_build
%else
%python3_pyproject_wheel
%endif

%check
export LANG=en_US.UTF-8
python3 -m pytest -k "not webtest" tests/*-tests.py

%install
%if 0%{?mageia}
%py3_install
%else
%python3_pyproject_install
%endif
%fdupes %{buildroot}%{python3_sitelib}

%files
%license COPYING
%{_bindir}/%{name}
%dir %{_prefix}/lib/obs/
%dir %{_prefix}/lib/obs/service/
%{_prefix}/lib/obs/service/clean_spec_file
%{_prefix}/lib/obs/service/clean_spec_file.service
%{python3_sitelib}/spec_cleaner
%{python3_sitelib}/spec_cleaner-%{version}*-info
%{_datadir}/%{name}

%files format_spec_file
%{_prefix}/lib/obs/service/format_spec_file
%{_prefix}/lib/obs/service/format_spec_file.service

%changelog
