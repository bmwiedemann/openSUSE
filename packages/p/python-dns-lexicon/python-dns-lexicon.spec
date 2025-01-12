#
# spec file for package python-dns-lexicon
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-dns-lexicon
Version:        3.20.1
Release:        0
Summary:        DNS record manipulation utility
License:        MIT
URL:            https://github.com/AnalogJ/lexicon
Source:         https://github.com/dns-lexicon/dns-lexicon/archive/refs/tags/v%{version}.tar.gz#/dns-lexicon-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION Python build system requirements
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
# /SECTION
# SECTION poetry.dependencies
BuildRequires:  %{python_module PyYAML >= 3}
BuildRequires:  %{python_module beautifulsoup4 >= 4}
BuildRequires:  %{python_module cryptography >= 3}
BuildRequires:  %{python_module pyotp}
BuildRequires:  %{python_module requests >= 2}
BuildRequires:  %{python_module tldextract >= 2}
# /SECTION
# SECTION extras
BuildRequires:  %{python_module boto3 >= 1.28}
BuildRequires:  %{python_module dnspython >= 2}
BuildRequires:  %{python_module localzone >= 0.9.8}
BuildRequires:  %{python_module softlayer => 5}
BuildRequires:  %{python_module softlayer-zeep >= 3}
# see comment in section testing below
# BuildRequires:  %%{python_module oci >= 2}
# /SECTION
# SECTION test dependencies
BuildRequires:  %{python_module pytest >= 3.8.0}
BuildRequires:  %{python_module vcrpy >= 1.13.0}
# OCI hijacks all connections during unit testing and lets them fail, we can't allow that on OBS
BuildConflicts: %{python_module oci}
# /SECTION
Requires:       python-PyYAML >= 3
Requires:       python-beautifulsoup4 >= 4
Requires:       python-cryptography >= 2
Requires:       python-dnspython >= 2
Requires:       python-pyotp
Requires:       python-requests >= 2
Requires:       python-tldextract >= 2
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-boto3 >= 1.28
Recommends:     python-localzone >= 0.9.8
Recommends:     python-oci >= 2
Recommends:     python-softlayer >= 5
Recommends:     python-softlayer-zeep >= 3
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
%autosetup -p1 -n dns-lexicon-%{version}
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
ignoretests="--ignore tests/providers/test_auto.py"
# no oci in test suite, see comment above
ignoretests="$ignoretests --ignore tests/providers/test_oci.py"
# test_namecheap has invalid vcr casettes, attempts to update them failed
ignoretests="$ignoretests --ignore tests/providers/test_namecheap.py"
ignoretests="$ignoretests --ignore tests/providers/test_godaddy.py"
%pytest tests $ignoretests -x

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
