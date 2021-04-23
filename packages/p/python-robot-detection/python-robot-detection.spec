#
# spec file for package python-robot-detection
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define skip_python2 1
Name:           python-robot-detection
Version:        0.4.0
Release:        0
Summary:        HTTP User Agent Bot Detection
License:        GPL-3.0-or-later
URL:            https://github.com/rory/robot-detection
# https://github.com/rory/robot-detection/issues/2
Source0:        https://github.com/rory/robot-detection/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Library for detecting if a HTTP User Agent header is likely to be a bot.

%prep
%setup -q -n robot-detection-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover

%files %{python_files}
%doc README.md
%license LICENCE
%{python_sitelib}/*

%changelog
