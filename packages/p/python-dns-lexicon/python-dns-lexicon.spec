#
# spec file for package python-dns-lexicon
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
%define skip_python2 1
Name:           python-dns-lexicon
Version:        3.9.4
Release:        0
Summary:        DNS record manipulation utility
License:        MIT
URL:            https://github.com/AnalogJ/lexicon
Source0:        https://github.com/AnalogJ/lexicon/archive/v%{version}.tar.gz#/lexicon-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION Python build system requirements
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module setuptools}
# /SECTION
# SECTION poetry.dependencies
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module tldextract}
# /SECTION
# SECTION extras
BuildRequires:  %{python_module PyNamecheap}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module localzone}
BuildRequires:  %{python_module softlayer => 5}
BuildRequires:  %{python_module transip >= 2}
BuildRequires:  %{python_module xmltodict}
# /section
# SECTION test dependencies
BuildRequires:  %{python_module pytest >= 3.8.0}
BuildRequires:  %{python_module vcrpy >= 1.13.0}
# /SECTION
Requires:       python-PyYAML
Requires:       python-beautifulsoup4
Requires:       python-cryptography
Requires:       python-future
Requires:       python-requests
Requires:       python-tldextract
Requires:       python-vcrpy
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-PyNamecheap
Recommends:     python-boto3
Recommends:     python-localzone
Recommends:     python-softlayer >= 5
Recommends:     python-transip >= 2
Recommends:     python-xmltodict
# Completely different pkg but same namespace
Conflicts:      python-lexicon
BuildArch:      noarch
%python_subpackages

%description
Lexicon provides a way to manipulate DNS records on multiple DNS providers
in a standardized way. Lexicon has a CLI, but it can also be used as a
Python library.

Lexicon was designed to be used in automation, specifically letsencrypt.

%prep
%autosetup -p1 -n lexicon-%{version}
# rpmlint
find . -type f -name ".gitignore" -delete

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lexicon
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_auto does not work inside OBS
%pytest lexicon/tests --ignore lexicon/tests/providers/test_auto.py --ignore lexicon/tests/providers/test_oci.py

%post
%python_install_alternative lexicon

%postun
%python_uninstall_alternative lexicon

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/lexicon
%{python_sitelib}/lexicon
%{python_sitelib}/dns_lexicon-%{version}*-info

%changelog
