#
# spec file for package python-patatt
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-patatt
Version:        0.6.3
Release:        0
Summary:        Cryptographic patch attestation for the masses
License:        MIT-0
URL:            https://git.kernel.org/pub/scm/utils/patatt/patatt.git/
Source0:        https://git.kernel.org/pub/scm/utils/patatt/patatt.git/snapshot/patatt-%{version}.tar.gz
Source1:        https://git.kernel.org/pub/scm/utils/patatt/patatt.git/snapshot/patatt-%{version}.tar.asc
Source2:        python-patatt.keyring
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
This utility allows an easy way to add end-to-end cryptographic attestation to
patches sent via mail. It does so by adapting the DKIM email signature standard
to include cryptographic signatures via the X-Developer-Signature email header.

If your project workflow doesn't use patches sent via email, then you don't
need this and should simply start signing your tags and commits.

%prep
%autosetup -n patatt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/patatt
%python_clone -a %{buildroot}%{_mandir}/man5/patatt.5

%check
# try at least a simple runtime test
%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" %{buildroot}%{_bindir}/patatt-%{$python_bin_suffix} --version | grep -q %{version}

%pre
%python_libalternatives_reset_alternative patatt

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/patatt
%python_alternative %{_mandir}/man5/patatt.5%{?ext_man}
%{python_sitelib}/patatt
%{python_sitelib}/patatt-%{version}*-info

%changelog
