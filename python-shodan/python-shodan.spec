#
# spec file for package python-shodan
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
%{!?license: %global license %doc}
Name:           python-shodan
Version:        1.14.0
Release:        0
Summary:        Python library and command-line utility for Shodan
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/achillean/shodan-python/
Source:         https://files.pythonhosted.org/packages/source/s/shodan/shodan-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-XlsxWriter
Requires:       python-click
Requires:       python-click-plugins
Requires:       python-colorama
Requires:       python-requests >= 2.2.1
Requires:       python-setuptools
Recommends:     python-curses
Suggests:       %{name}-doc
BuildArch:      noarch

%python_subpackages

%package -n %{name}-doc
Summary:        Documentation files for %name
Group:          Documentation/HTML
Provides:       %{python_module shodan-doc = %{version}}

%description
Shodan is a search engine for Internet-connected devices. Google lets you search for websites, Shodan lets you search for devices. This library provides developers easy access to all of the data stored in Shodan in order to automate tasks and integrate into existing tools.

%description -n %{name}-doc
HTML documentation on the API and examples for %name.

%prep
%setup -q -n shodan-%{version}
sed -i '1s/^#!.*//' shodan/cli/worldmap.py

%build
%python_build
pushd docs
make html
rm -r _build/html/.buildinfo _build/html/_sources/
make man
popd

%install
%python_install
install -Dm 644 docs/_build/man/shodan-python.1 %{buildroot}%{_mandir}/man1/shodan.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests need network access, skip them:
# https://developer.shodan.io/api/requirements
# SHODAN-API-KEY file required by tests

%files %{python_files}
%defattr(-,root,root,-)
%doc AUTHORS README.rst
%%license LICENSE
%python3_only %{_bindir}/shodan
%{python_sitelib}/*
%python3_only %{_mandir}/man1/shodan.1%{ext_man}

%files -n %{name}-doc
%doc docs/_build/html

%changelog
