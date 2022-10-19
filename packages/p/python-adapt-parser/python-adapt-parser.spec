#
# spec file for package python-adapt-parser
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-adapt-parser
Version:        1.0.0
Release:        0
Summary:        A text-to-intent parsing framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/MycroftAI/adapt
Source:         https://github.com/MycroftAI/adapt/archive/refs/tags/release/v%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove-python-six.patch
Patch:          remove-python-six.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The Adapt Intent Parser is a flexible and extensible intent definition and
determination framework. It is intended to parse natural language text into
a structured intent that can then be invoked programatically.

%prep
%autosetup -p1 -n adapt-release-v%{version}
sed -i -s "s/==/>=/" requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test/*.py

%files %{python_files}
%license LICENSE.md
%doc README.md SUPPORT.md GETTING_STARTED.md
%{python_sitelib}/adapt
%{python_sitelib}/adapt_parser-%{version}*-info

%changelog
