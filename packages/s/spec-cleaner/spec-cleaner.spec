#
# spec file for package spec-cleaner
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.2.3+1
Release:        0
Summary:        .spec file cleaner
License:        BSD-3-Clause
URL:            https://github.com/rpm-software-management/spec-cleaner
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-python-rpm-spec
BuildRequires:  python3-wheel
Requires:       python3-python-rpm-spec
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
%autosetup -p1
# Set correct package version, upstream has the next release number
sed -i 's/1\.2\.4/%{version}/g' spec_cleaner/__init__.py
rm pytest.ini

%build
%if 0%{?mageia}
%py3_build
%else
%python3_pyproject_wheel
%endif

%check
export LANG=en_US.UTF-8
# Tests that requires network
donttest="webtest or url_https.spec"
# Tests that requires network because of make_secure_url checking that
# the secure url exists
donttest+=" or source_https or rpmpreamble.spec or replace_pwdutils.spec or mingw32-clutter.spec"
python3 -m pytest -k "not ($donttest)" tests/*-tests.py

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
%{python3_sitelib}/spec_cleaner-*-info
%{_datadir}/%{name}

%files format_spec_file
%{_prefix}/lib/obs/service/format_spec_file
%{_prefix}/lib/obs/service/format_spec_file.service

%changelog
