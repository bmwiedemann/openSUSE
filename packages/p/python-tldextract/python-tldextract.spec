#
# spec file for package python-tldextract
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-tldextract
Version:        3.0.1
Release:        0
Summary:        Python module to separate the TLD of a URL
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/john-kurkowski/tldextract
Source:         https://files.pythonhosted.org/packages/source/t/tldextract/tldextract-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
### BEGIN test requirements
BuildRequires:  %{python_module filelock} >= 3.0.8
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-file} >= 1.4
BuildRequires:  %{python_module requests} >= 2.1.0
BuildRequires:  %{python_module responses}
### END test requirements
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-filelock >= 3.0.8
Requires:       python-idna >= 2.1.0
Requires:       python-requests >= 2.1.0
Requires:       python-requests-file >= 1.4
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      python-tldextract <= 2.0.1
BuildArch:      noarch
%python_subpackages

%description
tldextract accurately separates the gTLD or ccTLD (generic or country code
top-level domain) from the registered domain and subdomains of a URL, using the
Public Suffix List. By default, this includes the public ICANN TLDs and their
exceptions. You can optionally support the Public Suffix List's private domains
as well.

%prep
%setup -q -n tldextract-%{version}

%build
sed -i 's:--pylint::' pytest.ini
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/tldextract
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py develop --user
%pytest tests

%post
%python_install_alternative tldextract

%postun
%python_uninstall_alternative tldextract

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*
%python_alternative %{_bindir}/tldextract

%changelog
