#
# spec file for package python-dns-lexicon
#
# Copyright (c) 2020 SUSE LLC
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
Version:        3.3.19
Release:        0
Summary:        DNS record manipulation utility
License:        MIT
URL:            https://github.com/AnalogJ/lexicon
Source0:        https://github.com/AnalogJ/lexicon/archive/v%{version}.tar.gz#/lexicon-%{version}.tar.gz
BuildRequires:  %{python_module PyNamecheap}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module dnspython >= 1.15.0}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module localzone}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module pytest >= 3.8.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module softlayer}
BuildRequires:  %{python_module tldextract}
BuildRequires:  %{python_module transip >= 0.3.0}
BuildRequires:  %{python_module vcrpy >= 1.13.0}
BuildRequires:  %{python_module xmltodict}
BuildRequires:  %{python_module zeep}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyNamecheap
Requires:       python-PyYAML
Requires:       python-beautifulsoup4
Requires:       python-boto3
Requires:       python-cryptography
Requires:       python-dnspython >= 1.15.0
Requires:       python-future
Requires:       python-localzone
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-softlayer
Requires:       python-tldextract
Requires:       python-transip >= 0.3.0
Requires:       python-vcrpy
Requires:       python-xmltodict
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%setup -q -n lexicon-%{version}
# Remove, since they are completely broken
rm lexicon/tests/providers/test_auto.py

# rpmlint
find . -type f -name ".gitignore" -delete

%build
%python_build

# rpmlint
find . -type f -name ".buildinfo" -delete

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/lexicon
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest lexicon/tests

%post
%python_install_alternative lexicon

%postun
%python_uninstall_alternative lexicon

%files %{python_files}
%{python_sitelib}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/lexicon

%changelog
