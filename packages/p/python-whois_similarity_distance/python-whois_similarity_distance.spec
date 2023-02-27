#
# spec file for package python-whois_similarity_distance
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
%define skip_python36 1
Name:           python-whois_similarity_distance
Version:        1.0.2
Release:        0
Summary:        Python module for calculating the WHOIS Similarity Distance
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/stratosphereips/whois-similarity-distance
Source:         https://files.pythonhosted.org/packages/source/w/whois_similarity_distance/whois_similarity_distance-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Levenshtein
Requires:       python-certifi
Requires:       python-chardet
Requires:       python-ez_setup
Requires:       python-future
Requires:       python-idna
Requires:       python-numpy
Requires:       python-python-dateutil
Requires:       python-pythonwhois
Requires:       python-requests
Requires:       python-scikit-learn
Requires:       python-scipy
Requires:       python-six
Requires:       python-texttable
Requires:       python-tld
Requires:       python-urllib3
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       python-passivetotal
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Levenshtein}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module ez_setup}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module passivetotal}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pythonwhois}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module texttable}
BuildRequires:  %{python_module tld}
BuildRequires:  %{python_module urllib3}
# /SECTION
%python_subpackages

%description
This algorithm allows you to determine a numeric distance between two given domains, using their WHOIS information.

%prep
%setup -q -n whois_similarity_distance-%{version}
sed -i '1s/^#!.*//' whois_similarity_distance/wsd_domains.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/wsd_domains
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests

%post
%python_install_alternative wsd_domains

%postun
%python_uninstall_alternative wsd_domains

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%python_alternative %{_bindir}/wsd_domains
%{python_sitelib}/whois_similarity_distance
%{python_sitelib}/whois_similarity_distance-%{version}*-info

%changelog
