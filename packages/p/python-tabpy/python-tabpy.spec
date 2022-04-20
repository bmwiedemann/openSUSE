#
# spec file for package python-tabpy
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
%define         skip_python2 1
%define         skip_python36 1
Name:           python-tabpy
Version:        2.5.0
Release:        0
Summary:        Tableau Python service
License:        MIT
URL:            https://github.com/tableau/TabPy
Source:         https://github.com/tableau/TabPy/archive/%{version}.tar.gz#/tabpy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted
Requires:       python-cloudpickle
Requires:       python-docopt
Requires:       python-genson
Requires:       python-jsonschema
Requires:       python-pyOpenSSL
Requires:       python-requests
Requires:       python-simplejson
Requires:       python-tornado
Recommends:     python-nltk
Recommends:     python-numpy
Recommends:     python-pandas
Recommends:     python-scikit-learn
Recommends:     python-scipy
Suggests:       python-textblob
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module genson}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module nltk}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module tornado}
# scikit-learn dropped support for Python 3.6
# /SECTION
%python_subpackages

%description
Tableau service to run Python scripts.

%prep
%setup -q -n TabPy-%{version}
chmod a-x CHANGELOG README.md tabpy/VERSION
# These packages are optional, used mostly in one script,
# and textblob isnt yet packaged for openSUSE, and requires
# many nltk data packages to be created to be functional.
sed -Ei '/(nltk|numpy|pandas|scipy|sklearn|textblob)/d' setup.py
# future & hypothesis are not used; pytest-runner not needed
sed -Ei '/(future|hypothesis|pytest-runner)/d' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/tabpy
%python_clone -a %{buildroot}%{_bindir}/tabpy-deploy-models
%python_clone -a %{buildroot}%{_bindir}/tabpy-user
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
mkdir -p ~/bin
export PATH=~/bin:$PATH
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
cp %{buildroot}/%{_bindir}/tabpy-%{$python_bin_suffix} ~/bin/tabpy
$python -m pytest -k 'not integration' tests
}

%post
%python_install_alternative tabpy tabpy-deploy-models tabpy-user

%postun
%python_uninstall_alternative tabpy

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%python_alternative %{_bindir}/tabpy
%python_alternative %{_bindir}/tabpy-deploy-models
%python_alternative %{_bindir}/tabpy-user
%{python_sitelib}/*

%changelog
