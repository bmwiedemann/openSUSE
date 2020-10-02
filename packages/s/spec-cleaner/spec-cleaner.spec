#
# spec file for package spec-cleaner
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.2.1
Release:        0
Summary:        .spec file cleaner
License:        BSD-3-Clause
URL:            https://github.com/openSUSE/spec-cleaner
Source0:        https://github.com/openSUSE/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-isort
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-setuptools
# For the pkg_resources used in the binary loader
Requires:       python3-setuptools
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
%setup -q -n %{name}-%{name}-%{version}

%build
%python3_build

%check
export LANG=en_US.UTF-8
python3 -m pytest -k "not webtest"

%install
%python3_install

%files
%license COPYING
%{_bindir}/%{name}
%dir %{_prefix}/lib/obs/
%dir %{_prefix}/lib/obs/service/
%{_prefix}/lib/obs/service/clean_spec_file
%{_prefix}/lib/obs/service/clean_spec_file.service
%dir %{python3_sitelib}/spec_cleaner/
%{python3_sitelib}/spec_cleaner/__init__.py
%{python3_sitelib}/spec_cleaner/__main__.py
%{python3_sitelib}/spec_cleaner/dependency_parser.py
%{python3_sitelib}/spec_cleaner/fileutils.py
%{python3_sitelib}/spec_cleaner/rpmbuild.py
%{python3_sitelib}/spec_cleaner/rpmcheck.py
%{python3_sitelib}/spec_cleaner/rpmcleaner.py
%{python3_sitelib}/spec_cleaner/rpmcopyright.py
%{python3_sitelib}/spec_cleaner/rpmdescription.py
%{python3_sitelib}/spec_cleaner/rpmexception.py
%{python3_sitelib}/spec_cleaner/rpmfiles.py
%{python3_sitelib}/spec_cleaner/rpmhelpers.py
%{python3_sitelib}/spec_cleaner/rpminstall.py
%{python3_sitelib}/spec_cleaner/rpmpreamble.py
%{python3_sitelib}/spec_cleaner/rpmpreambleelements.py
%{python3_sitelib}/spec_cleaner/rpmprep.py
%{python3_sitelib}/spec_cleaner/rpmprune.py
%{python3_sitelib}/spec_cleaner/rpmregexp.py
%{python3_sitelib}/spec_cleaner/rpmrequirestoken.py
%{python3_sitelib}/spec_cleaner/rpmpackage.py
%{python3_sitelib}/spec_cleaner/rpmscriplets.py
%{python3_sitelib}/spec_cleaner/rpmsection.py
%{python3_sitelib}/spec_cleaner/__pycache__
%{python3_sitelib}/spec_cleaner-%{version}-py%{py3_ver}.egg-info
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/excludes-bracketing.txt
%{_datadir}/%{name}/licenses_changes.txt
%{_datadir}/%{name}/pkgconfig_conversions.txt
%{_datadir}/%{name}/allowed_groups.txt
%{_datadir}/%{name}/licenses_exceptions.txt
%{_datadir}/%{name}/cmake_conversions.txt
%{_datadir}/%{name}/perl_conversions.txt
%{_datadir}/%{name}/tex_conversions.txt

%files format_spec_file
%{_prefix}/lib/obs/service/format_spec_file
%{_prefix}/lib/obs/service/format_spec_file.service

%changelog
