#
# spec file for package python-structlog
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-structlog
Version:        19.1.0
Release:        0
Summary:        Structured Logging for Python
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Python
URL:            http://www.structlog.org/en/stable/
Source:         https://github.com/hynek/structlog/archive/%{version}.tar.gz
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module freezegun >= 0.2.8}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest >= 3.3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%if %{python_version_nodots} >= 36
BuildRequires:  python3-rapidjson
%endif
%python_subpackages

%description
structlog makes logging in Python less painful and more powerful by adding
structure to your log entries.

It’s up to you whether you want structlog to take care about the output of your
log entries or whether you prefer to forward them to an existing logging system
like the standard library’s logging module.

%prep
%setup -q -n structlog-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGE* README*
%license LICENSE*
%{python_sitelib}/*

%changelog
